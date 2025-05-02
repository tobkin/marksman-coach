import os
import streamlit as st
from PIL import Image
import pandas as pd
import time
import numpy as np

# Initialize session state
if 'playing' not in st.session_state:
    st.session_state['playing'] = False
if 'current_frame' not in st.session_state:
    st.session_state['current_frame'] = 0
if 'fps' not in st.session_state:
    st.session_state['fps'] = 60
if 'frames_data' not in st.session_state:
    st.session_state['frames_data'] = None

# Function to toggle play/pause
def toggle_play():
    st.session_state['playing'] = not st.session_state['playing']

# Remove default Streamlit padding
st.markdown(
    """
    <style>
        .block-container {
            max-width: 1400px;
            padding-left: 2rem;
            padding-right: 2rem;
        }
        .green-text {
            color: green;
        }
        section.stMain .block-container {
        padding-top: 0rem;
        z-index: 1;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# --- Define Paths ---
current_dir = os.path.dirname(os.path.abspath(__file__))
video_path = os.path.join(current_dir, "./assets/marksman-pipes-vid.mov")
banner_path = os.path.join(current_dir, "./assets/banner.png")
frames_path = os.path.join(current_dir, "./data/frames")
st.markdown("&nbsp;")  # Add empty space
st.image(banner_path)
st.title("Marksman Trainer")
st.markdown(
    """ 
    A tool that takes your shooting video and gives you real-time  
    feedback on your fundamentals.
    """
)

# --- SideBar ---
DATA_SOURCE_REAL_DATA_SIDEBAR_OPTION="Real Data"
DATA_SOURCE_STUB_DATA_SIDEBAR_OPTION="Stub Data"

st.sidebar.title("Navigation")

data_source = st.sidebar.radio("Select Data Source:",
    options = [
        DATA_SOURCE_REAL_DATA_SIDEBAR_OPTION,
        DATA_SOURCE_STUB_DATA_SIDEBAR_OPTION
    ], captions=["",""]
    )

# --- Get frame files from directory ---
frame_files = sorted([
    os.path.join(frames_path, fname)
    for fname in os.listdir(frames_path)
    if fname.lower().endswith(('.png', '.jpg', '.jpeg'))
]) 

# --- Load frames efficiently ---
# Only load frames data once and store in session state
if st.session_state['frames_data'] is None:
    # Show loading message
    with st.spinner("Loading frames... This may take a moment."):
        frames_data = []
        # Process in batches to avoid too many open files
        BATCH_SIZE = 50
        
        # Create a progress bar
        progress_bar = st.progress(0)
        total_files = len(frame_files)
        
        for i in range(0, total_files, BATCH_SIZE):
            batch_files = frame_files[i:i+BATCH_SIZE]
            batch_frames = []
            
            for f in batch_files:
                with Image.open(f) as img:
                    # Convert to RGB to ensure consistency
                    if img.mode != 'RGB':
                        img = img.convert('RGB')
                    # Store as numpy array to fully detach from file handle
                    batch_frames.append(np.array(img))
            
            frames_data.extend(batch_frames)
            
            # Update progress bar
            progress = min(i + BATCH_SIZE, total_files) / total_files
            progress_bar.progress(progress)
                
        st.session_state['frames_data'] = frames_data
        # Clear the progress bar when done
        progress_bar.empty()
        st.success(f"Successfully loaded {len(frames_data)} frames")

# Get frames from session state
frames_data = st.session_state['frames_data']

# --- Load Predictions ---
try:
    if data_source == DATA_SOURCE_STUB_DATA_SIDEBAR_OPTION:
        predictions = pd.read_csv("./data/pose-estimations/stub/stub-predictions.csv")
    else:
        predictions = pd.read_csv("./data/pose-estimations/stub/stub-predictions.csv")
    # Limit frames to match predictions if needed
    if len(frames_data) > len(predictions):
        frames_data = frames_data[:len(predictions)]
except Exception as e:
    st.warning(f"Could not load predictions: {e}")
    predictions = None

# Frame selection slider with callback
def on_frame_change():
    if not st.session_state['playing']:
        st.session_state['current_frame'] = st.session_state['frame_slider']

current_frame = st.slider(
    "Frame", 
    0, 
    len(frames_data)-1, 
    st.session_state['current_frame'], 
    key="frame_slider",
    on_change=on_frame_change
)

# Play/Pause button
if st.button("Play/Pause"):
    toggle_play()
    if not st.session_state['playing']:
        st.session_state['current_frame'] = st.session_state['frame_slider']

# Update frame only if playing
if st.session_state['playing']:
    st.session_state['current_frame'] = (st.session_state['current_frame'] + 5) % len(frames_data)

# Get current frame index for display
current_idx = st.session_state['current_frame']

# Prepare feedback data
if predictions is not None and current_idx < len(predictions):
    # Get all the values for current frame
    values = [
        predictions['head_position'][current_idx] if 'head_position' in predictions else "Good",
        predictions['rifle_butt_placement'][current_idx] if 'rifle_butt_placement' in predictions else "Good",
        predictions['non_firing_hand_position'][current_idx] if 'non_firing_hand_position' in predictions else "Good",
        predictions['elbow_placement'][current_idx] if 'elbow_placement' in predictions else "Good",
        predictions['natural_point_of_aim'][current_idx] if 'natural_point_of_aim' in predictions else "Good",
        predictions['balance'][current_idx] if 'balance' in predictions else "Good",
        predictions['relaxation'][current_idx] if 'relaxation' in predictions else "Good"
    ]
    
    # Define component names
    fundamentals = [
        "Head Position", 
        "Rifle Butt Placement", 
        "Non-Firing Hand Position", 
        "Elbow Placement", 
        "Natural Point of Aim", 
        "Balance", 
        "Relaxation"
    ]
else:
    # Fallback static components
    fundamentals = [
        "Head Position", 
        "Rifle Butt Placement", 
        "Non-Firing Hand Position", 
        "Elbow Placement", 
        "Natural Point of Aim", 
        "Balance", 
        "Relaxation"
    ]
    values = ["Good", "Good", "Good", "Good", "Good", "Good", "Good"]

# Create inline layout with image and feedback side by side
col1, col2 = st.columns([3, 2])

with col1:
    # Display current frame - convert numpy array back to image
    current_frame_img = Image.fromarray(frames_data[current_idx])
    st.image(current_frame_img, caption=f"Frame {current_idx+1}/{len(frames_data)}")

with col2:
    st.subheader("Feedback")
    
    # Display feedback
    for i in range(len(fundamentals)):
        cols = st.columns([3, 2])
        component = fundamentals[i]
        grade = str(values[i]).upper()
        
        with cols[0]:
            st.write(component)
        with cols[1]:
            if str(values[i]).lower() == "good":
                st.markdown(f"<span style='color:green; font-weight:bold;'>{grade}</span>", unsafe_allow_html=True)
            else:
                st.markdown(f"<span style='color:red; font-weight:bold;'>{grade}</span>", unsafe_allow_html=True)
        
        # Only add divider if not the last item
        if i < len(fundamentals) - 1:
            st.markdown("<hr style='margin: 0; padding: 0; height: 1px; background-color: #363636;'>", unsafe_allow_html=True)

# --- Footer ---
st.markdown("---")
st.markdown("""
Created by Toby Tobkin, Paul Kim, Ryan Loper
""")

# Simple controlled rerun if playing
if st.session_state['playing']:
    time.sleep(1.0 / st.session_state['fps'])
    st.rerun()
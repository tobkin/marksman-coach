import os
import streamlit as st
from PIL import Image
import pandas as pd
import time

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
        .stButton>button {
            width: 100%;
        }
        .frame-counter {
            text-align: center;
            font-size: 16px;
            margin-top: 5px;
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

st.image(banner_path)
st.title("Marksman Trainer")
st.markdown(
    """ 
    A tool that takes your shooting video and gives you real-time  
    feedback on your fundamentals.
    """
)

# --- Get frames from file ---
frame_files = sorted([
    os.path.join(frames_path, fname)
    for fname in os.listdir(frames_path)
    if fname.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp'))
]) 
frames = [Image.open(f) for f in frame_files]

# --- Components ---
components = [
    {"Component": "Head Position", "Grade": "Good"},
    {"Component": "Rifle Butt Placement", "Grade": "Good"},
    {"Component": "Non-firing Hand Position", "Grade": "Good"},
    {"Component": "Elbow Placement", "Grade": "Good"},
    {"Component": "Natural Point of Aim", "Grade": "Good"},
    {"Component": "Balance", "Grade": "Good"},
    {"Component": "Relaxation", "Grade": "Good"},
]


col1, col2 = st.columns([3, 2])

with col1:
    # st.video(video_path, start_time="1s", end_time="15s")
    if frames:
        idx = st.slider("Frame", 0, len(frames)-1, 0)
        st.image(frames[idx], caption=f"Frame {idx+1}")

with col2:
    st.subheader("Feedback")
    
   # Create a clean display without using HTML tables
    for row in components:
        component = row['Component']
        grade = row['Grade']
        
        cols = st.columns([3, 2])
        capitalized_value = values[i].upper()
        with cols[0]:
            st.write(fundamentals[i])
        with cols[1]:
            if values[i] == "good":
                st.markdown(f"<span style='color:green; font-weight:bold;'>{capitalized_value}</span>", unsafe_allow_html=True)
            else:
                st.markdown(f"<span style='color:red; font-weight:bold;'>{capitalized_value}</span>", unsafe_allow_html=True)
        
        # Only add divider if it's not the last item
        if i < len(fundamentals) - 1:
            st.markdown("<hr style='margin: 0; padding: 0; height: 1px; background-color: #363636;'>", unsafe_allow_html=True)

# --- Footer ---
st.markdown("---")
st.markdown("""
Created by Toby Tobkin, Paul Kim, Ryan Loper
""")

# The playback logic
if st.session_state.playing:
    frame_delay = 1.0 / st.session_state.fps
    
    # Display current frame
    frame_container.image(frames[st.session_state.current_frame], caption=f"Playing at {st.session_state.fps} FPS")
    progress_container.markdown(
        f"<div class='frame-counter'>Frame {st.session_state.current_frame + 1}/{len(frames)}</div>",
        unsafe_allow_html=True
    )
    
    # Increment frame
    st.session_state.current_frame += 1
    
    # Reset if we reach the end
    if st.session_state.current_frame >= len(frames):
        st.session_state.current_frame = 0
        st.session_state.playing = False
        st.experimental_rerun()
    
    # Control timing for proper FPS
    time.sleep(frame_delay)
    st.experimental_rerun()
else:
    # Display current frame when not playing
    frame_container.image(frames[st.session_state.current_frame], caption=f"Frame {st.session_state.current_frame + 1}/{len(frames)}")
    progress_container.markdown(
        f"<div class='frame-counter'>Frame {st.session_state.current_frame + 1}/{len(frames)}</div>",
        unsafe_allow_html=True
    )
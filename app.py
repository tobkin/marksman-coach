import os
import streamlit as st
from PIL import Image
import pandas as pd
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
st.title( "Marksman Trainer")
st.markdown(
    """ 
    A tool that takes your shooting video and gives you real-time  
    feedback on your fundamentals.
    """
)

# --- Layout: Video and Text Side-by-Side ---
#get frames from file
frames = frame_files = sorted([
    os.path.join(frames_path, fname)
    for fname in os.listdir(frames_path)
]) 
# --- Load Predictions ---
predictions = pd.read_csv("./data/stub/stub-predictions.csv")

# --- Limit Frames (fix later) ---
frames = [Image.open(f) for f in frames[:len(predictions)]]

col1, col2 = st.columns([3, 2])

with col1:
    idx = st.slider("Frame", 0, len(frames)-1, 0)
    st.image(frames[idx], caption=f"Frame {idx+1}")

with col2:
   # Assuming fundamentals is a list of the names of the fundamentals in the same order
    fundamentals = [
        "Head Position", 
        "Rifle Butt Placement", 
        "Non-Firing Hand Position", 
        "Elbow Placement", 
        "Natural Point of Aim", 
        "Balance", 
        "Relaxation"
    ]

    # Get all the values
    values = [
        predictions['head_position'][idx],
        predictions['rifle_butt_placement'][idx],
        predictions['non_firing_hand_position'][idx],
        predictions['elbow_placement'][idx],
        predictions['natural_point_of_aim'][idx],
        predictions['balance'][idx],
        predictions['relaxation'][idx]
    ]

    # Display all fundamentals and their grades
    st.subheader("Shooting Fundamentals Feedback")

    for i in range(len(fundamentals)):
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

"""
)
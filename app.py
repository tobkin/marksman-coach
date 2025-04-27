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


col1, col2 = st.columns([3, 2])  # Adjust the ratio as you like

with col1:
    # st.video(video_path, start_time="1s", end_time="15s")
    if frames:
        idx = st.slider("Frame", 0, len(frames)-1, 0)
        st.image(frames[idx], caption=f"Frame {idx+1}")

with col2:
    st.subheader("Feedback")
    
    # Create the HTML table manually
    table_html = """
    <style>
    .custom-table {
        border-collapse: collapse;
        width: 100%;
    }
    .custom-table td {
        border: 1px solid #363636;
        padding: 6px 12px;
        font-size: 16px;
    }
    </style>
    <table class="custom-table">
    """
    
    # Add rows
    for row in components:
        table_html += f"<tr><td>{row['Component']}</td><td>{row['Grade']}</td></tr>"
    
    table_html += "</table>"
    
    st.write(table_html, unsafe_allow_html=True)


# --- Footer ---
st.markdown("---")
st.markdown("""

Created by Toby Tobkin, Paul Kim, Ryan Loper

"""
)
import os
import streamlit as st

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
current_dir = os.path.dirname(os.path.abspath(__file__))
video_path = os.path.join(current_dir, "shooting-video.mov")

st.title("Marksman Trainer")
st.markdown(
    """ 
    A tool that takes your shooting video and gives you real-time  
    feedback on your fundamentals.
    """
)

# --- Layout: Video and Text Side-by-Side ---
col1, col2 = st.columns([3, 2])  # Adjust the ratio as you like

with col1:
    st.video(video_path, start_time="1s", end_time="15s")

with col2:
    st.subheader("Feedback")
    st.markdown(
        """
        Head Position: <span class="green-text">Good</span> \n
        Rifle Butt Placement: <span class="green-text">Good</span> \n
        Non-firing Hand Position: <span class="green-text">Good</span> \n
        Elbow Placement: <span class="green-text">Good</span> \n
        Natural Point of Aim: <span class="green-text">Good</span> \n
        Balance: <span class="green-text">Good</span> \n
        Relaxation: <span class="green-text">Good</span>
        """,
        unsafe_allow_html=True
    )

# --- Footer ---
st.markdown("---")
st.markdown("""

Created by Toby Tobkin, Paul Kim, Ryan Loper

"""
)
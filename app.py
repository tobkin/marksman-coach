import os
import streamlit as st

current_dir = os.path.dirname(os.path.abspath(__file__))
video_path = os.path.join(current_dir, "shooting-video.mov")

st.title("Marksman Trainer")
st.markdown(
    """ 
      A tool that takes your shooting video and gives you real time
      feeeback on your fundamentals.
    """
)

st.video(video_path, start_time="1s", end_time="15s")


st.markdown(
    """
    Footer
    """
)

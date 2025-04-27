import streamlit as st
import pandas as pd

st.title("The Marksman Training Solution")

st.write("### What is pose analysis?")
st.image("./assets/pitch/singapore-marksman-pose-analysis.png", caption="Singapore marksman using pose analysis")
st.write("""
    Pose analysis is a computer vision technology that tracks human body positions and movements in real-time. 
    Originally developed for sports and physical therapy applications, it uses AI to identify key body landmarks 
    and measure joint angles with high precision. This technology has evolved from research labs to practical 
    applications over the past decade, with Google's MediaPipe making it accessible for edge devices.
    
    For military training, pose analysis offers an objective, consistent way to evaluate and improve 
    fundamental skills without increasing instructor workload or ammunition consumption. It transforms 
    traditional training by providing quantitative feedback that human observation alone might miss.
""")

st.write("### How can it be used to assess marksmanship fundamentals?")
st.image("./assets/pitch/canva-mockup.png", caption="Concept: Pose analysis technology applied to marksmanship training")

data = {
    "Element": [
        "Head Position", 
        "Rifle Butt Placement", 
        "Non-firing Hand Position", 
        "Elbow Placement", 
        "Natural Point of Aim", 
        "Balance", 
        "Relaxation"
    ],
    "API Measurements": [
        "neck_lateral_flexion, neck_forward_flexion", 
        "shoulder_extension", 
        "elbow_side", 
        "elbow_side", 
        "shoulder_extension, elbow_side, hip_side", 
        "hip_side, knee_side", 
        "All joint angles"
    ],
    "Measurement Strategy": [
        "Calculate deviation from vertical (0 degrees +/- 5 degrees). Flag if lateral flexion > 10 degrees or forward flexion > 15 degrees",
        "Measure angle between torso and upper arm: optimal = 45 degrees +/- 10 degrees. Distance from shoulder joint to stock should be consistent (+/-1cm)",
        "Calculate angle of support arm: optimal = 30-40 degrees between upper arm and forearm. Distance from barrel to non-firing hand = 15-20cm",
        "Measure vertical drop from shoulder: optimal position = shoulder width - 5cm. Angle between upper arm and forearm should be 90 degrees +/- 15 degrees",
        "Apply vector projection of body alignment vs. target line. Calculate angular deviation between rest position and aiming position (< 5 degrees)",
        "Compute center of mass using knee (k), hip (h), and shoulder (s) coordinates: CoM = (k+h+s)/3. Measure foot stance width (optimal = 1.5x shoulder width)",
        "Compute variance in joint angles over 3-second interval. Low variance (sigma^2 < 2 degrees) indicates proper muscle relaxation"
    ]
}

df = pd.DataFrame(data)
df = df.set_index("Element")
st.table(df.style.set_properties(subset=['API Measurements'], **{'width': '170px'}))


st.write("### Pose analysis using Quickpose")
st.image("./assets/pitch/quickpose-sports-performance-pdp.png", caption="Quickpose: A high-level wrapper around MediaPipe Pose")
st.write("### API Implementation")
st.code("""measurement=elbow_side,shoulder_extension,neck_lateral_flexion,neck_forward_flexion,hip_side,knee_side
side=both""", language="text")
# todo explain that quickpose is a high-level wrapper around mediapipe pose
# code snippet: the API call to the quickpose model
# drag selector the same as in Marksman_Trainer.py to select the frame jpg
# two columns: one for input frame, one for output frame

st.write("### Pose analysis using Mediapipe")
# todo explain that mediapipe is a lower-level library that quickpose is built on top of
st.image("./assets/pitch/mediapipe-pose-github-tearsheet.png", caption="MediaPipe Pose: The underlying library for Quickpose. Can be used for directly fine-tuning custom pose analysis use cases.")
# code snippet: the API call to the mediapipe pose model
# drag selector the same as in Marksman_Trainer.py to select the frame jpg
# two columns: one for input frame, one for output frame

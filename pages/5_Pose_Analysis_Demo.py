import streamlit as st
import pandas as pd

st.title("The Marksman Training Solution")

st.write("## What is pose analysis?")
# todo: make a short, concise, business-focused explanation of what pose analysis is and its history

st.write("## How can it be used to assess marksmanship fundamentals?")
# todo: make a streamlit table from this context:

# Create dataframe with marksman position measurement strategies
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
st.table(df)

st.write("## API Implementation")
st.code("""measurement=elbow_side,shoulder_extension,neck_lateral_flexion,neck_forward_flexion,hip_side,knee_side
side=both""", language="text")

st.write("## Pose analysis using Quickpose")
# todo explain that quickpose is a high-level wrapper around mediapipe pose
# code snippet: the API call to the quickpose model
# drag selector the same as in Marksman_Trainer.py to select the frame jpg
# two columns: one for input frame, one for output frame

st.write("## Pose analysis using Mediapipe")
# todo explain that mediapipe is a lower-level library that quickpose is built on top of
# todo: 300px wide screenshot of ./assets/pitch/mediapipe-pose-github-tearsheet.png
# code snippet: the API call to the mediapipe pose model
# drag selector the same as in Marksman_Trainer.py to select the frame jpg
# two columns: one for input frame, one for output frame

st.image("./assets/training-ratio.jpg", width=500)
st.image("./assets/training-accident.jpg", width=500)

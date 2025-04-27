import streamlit as st
import pandas as pd
import os
import glob
import requests
import json

# Set page layout to wide format
st.set_page_config(layout="wide")

st.title("Pose Analysis Demo & Technical Explanation")

# Create inferences directory if it doesn't exist
os.makedirs("./inferences", exist_ok=True)

# Load API key and mask it
api_key_path = "./secrets/quickpose-api-key.txt"
if os.path.exists(api_key_path):
    with open(api_key_path, "r") as f:
        api_key = f.read().strip()
        masked_key = "*" * (len(api_key) - 4) + api_key[-4:]
else:
    masked_key = "<Your API Key>"
    api_key = None
    st.warning("API key not found. Please place your Quickpose API key in ./secrets/quickpose-api-key.txt")

# Frame selector for Quickpose
st.subheader("Quickpose Frame Analysis")
frame_files = sorted(glob.glob("./data/frames/*.jpg"))

frame_index = st.slider("Select a frame from the `./data/frames` directory for Quickpose analysis", 0, len(frame_files)-1, 0, key="quickpose_slider")
selected_frame = frame_files[frame_index]
relative_path = os.path.relpath(selected_frame)

# Get frame filename for caching
frame_filename = os.path.basename(selected_frame)
cache_filename = f"./inferences/quickpose_{frame_filename.replace('.jpg', '.json')}"

# code snippet: the API call to the quickpose model with the selected image:
api_format = st.selectbox("Select API request format:", ["Python", "curl"], key="api_format_selector")

with st.expander("Show API Request Code", expanded=False):
    if api_format == "Python":
        st.code(f'''
import requests

api_key = "{masked_key}"  
image_path = "{relative_path}"  
measurements = "elbow_side,shoulder_extension,neck_lateral_flexion,neck_forward_flexion,hip_side,knee_side"
side = "both"

url = "https://api.quickpose.ai/jointtrack/v1/detect"
headers = {{
    "X-API-Key": api_key
}}

files = {{
    "image": open(image_path, "rb")
}}
data = {{
    "measurement": measurements,
    "side": side
}}

response = requests.post(url, headers=headers, files=files, data=data)

if response.status_code == 200:
    result = response.json()
    print("Pose analysis successful!")
else:
    print(f"Error: {{response.status_code}}, {{response.text}}")
''', language="python")
    else:  # curl format
        st.code(f'''
curl -X POST "https://api.quickpose.ai/jointtrack/v1/detect" \\
     -H "X-API-Key: {masked_key}" \\
     -H "Content-Type: multipart/form-data" \\
     -F 'image=@{relative_path}' \\
     -F 'measurement=elbow_side,shoulder_extension,neck_lateral_flexion,neck_forward_flexion,hip_side,knee_side' \\
     -F 'side=both'
''', language="bash")

# Function to perform Quickpose API call and cache results
def call_quickpose_api(image_path, cache_path, api_key):
    cached = False
    if os.path.exists(cache_path):
        with open(cache_path, 'r') as f:
            result = json.load(f)
        cached = True
    else:
        if api_key is None:
            return None, False
            
        measurements = "elbow_side,shoulder_extension,neck_lateral_flexion,neck_forward_flexion,hip_side,knee_side"
        side = "both"
        
        url = "https://api.quickpose.ai/jointtrack/v1/detect"
        headers = {
            "X-API-Key": api_key
        }
        
        files = {
            "image": open(image_path, "rb")
        }
        data = {
            "measurement": measurements,
            "side": side
        }
        
        response = requests.post(url, headers=headers, files=files, data=data)
        
        if response.status_code == 200:
            result = response.json()
            # Cache the result
            with open(cache_path, 'w') as f:
                json.dump(result, f)
        else:
            return None, False
    
    return result, cached

# Display in two columns
col1, col2 = st.columns(2)

with col1:
    st.write("**📥 Input Image**")
    st.image(selected_frame, caption=f"Path: `{relative_path}`", width=600)

with col2:
    st.write("**📤 Pose Analysis Output**")
    
    # Call the API and display results
    api_result, cached = call_quickpose_api(selected_frame, cache_filename, api_key)
    
    if api_result:
        status_msg = "🔄 Live API inference" if not cached else "💾 Cached inference"
        st.success(f"{status_msg}")
        
        # Display the result as a code block
        with st.expander("Show API Response JSON", expanded=False):
            st.code(json.dumps(api_result, indent=2), language="json")
        
        # You could also visualize the pose landmarks on the image here
        # This would require parsing the API response and drawing on the image
    else:
        st.error("API call failed or API key not provided")

st.write("### What is pose analysis?")
st.image("./assets/pitch/singapore-marksman-pose-analysis.png", caption="Singapore marksman using pose analysis", width=600)
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
st.image("./assets/pitch/canva-mockup.png", caption="Concept: Pose analysis technology applied to marksmanship training", width=600)

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
st.image("./assets/pitch/quickpose-sports-performance-pdp.png", caption="Quickpose: A high-level wrapper around MediaPipe Pose", width=600)

st.write("### Quickpose API Request")
st.write("""
    Quickpose provides a developer-friendly API that simplifies access to MediaPipe's advanced pose tracking capabilities. 
    It builds upon MediaPipe's powerful pose detection model while abstracting away complexity and adding 
    specialized measurements for joint angles and biomechanical analysis. This makes it ideal for applications 
    requiring precise human motion assessment without the need for extensive computer vision expertise. However, for
    our specialized use case, this precise expertise will be necessary for fine-tuning to production quality.
""")

st.write("### Pose analysis using Mediapipe")
st.write("""
    MediaPipe is Google's open-source framework for building multimodal applied machine learning pipelines. 
    As the underlying foundation for Quickpose, MediaPipe Pose provides more granular control and customization 
    options for developers with computer vision expertise.
""")
st.image("./assets/pitch/mediapipe-pose-github-tearsheet.png", caption="MediaPipe Pose: The underlying library for Quickpose. Can be used for directly fine-tuning custom pose analysis use cases.", width=600)

st.write("### Example MediaPipe API Implementation")
st.warning("This code is a work in progress and has not been tested. It is provided as a conceptual reference for direct MediaPipe integration.", icon="️🚧")

with st.expander("Show MediaPipe Example Code", expanded=False):
    st.code('''
import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
pose = mp_pose.Pose(
    static_image_mode=False,
    model_complexity=2,  # 0, 1, or 2 - higher is more accurate but slower
    smooth_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Process an image
def process_image(image_path):
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2RGB)
    
    # Process the image and extract pose landmarks
    results = pose.process(image_rgb)
    
    # Draw landmarks on the image
    annotated_image = image.copy()
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(
            annotated_image,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS
        )
        
        # Example: Calculate elbow angle
        # (Would customize this with proper marksmanship metrics)
        landmarks = results.pose_landmarks.landmark
        # Process landmarks for marksmanship analysis
        
    return annotated_image, results
''', language="python")

# Frame selector for MediaPipe
st.subheader("MediaPipe Frame Analysis")
frame_index = st.slider("Select a frame for MediaPipe analysis", 0, len(frame_files)-1, 0, key="mediapipe_slider")
selected_frame = frame_files[frame_index]
relative_path = os.path.relpath(selected_frame)

# Display in two columns
col1, col2 = st.columns(2)

with col1:
    st.write("**📥 Input Image**")
    st.image(selected_frame, caption=f"Path: `{relative_path}`", width=600)

with col2:
    st.write("**📤 Pose Analysis Output**")
    st.info("MediaPipe integration not implemented yet. This will show the processed image with pose landmarks when implemented.")

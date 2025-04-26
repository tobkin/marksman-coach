# marksman-coach

## Dev Environment Setup
1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

3. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Canva Mockup
[Canva Mockup Design](https://www.canva.com/design/DAGlwddIz1E/0pl_l_IyjJkSFSfd7dvlzg/edit)

## Context Data
- The rifle shooting process is detailed on page 5-2 of tc3-22-9.pdf.  
- Minute details of the shooting process are described on page 14 of army-marksmanship-unit-rifle.pdf.  
- [Improving handgun detection through a combination of visual features and body pose-based data](https://www.sciencedirect.com/science/article/pii/S0031320322007312)  
- Reference Githubs:
  - [Edunet_AI_internship_2025](https://github.com/itzdineshx/Edunet_AI_internship_2025?tab=readme-ov-file)

## Shot Process Overview

Based on the army rifle and carbine documents, the shot process consists of three distinct phases:

**Pre-shot phase**:
- Position
- Natural Point of Aim
- Sight Alignment/Sight Picture
- Hold

**Shot phase**:
- Refine Aim
- Breathing Control
- Trigger Control

**Post-shot phase**:
- Follow-through
- Recoil management
- Call the Shot
- Evaluate

This process forms a complete cycle for each shot taken. The functional elements that support this process include stability, aim, control, and movement – all of which work together to produce accurate and precise shots.

## Test Data
[youtube video links]

## Task List
When you start a task, add your name before it and move it to the In Progress section. When you complete a task, move it to the Done section.

### Todo

#### Pitch
- Talk track
- Dry run grading of talk track
- Slide deck (in the Streamlit app)
- Talk track final copyediting
- Practice pitching
- Contact & followup list

#### Frontend Engineering
- Header: Easy to read URL for the app, Prose, imagery, and soft elements to make it look Army
- Video player module with slider
- Print the pose ratings to the side of the video
- Footer: Team information -- LinkedIns, photos, etc
- UX Review with Kyra
- [Extra Credit] Encode the video with the pose ratings

#### Integration Engineering
- Integrate batch inference data with live application

#### MLOps
- [Toby] Stub data for live app
- Commit to repo and and trim the shooting video to 30 seconds
- [Ryan] Label 5 frames of the video in Canva
- [Toby] Model selection
- [Toby] Exploratory modeling
- [Toby] Fine tuning
- [Toby] Batch inference

#### DevOps
- [Toby] DNS configuration for app
- [Toby] Host the app on cloud
- [If we have problems] Dev containerization

### In Progress

#### Pitch
- No tasks currently in progress

#### Frontend Engineering
- [Toby] Hello World Steamlit App

#### Integration Engineering
- No tasks currently in progress

#### MLOps
- No tasks currently in progress

#### DevOps
- No tasks currently in progress

### Done

#### Pitch
- No tasks completed yet

#### Frontend Engineering
- [All]: UI mockup in Canva

#### Integration Engineering
- No tasks completed yet

#### MLOps
- Gather official marksmanship procedural guides
- Gather test video screenshots for UI mockup

#### DevOps
- No tasks completed yet
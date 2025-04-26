## Repo Map
```
.
├── assets
│   ├── banner.png
│   └── shooting-video.mov
├── data
│   ├── example-pose-predictions
│   ├── multi-subject
│   └── single-subject
├── project-mgmt
│   ├── 1-todo.md
│   ├── 2-in-progress.md
│   └── 3-done.md
├── LICENSE
├── README.md
├── app.py
├── army-marksmanship-unit-rifle.pdf
├── army-rifle-and-carbine.pdf
├── requirements.txt
└── shooting-video.mov
```

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
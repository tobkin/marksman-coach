# Prompt: Marksmanship Analysis Stub Dataset

## Quantitative Variables
- **Total frames**: 900
- **Sample size**: 900 rows
- **Frame increment**: Total Frames / Sample Size
- **Phase distribution**:
  - Position: Fast progression (10% of frames)
  - Natural Point of Aim: Moderate speed (15% of frames)
  - Sight Alignment/Sight Picture: Moderate speed (15% of frames)
  - Hold: Slow progression (20% of frames)
  - Refine Aim: Slow progression (20% of frames)
  - Breathing Control: Slow progression (15% of frames)
  - Trigger Control: Fast progression (5% of frames)

## Background
I need sample CSV data for a frontend application that analyzes marksmanship technique. The input dataset consists of approximately 900 frames from a side-view video of a marksman.

## CSV Structure
- **Columns**: videoPath, frame, shotPhase, head_position, rifle_butt_placement, non_firing_hand_position, elbow_placement, natural_point_of_aim, balance, relaxation
- **Assessment values**: "good" or "bad" (lowercase)
- **Video path**: "./assets/shooting-video.mov"

## Shot Phases (in chronological order)
### Pre-shot phase:
- Position
- Natural Point of Aim
- Sight Alignment/Sight Picture
- Hold

### Shot phase:
- Refine Aim
- Breathing Control
- Trigger Control

## Requirements
- Include all shot phases in chronological order
- Timing pattern: The marksman will quickly advance through the position phase, slow down on hold, refine aim, and breathing control, then go quickly through trigger control
- Include a mix of "good" and "bad" assessments for different technique elements
- Assessment transitions should reflect realistic physical movement progression (not random changes)
- Technique elements should show logical improvement or degradation patterns as the marksman adjusts position and technique
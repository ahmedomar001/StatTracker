# StatTracker: Shot Detection Using Pose Estimation

This project uses MediaPipe's human pose estimation to automatically detect and visualize shot attempts from basketball videos — including NBA 2K gameplay and real NBA highlight reels. By analyzing body landmarks such as the wrists and shoulders, the system estimates when a player raises their arms for a shot, and plots the detected shot locations on a basketball court.

## How It Works

1. **Frame Extraction**  
   Extracts frames from a basketball video (e.g., `NBA_Gameplay.mp4` or highlight clips).

2. **Pose Estimation**  
   Uses MediaPipe Pose to detect 33 body landmarks (e.g., wrist, shoulder, chest) per frame.

3. **Shot Detection Logic**  
   A shot is detected if:
   - Either wrist is raised above the corresponding shoulder.
   - The detection isn't too close to a previous one (avoids duplicate counting).
   - Chest position is saved as the shot coordinate.

4. **Visualization**  
   Shot attempts are plotted on a normalized scatter plot using `matplotlib`.

## Why Pose Estimation?

Traditional stat tracking requires manual annotation or ball tracking. Instead, this project shows that player body movement alone can be a strong signal for detecting basketball actions like shooting.

## File Structure
StatTracker/

├── videos/

│ └── * Your inputed video here.mp4

├── frames/

│ └── frame_*.jpg

├── output/

│ └── shot_scatter_plot.png

├── pose_estimations.py

└── README.md

## Requirements

Make sure the following Python packages are installed:
- pip install mediapipe opencv-python matplotlib numpy

- 
## How to Run
- python pose_estimations.py

  
- This will:
  - Extract frames from `videos/Your video here.mp4`
  - Run pose estimation and detect shots
  - Save the scatter plot to `output/shot_scatter_plot.png`


## Future Work

- Improve accuracy by:
  - Requiring both wrists raised
  - Tracking vertical movement or jump height
  - Adding ball tracking
- Extend to other basketball stats (e.g., blocks, passes, rebounds)
- Adapt to other sports using similar pose-based logic

## Author

Ahmed Omar  
GitHub: https://github.com/ahmedomar001

## License

This project is for educational purposes under CSE 4310 at UTA.



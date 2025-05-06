#  NBA Gameplay Shot Detection and Visualization Script

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import mediapipe as mp

# Step 1: Extract frames from NBA gameplay recording 
def extract_frames(video_path="videos/NBA_2K_Gameplay.mp4", output_folder="frames", frame_rate=1):
    os.makedirs(output_folder, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if count % (fps // frame_rate) == 0:
            filename = os.path.join(output_folder, f"frame_{count}.jpg")
            cv2.imwrite(filename, frame)
        count += 1

    cap.release()
    print(" Frames extracted!")

# Step 2: Run pose estimation and detect shot attempts 
def detect_shots_from_frames(frame_folder="frames"):
    pose = mp.solutions.pose.Pose(static_image_mode=True)

    LEFT_WRIST, RIGHT_WRIST = 15, 16
    LEFT_SHOULDER, RIGHT_SHOULDER = 11, 12
    CHEST = 0  # approximate shot position

    shot_coords = []

    for filename in sorted(os.listdir(frame_folder)):
        if not filename.endswith(".jpg"):
            continue
        path = os.path.join(frame_folder, filename)
        image = cv2.imread(path)
        result = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        if result.pose_landmarks:
            lm = result.pose_landmarks.landmark
            lw_up = lm[LEFT_WRIST].y < lm[LEFT_SHOULDER].y
            rw_up = lm[RIGHT_WRIST].y < lm[RIGHT_SHOULDER].y
            if lw_up or rw_up:
                shot_coords.append((lm[CHEST].x, lm[CHEST].y))

    print(f" {len(shot_coords)} shot attempts detected!")
    return shot_coords

# Step 3: Visualize shots on court 
def visualize_shots(shot_coords):
    if not shot_coords:
        print("No shots to visualize.")
        return

    x, y = zip(*shot_coords)
    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, c='red', s=100, label="Shot Attempts")
    plt.title("Detected Shot Attempts")
    plt.xlabel("Court Width (normalized)")
    plt.ylabel("Court Length (normalized)")
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.gca().invert_yaxis()
    plt.legend()
    plt.grid(True)
    plt.savefig("output/shot_scatter_plot.png")
    plt.show()

# Main Program 
if __name__ == "__main__":
    extract_frames(video_path="videos/Lakers-wolves.mp4")
    shot_coords = detect_shots_from_frames()
    visualize_shots(shot_coords)

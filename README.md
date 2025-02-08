Hand Tracking with OpenCV and MediaPipe

Overview

This project utilizes OpenCV and MediaPipe to track and visualize hand movements in real-time using a webcam. The system detects hands, identifies key landmarks, and specifically highlights the index finger tip.

Features

Real-time hand detection and tracking

Draws hand landmarks and connections

Highlights the index finger tip with a green circle

Displays live tracking in an OpenCV window

Press 'q' to exit

Requirements

Ensure you have the following installed:

Python 3.x

OpenCV

MediaPipe

Install dependencies using:

pip install opencv-python mediapipe

Usage

Run the script:

python hand_tracking.py

How It Works

Captures video from the webcam.

Converts frames to RGB and processes them using MediaPipe.

Detects hands and draws landmarks.

Extracts the index finger tip coordinates.

Highlights the index finger tip with a green circle.

Displays the video with tracking overlay.

Example Output

The script will print index finger tip coordinates:

Index Finger Tip: 320, 240
Index Finger Tip: 330, 250

Controls

Press 'q' to exit the program.

Future Improvements

Gesture recognition

Virtual mouse control using hand gestures

Multi-hand tracking with advanced interactions

Acknowledgments

Built using MediaPipe and OpenCV.

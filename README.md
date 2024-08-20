# Hand-Tracking Model with OOP Architecture

## Overview

This project implements a hand-tracking model using OpenCV and a pre-trained machine learning model for hand landmark detection. The project is designed with Object-Oriented Programming (OOP) principles to ensure clean, modular, and reusable code. 

## Project Structure

The main functionality of the hand-tracking model is divided into different classes and methods, each responsible for a specific part of the process:

- **HandDetector**: A class responsible for detecting hands in a video stream using a pre-trained model.
- **HandLandmarks**: A class that identifies and processes the landmarks of detected hands.
- **HandTrackingApp**: The main application class that integrates the hand detection and landmark processing, handles the video feed, and displays the output.

## Key Components

### 1. HandDetector Class

This class encapsulates the logic for initializing the hand detection model, processing frames, and returning detected hand regions.

```python
class HandDetector:
    def __init__(self, model_path):
        # Load the pre-trained model for hand detection
        pass

    def detect_hands(self, frame):
        # Process the frame to detect hands
        return hand_regions
```
### 2. HandLandmarks Class

This class processes the detected hand regions to identify and mark the landmarks.
```python
class HandLandmarks:
    def __init__(self, model):
        # Initialize with the hand detection model
        pass

    def find_landmarks(self, hand_region):
        # Process the hand region to find landmarks
        return landmarks

```
### 3. HandTrackingApp Class

This class is the main controller of the application, integrating hand detection and landmark processing. It handles the video input, runs detection, and displays the results


``` python
class HandTrackingApp:
    def __init__(self, video_source=0):
        # Initialize the video capture and detection components
        pass

    def run(self):
        # Main loop to capture video, process frames, and display results
        pass



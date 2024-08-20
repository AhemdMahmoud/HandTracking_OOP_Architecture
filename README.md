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

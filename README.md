# Face Recognition System

![Python](https://img.shields.io/badge/Python-3.8+-3776AB.svg?style=flat-square&logo=python)
![Firebase](https://img.shields.io/badge/Firebase-FFCA28.svg?style=flat-square&logo=firebase)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8.svg?style=flat-square&logo=opencv)
![License](https://img.shields.io/badge/License-MIT-4CAF50.svg?style=flat-square)

<p align="center">
  <strong>A cutting-edge facial recognition solution for automated attendance tracking and identity verification across multiple sectors.</strong>
</p>

---

## Overview

The **Face Recognition System** is an advanced computer vision application designed to automate identity verification and attendance tracking, with applications in education, law enforcement, healthcare, and forensic science. Developed as a senior project at Düzce University’s Computer Engineering Department, the system leverages real-time facial recognition to enhance efficiency, accuracy, and security. The implemented prototype focuses on an automated attendance system for educational institutions, using a webcam to identify students, mark their attendance, and store data in Firebase Realtime Database. Its modular design supports expansion to critical use cases such as criminal detection, patient identification, and forensic analysis.

The system combines a user-friendly graphical interface, robust face recognition algorithms, and cloud-based data management to provide a scalable solution for identity-related challenges.

---

## Features

### Main Application
- **Real-Time Face Recognition**:
  - Detects and identifies faces instantly using `face_recognition` and dlib.
  - Matches live face encodings against pre-stored encodings for accurate identification.
- **Graphical User Interface**:
  - Displays live webcam feed with bounding boxes around recognized faces.
  - Shows mode indicators (Active, Marked, Already Marked, No Match) using dynamic images.
  - Presents student details (e.g., name, ID, major, attendance count) upon recognition.
- **Automated Attendance Tracking**:
  - Marks attendance for recognized students, preventing duplicates within 30 seconds.
  - Updates Firebase with attendance counts and timestamps.
- **Efficient Processing**:
  - Resizes video frames for faster recognition.
  - Uses pre-computed encodings for quick matching.

### Encoding Generator
- **Face Encoding**:
  - Processes student images to generate unique face encodings.
  - Saves encodings and IDs to `EncodeFile.p` for use in the main application.
- **Batch Processing**: Handles multiple images in the `Images` folder.

### Firebase Integration
- **Student Profiles**:
  - Stores data (e.g., name, T.C, nationality, attendance) in Firebase Realtime Database.
  - Supports dynamic updates and retrieval.
- **Attendance Management**:
  - Increments `total_attendance` and updates `last_attendance_time` for recognized students.
- **Cloud Storage**:
  - Uploads student images to Firebase Storage (implemented in the encoding generator).

### Versatility
- Designed for broader applications in law enforcement (criminal detection), healthcare (patient identification), and forensics (identity verification).
- Extensible for new users and scenarios through image and database updates.

---

## Architecture

The system integrates multiple components:
- **Main Application (`main.py`)**: Captures video, performs face recognition, and updates the GUI and Firebase.
- **Encoding Generator (`encode_generator.py`)**: Prepares face encodings from student images.
- **Firebase Initialization Scripts (`add_data_to_firebase_*.py`)**: Populate student profiles in Firebase.
- **Firebase Realtime Database**:
  - Structure: `Students/{student_id}` with fields like `name`, `T.C`, `nationality`, `total_attendance`, `last_attendance_time`.
- **Resources**:
  - `Resources/background.png`: GUI background.
  - `Resources/Modes/*.png`: Mode images (e.g., Active, Marked).
  - `Images/*.png`: Student images for encoding.
  - `EncodeFile.p`: Face encodings and IDs.
  - `serviceAccountKey.json`: Firebase credentials.

<p align="center">
  <img src="screenshots/architecture-diagram.png" alt="System Architecture" width="600"/>
</p>

---

## Prerequisites

### Hardware
- **Webcam**: For capturing live video (minimum resolution: 640x480).

### Software
- **Python**: 3.8 or higher
- **Dependencies**:
  ```bash
  opencv-python face_recognition cvzone numpy pickle firebase_admin

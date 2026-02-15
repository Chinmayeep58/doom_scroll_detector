# Doom Scroll Detector (Head Tilt Based)

A simple OpenCV + MediaPipe desktop app that detects when a user keeps their head tilted down for a sustained time (a common posture while using a phone) and triggers an on-screen warning with a buzzer sound.

## 🚀 Features

* Real-time webcam face detection
* Head tilt detection using facial landmarks
* Timer-based “doom scrolling” detection
* Visual alert on screen
* Audible buzzer warning

## 🛠 Tech Stack

* Python
* OpenCV
* MediaPipe Tasks API
* Playsound

## 📂 Project Structure

```
doom_scrolling/
│
├── main.py
├── face_landmarker.task
├── buzzer.mp3
└── README.md
```

## 📦 Installation

Install dependencies:

```bash
pip install opencv-python mediapipe playsound==1.2.2
```

Download the face landmark model and place it in the project folder:

```
face_landmarker.task
```

## ▶️ Run the App

```bash
python main.py
```

Press **Q** to exit.

## ⚙️ How It Works

1. Webcam captures your face.
2. MediaPipe detects facial landmarks.
3. Compares nose position vs eye position.
4. If head is tilted down for a few seconds:

   * Timer starts
   * Warning text appears
   * Buzzer sound plays

## 🔧 Adjustable Settings (in `main.py`)

* `head_down_threshold` → sensitivity of tilt detection
* `doom_threshold` → seconds before alert triggers

## 📌 Notes

* Best results when seated in front of the laptop.
* Works without phone detection (posture-based).
* Designed as a simple MVP for productivity awareness.

## 🌱 Future Improvements

* Phone object detection
* Productivity stats dashboard
* Background tray app
* Auto pause during meetings

# Emotion Analysis System

A real-time facial emotion detection system using computer vision and deep learning. This project captures video from a webcam, analyzes facial expressions, and provides audio feedback about detected emotions.

## Features

- **Real-time Emotion Detection**: Analyzes facial expressions using DeepFace library  
- **Text-to-Speech Feedback**: Announces detected emotions using pyttsx3  
- **Multi-threaded Architecture**: Separates emotion analysis from speech output for better performance  
- **Headless Environment Support**: Works in environments without GUI (Codespaces, servers)  
- **Error Handling**: Robust fallback mechanisms for missing dependencies  

## Technologies Used

- **OpenCV (opencv-python-headless)**: Computer vision and video capture  
- **DeepFace**: Deep learning-based facial emotion recognition  
- **TensorFlow 2.20.0**: Machine learning framework  
- **tf-keras**: Keras API for TensorFlow  
- **pyttsx3**: Text-to-speech conversion  
- **Python 3.12**: Programming language  

## Installation

### Prerequisites

- Python 3.8 or higher  
- Webcam (for real-time detection)  
- For Linux/Ubuntu systems: espeak package  

### Clone the Repository

```bash
git clone https://github.com/MANOHARPOTLURU/Emotion_Analysis.git
cd Emotion_Analysis
```

### Install Python Dependencies

```bash
pip install opencv-python-headless deepface tf-keras pyttsx3
```

### Install System Dependencies (Linux/Ubuntu)

```bash
sudo apt-get update
sudo apt-get install -y espeak
```

## Usage

```bash
python Emotion_Analysis.py
```

### Controls

- **Press 'q'**: Quit the application  
- The system will automatically detect faces and analyze emotions  
- Detected emotions will be announced via text-to-speech (if available)  

## How It Works

1. **Video Capture**: Captures frames from the default webcam  
2. **Face Detection**: Detects faces in each frame using OpenCV  
3. **Emotion Analysis**: Uses DeepFace to analyze the dominant emotion  
4. **Speech Output**: Announces the detected emotion using a separate thread  
5. **Visual Feedback**: Displays the video feed with emotion labels  

## Detected Emotions

- Happy  
- Sad  
- Angry  
- Fear  
- Surprise  
- Disgust  
- Neutral  

## Troubleshooting

### libGL.so.1 error
```bash
pip uninstall opencv-python -y
pip install opencv-python-headless
```

### tf_keras not found
```bash
pip install tf-keras
```

### espeak not installed
```bash
sudo apt-get install -y espeak
```

## Author

**Manohar Potluru**  
GitHub: [@MANOHARPOTLURU](https://github.com/MANOHARPOTLURU)

## Project Status

✅ All dependencies resolved and tested  
✅ Runs successfully in headless environments (GitHub Codespaces)  
✅ Error handling implemented for all critical components  

**Last Updated**: November 21, 2025

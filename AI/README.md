# AI Track

[Back to Main Page](../README.md)

## Overview

This page documents the tasks, progress, and learning outcomes related to the AI track of the robotics summer training program.

The AI track focuses on artificial intelligence, machine learning, computer vision, image recognition, OpenCV, speech processing, Large Language Models, and practical AI applications.

## Tasks

| Task No. | Task Name | Date | Status | Documentation |
|---|---|---|---|---|
| 1 | Image Recognition Model Using Teachable Machine | 2026-07-11 | Completed | [View Task](./Task-1-Image-Recognition) |
| 2 | OpenCV Computer Vision Projects | 2026-07-27 | In Progress | [View Task](./Task-2-OpenCV) |
| 3 | Voice-to-Voice AI Assistant | 2026-07-29 | Completed | [View Task](./Task-3-Voice-to-Voice-AI-Assistant) |

## Task Summary

### Task 1: Image Recognition Model Using Teachable Machine

This task focused on training an image recognition model using Google Teachable Machine.

The model was trained using three classes:

- Screwdriver
- Wrench
- Pliers

After training and testing, the model was exported in TensorFlow/Keras format and used in a Python script to predict the class of an input image.

[Open Task 1 Documentation](./Task-1-Image-Recognition)

### Task 2: OpenCV Computer Vision Projects

This task focuses on using OpenCV to complete different computer vision subtasks.

The first completed subtask is Color Recognition Using OpenCV. The program reads an image, converts it to HSV color space, detects selected colors, creates a mask, and draws a rectangle around the detected color.

The remaining OpenCV subtasks will be completed later.

[Open Task 2 Documentation](./Task-2-OpenCV)

### Task 3: Voice-to-Voice AI Assistant

This task focused on building a complete AI assistant that receives spoken input and responds using generated speech.

The task was divided into three independent subtasks:

- Speech-to-Text using OpenAI Whisper
- LLM Processing using Cohere
- Text-to-Speech using pyttsx3 and Windows SAPI5

Each component was developed and tested independently before being integrated into the final Voice-to-Voice AI Assistant.

The completed workflow is:

```text
Voice Input
     ↓
Speech-to-Text
     ↓
Recognized Transcript
     ↓
Cohere LLM
     ↓
Generated AI Response
     ↓
Text-to-Speech
     ↓
Spoken AI Response
```

The final application records a spoken question, transcribes it using Whisper, sends the transcript to Cohere, generates an AI response, converts the response into a WAV audio file, and plays the spoken answer.

[Open Task 3 Documentation](./Task-3-Voice-to-Voice-AI-Assistant)

## Task 2 Subtasks

| Subtask No. | Subtask Name | Status | Documentation |
|---|---|---|---|
| 1 | Color Recognition Using OpenCV | Completed | [View Subtask](./Task-2-OpenCV/Subtask-1-Color-Recognition) |
| 2 | Face Recognition | Planned | To be added later |
| 3 | Object Tracking | Planned | To be added later |
| 4 | Object Recognition | Planned | To be added later |
| 5 | Line Tracking | Planned | To be added later |
| 6 | Tag Recognition | Planned | To be added later |
| 7 | Object Classification | Planned | To be added later |

## Task 3 Components

| Component No. | Component Name | Status | Documentation |
|---|---|---|---|
| 1 | Speech-to-Text | Completed | [View Subtask](./Task-3-Voice-to-Voice-AI-Assistant/Subtask-1-Speech-to-Text) |
| 2 | LLM Processing | Completed | [View Subtask](./Task-3-Voice-to-Voice-AI-Assistant/Subtask-2-LLM-Processing) |
| 3 | Text-to-Speech | Completed | [View Subtask](./Task-3-Voice-to-Voice-AI-Assistant/Subtask-3-Text-to-Speech) |
| 4 | Final Voice-to-Voice AI Assistant | Completed | [View Final Project](./Task-3-Voice-to-Voice-AI-Assistant/Final-Voice-Assistant) |

## Tools and Topics

- Artificial Intelligence
- Machine Learning
- Image Recognition
- Computer Vision
- OpenCV
- Python
- NumPy
- TensorFlow/Keras
- Google Teachable Machine
- Dataset collection
- Model training
- Model testing
- Image processing
- HSV color space
- Speech-to-Text
- OpenAI Whisper
- Audio recording
- Audio processing
- Language detection
- Large Language Models
- Cohere Chat API
- API integration
- Environment variables
- API-key security
- Text-to-Speech
- pyttsx3
- Windows SAPI5
- SoundDevice
- SciPy
- FFmpeg
- PyTorch
- WAV audio files
- Modular Python architecture
- Error handling
- System integration
- GitHub documentation

## Notes

- Each AI task has its own folder and README page.
- The main AI page is used as an index and summary page.
- Detailed documentation, source code, screenshots, and outputs are stored inside each task folder.
- Task 2 is organized into subtasks to keep each OpenCV topic separated and clear.
- Task 3 is organized into three independent subtasks and one final integration project.
- Each Task 3 component was developed and tested independently before the complete system was assembled.
- Private API credentials are stored locally using environment variables and are excluded from GitHub.
- The HuskyLens task will be completed later when the component arrives.

## Reflection

The AI track helped me apply artificial intelligence concepts through practical projects involving image classification, computer vision, speech recognition, Large Language Models, and speech generation.

Task 1 introduced me to image classification and model training using Google Teachable Machine. I learned how to collect and organize a dataset, train a model using multiple classes, export it in TensorFlow/Keras format, and use the trained model inside a Python application.

Task 2 introduced me to OpenCV and basic image processing. Through the Color Recognition subtask, I learned how to read images, convert them from BGR to HSV color space, create color masks, detect selected colors, and draw bounding boxes around detected regions.

Task 3 introduced me to the complete process of building and integrating an AI pipeline. I learned how to record microphone audio, use OpenAI Whisper for speech recognition, detect spoken languages, connect a Python application to the Cohere Chat API, secure an API key using environment variables, generate AI responses, convert text into speech, create WAV audio files, and play spoken responses.

The most important lesson from Task 3 was the value of modular software architecture. Instead of placing the entire system inside one large Python file, I separated configuration, recording, transcription, LLM communication, Text-to-Speech processing, terminal utilities, and application control into independent modules.

Developing each component separately before integration made the final application easier to test, understand, maintain, and improve. These tasks helped me understand how individual AI technologies can be combined to build practical and interactive systems.

# Subtask 1 - Color Recognition Using OpenCV

[Back to Task 2 - OpenCV](../README.md)

## Overview

This subtask focused on using OpenCV to recognize colors in an image.

The program reads an input image, converts it to HSV color space, creates a color mask, detects colored areas, and draws a rectangle around the detected color.

This subtask was completed using an image file instead of a webcam because a webcam was not available at the time.

## Objective

The objective of this subtask was to practice basic computer vision using OpenCV by detecting colors from an image.

The program was designed to detect common colors such as:

- Red
- Green
- Blue
- Yellow

## Tools and Technologies Used

- Python
- OpenCV
- NumPy
- Visual Studio Code
- Image processing
- GitHub documentation

## Project Idea

The idea of this project is to recognize specific colors inside an image.

The program uses HSV color ranges to isolate selected colors from the original image. After detecting the color, it creates a mask and draws a bounding box around the detected area.

## How It Works

The program follows these steps:

1. Read the input image.
2. Resize the image if it is too large.
3. Convert the image from BGR to HSV color space.
4. Define HSV ranges for selected colors.
5. Create a color mask.
6. Remove small noise from the mask.
7. Find contours of the detected colored areas.
8. Draw a rectangle around the detected color.
9. Add the detected color name on the image.
10. Save the mask and final result images.

## Project Files

The subtask contains:

```text
Subtask-1-Color-Recognition/
├── README.md
├── files/
│   ├── original-image.jpg
│   ├── color-mask.png
│   ├── final-result.png
│   └── vscode-output.png
└── source-code/
    ├── color_recognition.py
    └── requirements.txt

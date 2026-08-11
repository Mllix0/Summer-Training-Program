# Mechanical Task 6 – Three Movement

[Back to Mechanical Track](../README.md)

## Overview

This task focused on programming the physical robotic dog to perform three different movements using four servo motors controlled by an Arduino Uno.

Each movement was programmed and tested separately to make it easier to adjust the servo positions, movement angles, timing, and overall robot behavior.

The three completed movements are:

1. Forward
2. Waving
3. Dance

## Hardware and Software

### Hardware

- Arduino Uno
- 4 Servo Motors
- Robotic Dog Structure
- External 5V Power Supply
- Jumper Wires
- USB Cable

### Software

- Visual Studio Code
- PlatformIO
- Arduino Framework
- Arduino Servo Library

## Wiring

Four servo motors were connected to the Arduino Uno to control the four legs of the robotic dog.

### Servo Connections

| Servo | Signal Pin | Power | Ground |
|---|---|---|---|
| Front Left | D3 | External 5V | GND |
| Front Right | D4 | External 5V | GND |
| Rear Left | D6 | External 5V | GND |
| Rear Right | D7 | External 5V | GND |

### Wiring Layout

```text
Arduino Uno
│
├── D3 ───── Front Left Servo Signal
├── D4 ───── Front Right Servo Signal
├── D6 ───── Rear Left Servo Signal
├── D7 ───── Rear Right Servo Signal
│
└── GND ──── External Power Supply GND


External 5V Power Supply
│
├── +5V ──── Front Left Servo VCC
├── +5V ──── Front Right Servo VCC
├── +5V ──── Rear Left Servo VCC
├── +5V ──── Rear Right Servo VCC
│
└── GND ──── All Servo GND Wires
             │
             └── Arduino GND
```

> **Important:** The four servo motors were powered using an external regulated 5V supply instead of powering all four directly from the Arduino 5V pin. The Arduino and external power supply share a common ground.

## Servo Calibration

Before programming the movements, the four servo motors were calibrated to find suitable neutral positions for the robot legs.

The final neutral positions were:

| Servo | Neutral Position |
|---|---:|
| Front Left | 90° |
| Front Right | 95° |
| Rear Left | 95° |
| Rear Right | 95° |

These positions were adjusted experimentally until the robot legs were aligned correctly for movement testing.

## Movement 1 – Forward

The first movement programmed was the forward movement.

The movement uses alternating diagonal pairs of legs. The front-left and rear-right legs move as one pair, while the front-right and rear-left legs move as the second pair.

The sequence is repeated several times to produce forward motion.

### Forward Movement Settings

- Movement amount: ±20°
- Movement delay: 350 ms
- Repetitions: 12

### Code

[View `forward.cpp`](./files/code/forward.cpp)

### Forward Movement Video

https://github.com/user-attachments/assets/b1a6fcc6-c7c4-42e5-bac5-b0612af8a4b5

## Movement 2 – Waving

The second movement programmed was a waving motion.

The **front-right leg** is used for the wave while the other three legs remain close to their neutral positions.

The front-right servo repeatedly moves between two angles to create the waving motion.

### Waving Settings

- Waving leg: Front Right
- Neutral position: 95°
- First wave position: 70°
- Second wave position: 120°
- Repetitions: 5
- Delay between positions: 300 ms

### Code

[View `waving.cpp`](./files/code/waving.cpp)

### Waving Movement Video

https://github.com/user-attachments/assets/f83f3399-bcd2-40d4-88b0-bf1e8e881018

## Movement 3 – Dance

The third movement programmed was a dance motion.

All four legs participate in the movement.

The front legs move through a larger angle, while the rear legs move through a smaller angle. This creates an alternating movement while keeping the rear section of the robot more stable.

During testing, the rear-leg movement was reduced until a smoother motion was achieved.

### Dance Settings

- Front legs movement: ±20°
- Rear legs movement: ±5°
- Dance delay: 300 ms
- Repetitions: 6

### Code

[View `dance.cpp`](./files/code/dance.cpp)

### Dance Movement Video

https://github.com/user-attachments/assets/40cf0b1f-7e6c-4aee-96e4-4aac63909692

## Project Files

```text
Task-6-Three-Movement/
├── README.md
└── files/
    ├── code/
    │   ├── forward.cpp
    │   ├── waving.cpp
    │   └── dance.cpp
    └── media/
        ├── forward.mp4
        ├── waving.mp4
        └── dance.mp4
```

## Result

The robotic dog was successfully programmed to perform three separate movements:

- Forward movement
- Waving using the front-right leg
- Dance movement using all four legs

Each movement was programmed, tested, and adjusted separately.

The servo neutral positions and movement angles were calibrated experimentally to achieve suitable physical movement for the robotic dog.

The final code for each movement is stored separately inside the project files, together with its corresponding demonstration video.

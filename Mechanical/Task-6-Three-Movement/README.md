# Mechanical Task 6 – Three Movement

[Back to Mechanical Track](../README.md)

## Overview

This task focused on programming the physical robotic dog to perform three different movements using four servo motors controlled by an Arduino.

Each movement was programmed and tested separately to make it easier to adjust the servo positions, movement angles, and timing.

The three completed movements are:

1. Forward
2. Waving
3. Dance

## Hardware and Software

- Arduino Uno
- 4 Servo Motors
- Robotic Dog Structure
- Visual Studio Code
- PlatformIO
- Arduino Servo Library

## Servo Configuration

The four servo motors were connected to the Arduino using the following pins:

| Servo | Arduino Pin | Neutral Position |
|---|---:|---:|
| Front Left | D3 | 90° |
| Front Right | D4 | 95° |
| Rear Left | D6 | 95° |
| Rear Right | D7 | 95° |

These neutral positions were adjusted experimentally so that the robot could maintain a suitable resting position before performing the movements.

---

## Movement 1 – Forward

The forward movement uses alternating diagonal pairs of legs.

The robot repeatedly changes the positions of the front-left/rear-right pair and the front-right/rear-left pair to create forward motion.

### Code

[View `forward.cpp`](./files/code/forward.cpp)

### Forward Movement Video

[Watch Forward Movement](./files/media/forward.mp4)

---

## Movement 2 – Waving

The waving movement uses the **front-right leg**.

The other three legs remain close to their neutral positions while the front-right servo repeatedly moves between two angles to create a waving motion.

### Code

[View `waving.cpp`](./files/code/waving.cpp)

### Waving Movement Video

[Watch Waving Movement](./files/media/waving.mp4)

---

## Movement 3 – Dance

The dance movement uses all four legs.

The front legs move through a larger angle while the rear legs move through a smaller angle to create a controlled alternating dance motion.

The final movement angles used were:

- Front legs: ±20°
- Rear legs: ±5°

### Code

[View `dance.cpp`](./files/code/dance.cpp)

### Dance Movement Video

[Watch Dance Movement](./files/media/dance.mp4)

---

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

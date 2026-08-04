# Electrical Track

[Back to Main Page](../README.md)

## Overview

This page documents the tasks, progress, and learning outcomes related to the Electrical track of the robotics summer training program.

The Electrical track focuses on circuits, sensors, motors, microcontrollers, wiring, simulations, wireless control, and electronic components used in robotics systems.

Each task has its own folder and README file containing the circuit explanation, code, media, demonstrations, results, challenges, and learning outcomes.

## Tasks

| Task No. | Task Name | Date | Status | Documentation |
|---|---|---|---|---|
| 1 | Four Servo Motors Control Using Tinkercad | 2026-07-14 | Completed | [View Task](./Task-1-Servo-Motors) |
| 2 | Arduino Motor and Sensor Control | 2026-07-27 | Completed | [View Task](./Task-2-DC-Motor-Control-and-Obstacle-Avoidance) |
| 3 | ESP32 Web-Controlled Servo Motor | 2026-08-05 | Completed | [View Task](./Task-3-ESP32-Web-Controlled-Servo) |

## Task Summary

### Task 1: Four Servo Motors Control Using Tinkercad

This task focused on programming four servo motors in Tinkercad using Arduino.

The motors were programmed to perform a sweep motion for two seconds. After the movement sequence finished, all four motors stopped and held their positions at 90 degrees.

The circuit was built using:

- Arduino Uno
- Breadboard
- Four micro servo motors
- Jumper wires
- Tinkercad Circuits

This task introduced multi-servo control, Arduino timing, circuit wiring, and simulated testing.

[Open Task 1 Documentation](./Task-1-Servo-Motors)

---

### Task 2: Arduino Motor and Sensor Control

Task 2 explored Arduino-based motor, sensor, and actuator control through two related subtasks.

The first subtask was completed as a Tinkercad simulation involving DC motor control and obstacle avoidance. The second subtask was completed as a physical Arduino project in which an ultrasonic sensor controls a servo motor based on object distance.

#### Subtask 1: DC Motor Control and Obstacle-Avoidance Simulation

The first subtask focused on controlling four DC motors using an Arduino Uno and two L293D motor-driver ICs.

The simulated circuit included:

- Arduino Uno
- Two L293D motor drivers
- Four DC motors
- HC-SR04 ultrasonic sensor
- Servo motor
- Tinkercad Circuits

The motors followed the required movement sequence:

1. Move forward.
2. Move backward.
3. Turn right and left alternately.
4. Stop.

When an obstacle was detected at a distance of 10 cm or less, the motors stopped and the servo moved left and right to simulate directional scanning.

[Open Subtask 1 Documentation](./Task-2-DC-Motor-Control-and-Obstacle-Avoidance/Subtask-1-Tinkercad-Simulation)

#### Subtask 2: Hands-On Ultrasonic Servo Control

The second subtask focused on building a physical Arduino system using an HC-SR04 ultrasonic sensor and an SG90 servo motor.

The system operates as follows:

1. The servo remains at `0°` while the area is clear.
2. When an object reaches `10 cm` or closer, the LED turns on and the servo moves to `90°`.
3. The servo remains at `90°` while the object is nearby.
4. When the object moves beyond `12 cm`, the LED turns on while the servo returns to `0°`.

The separate activation and return distances help prevent unstable movement near the detection threshold.

| Setting | Final Value |
|---|---:|
| Original servo angle | 0° |
| Activated servo angle | 90° |
| Activation distance | 10 cm |
| Return distance | 12 cm |

The project was developed using Visual Studio Code and PlatformIO.

[Open Subtask 2 Documentation](./Task-2-DC-Motor-Control-and-Obstacle-Avoidance/Subtask-2-Hands-On-Servo-Control)

[Open Complete Task 2 Documentation](./Task-2-DC-Motor-Control-and-Obstacle-Avoidance)

---

### Task 3: ESP32 Web-Controlled Servo Motor

This task focused on using an ESP32 to create its own Wi-Fi Access Point and host a local webpage for controlling a servo motor.

The webpage includes two buttons:

- **OPEN**
- **CLOSE**

The system operates as follows:

- Pressing **OPEN** moves the servo to `90°`, turns on the green LED, and turns off the red LED.
- Pressing **CLOSE** moves the servo to `0°`, turns on the red LED, and turns off the green LED.

The project used:

- 38-pin ESP32 development board
- Servo motor
- Green LED
- Red LED
- Two 220 Ω resistors
- Breadboard
- Jumper wires
- Visual Studio Code
- PlatformIO
- Wokwi

The circuit and component behavior were first tested in Wokwi. The final webpage, Wi-Fi Access Point, servo movement, and LED indicators were then tested successfully using the physical ESP32.

[Open Task 3 Documentation](./Task-3-ESP32-Web-Controlled-Servo)

## Folder Structure

```text
Electrical/
├── README.md
├── Task-1-Servo-Motors/
│   ├── README.md
│   └── files/
│       ├── servo-code.ino
│       └── tinkercad-circuit.png
├── Task-2-DC-Motor-Control-and-Obstacle-Avoidance/
│   ├── README.md
│   ├── Subtask-1-Tinkercad-Simulation/
│   │   ├── README.md
│   │   └── files/
│   │       ├── simulation-circuit.png
│   │       ├── simulation-code.png
│   │       ├── simulation-demo.gif
│   │       └── simulation-code.ino
│   └── Subtask-2-Hands-On-Servo-Control/
│       ├── README.md
│       └── files/
│           ├── media/
│           │   ├── circuit-overview.jpg
│           │   ├── hands-on-demo.mov
│           │   └── serial-monitor.png
│           ├── src/
│           │   └── main.cpp
│           ├── .gitignore
│           └── platformio.ini
└── Task-3-ESP32-Web-Controlled-Servo/
    ├── README.md
    ├── platformio.ini
    ├── src/
    │   └── main.cpp
    ├── media/
    │   ├── serial-monitor-output.png
    │   ├── servo-close-state.png
    │   ├── servo-open-state.png
    │   ├── web-control-close-page.png
    │   └── web-control-open-page.png
    └── wokwi/
        ├── diagram.json
        ├── sketch.ino
        └── libraries.txt

# Task 2 – Arduino Motor and Sensor Control

[Back to Electrical Track](../README.md)

## Overview

This task explores Arduino-based motor, sensor, and actuator control through two related subtasks.

The first subtask was completed as a Tinkercad simulation involving DC motor control and obstacle avoidance. The second subtask was completed as a physical Arduino project in which an ultrasonic sensor controls a servo motor based on object distance.

Although both subtasks use Arduino and ultrasonic sensing, they have different hardware configurations and objectives.

---

## Subtasks

| Subtask | Description | Status |
|---|---|---|
| [Subtask 1 – Tinkercad Simulation](./Subtask-1-Tinkercad-Simulation) | DC motor control and obstacle avoidance using an L293D motor driver, ultrasonic sensor, and servo motor | Completed |
| [Subtask 2 – Hands-On Servo Control](./Subtask-2-Hands-On-Servo-Control) | Physical ultrasonic sensor and servo control system with an LED indicator | Completed |

---

## Subtask 1 – Tinkercad Simulation

The first subtask focused on building and testing a simulated Arduino motor-control system in Tinkercad.

The simulation included:

- Arduino Uno
- L293D motor driver
- Four DC motors
- HC-SR04 ultrasonic sensor
- Servo motor
- Motor movement sequences
- Obstacle detection
- Simulated directional scanning

When the ultrasonic sensor detected an obstacle within the specified distance, the motors stopped and the servo moved to simulate scanning the surrounding area.

[View Subtask 1 documentation](./Subtask-1-Tinkercad-Simulation)

---

## Subtask 2 – Hands-On Servo Control

The second subtask focused on building a physical Arduino system using an HC-SR04 ultrasonic sensor and an SG90 servo motor.

The physical system included:

- Arduino Uno
- HC-SR04 ultrasonic sensor
- SG90 servo motor
- LED
- 330 Ω resistor
- Breadboard and jumper wires

The final system was configured to:

1. Keep the servo at `0°` while the area is clear.
2. Move the servo to `90°` when an object reaches `10 cm` or closer.
3. Turn on the LED while the servo is moving.
4. Keep the servo activated while the object remains nearby.
5. Return the servo to `0°` when the object moves beyond `12 cm`.

Different servo angles and detection distances were also tested using one configurable program.

[View Subtask 2 documentation](./Subtask-2-Hands-On-Servo-Control)

---

## Comparison

| Feature | Subtask 1 | Subtask 2 |
|---|---|---|
| Implementation | Tinkercad simulation | Physical circuit |
| Main output | DC motor movement | Servo movement |
| Motor driver | L293D | Not required |
| DC motors | Four | None |
| Servo motor | Used for simulated scanning | Controlled directly by distance |
| Ultrasonic sensor | Obstacle detection | Distance-based servo activation |
| LED | Not included | Movement indicator |
| Development environment | Tinkercad | Visual Studio Code and PlatformIO |

---

## Project Structure

```text
Task-2-DC-Motor-Control-and-Obstacle-Avoidance/
├── README.md
├── Subtask-1-Tinkercad-Simulation/
│   ├── README.md
│   └── files/
└── Subtask-2-Hands-On-Servo-Control/
    ├── README.md
    └── files/
        ├── media/
        ├── src/
        │   └── main.cpp
        ├── .gitignore
        └── platformio.ini
```

---

## Tools and Technologies

- Arduino Uno
- Tinkercad Circuits
- Visual Studio Code
- PlatformIO IDE
- Arduino framework
- L293D motor driver
- HC-SR04 ultrasonic sensor
- SG90 servo motor
- DC motors
- LED

---

## Results

Both subtasks were completed successfully.

The simulation demonstrated DC motor control, movement sequences, obstacle detection, and servo-based scanning.

The hands-on implementation successfully measured object distance, controlled an SG90 servo motor, operated an LED movement indicator, and prevented unstable switching near the detection threshold.

---

## Learning Outcomes

Through this task, I learned how to:

- Control DC motors using an L293D motor driver.
- Create motor movement sequences using Arduino.
- Measure distance using an HC-SR04 ultrasonic sensor.
- Control an SG90 servo motor based on sensor input.
- Combine sensors, motors, servos, and indicators in Arduino projects.
- Build and test circuits using Tinkercad.
- Develop physical Arduino projects using PlatformIO.
- Compare simulated and hands-on circuit implementations.
- Organize related projects into clear GitHub subtasks.

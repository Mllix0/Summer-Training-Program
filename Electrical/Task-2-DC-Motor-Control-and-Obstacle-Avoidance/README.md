# Task 2 - DC Motor Control and Obstacle Avoidance

[Back to Electrical Track](../README.md)

## Overview

This task focuses on controlling DC motors and creating an obstacle avoidance system using Arduino.

The task is divided into two parts:

1. Tinkercad simulation
2. Hands-on hardware implementation

For now, the Tinkercad simulation was completed. The hands-on hardware implementation will be completed later when the physical components arrive.

## Task Requirements

The task requires creating a system that includes:

- 4 DC motors
- L293D motor driver
- Ultrasonic sensor
- Servo motor
- Arduino control

The required motor sequence is:

1. Move forward for 30 seconds.
2. Move backward for 60 seconds.
3. Move right and left alternately for 60 seconds.
4. Stop the motors.

The obstacle avoidance part requires:

- Detecting obstacles using an ultrasonic sensor.
- If the obstacle distance is 10 cm or less, the motors should stop.
- The servo motor should move to simulate scanning.

## Task Structure

```text
Task-2-DC-Motor-Control-and-Obstacle-Avoidance/
├── README.md
└── Subtask-1-Tinkercad-Simulation/
    ├── README.md
    └── files/
        ├── simulation-circuit.png
        ├── simulation-code.png
        ├── simulation-demo.gif
        └── simulation-code.ino

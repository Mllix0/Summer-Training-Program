# Electrical Track

[Back to Main Page](../README.md)

## Overview

This page documents the tasks, progress, and learning outcomes related to the Electrical track of the robotics summer training program.

The Electrical track focuses on circuits, sensors, motors, microcontrollers, wiring, power systems, simulations, and electronic components used in robotics systems.

Each task has its own folder and README file that includes the circuit explanation, code, screenshots, results, challenges, and what I learned.

## Tasks

| Task No. | Task Name | Date | Status | Documentation |
|---|---|---|---|---|
| 1 | Four Servo Motors Control Using Tinkercad | 2026-07-14 | Completed | [View Task](./Task-1-Servo-Motors) |
| 2 | DC Motor Control and Obstacle Avoidance | 2026-07-27 | Simulation Completed | [View Task](./Task-2-DC-Motor-Control-and-Obstacle-Avoidance) |

## Task Summary

### Task 1: Four Servo Motors Control Using Tinkercad

This task focused on programming four servo motors in Tinkercad using Arduino.

The motors were programmed to run using a sweep motion for 2 seconds, then all motors stopped and held at 90 degrees. The circuit was built using an Arduino Uno, a breadboard, and four micro servo motors.

[Open Task 1 Documentation](./Task-1-Servo-Motors)

### Task 2: DC Motor Control and Obstacle Avoidance

This task focused on controlling four DC motors using Arduino and L293D motor drivers.

The simulation was built in Tinkercad using an Arduino Uno, two L293D motor driver ICs, four DC motors, an ultrasonic sensor, and a servo motor. The motors followed the required movement sequence: forward, backward, right and left alternating, then stop.

The ultrasonic sensor was used to detect obstacles. If an obstacle was detected at a distance of 10 cm or less, the motors stopped and the servo motor moved left and right to simulate scanning.

The Tinkercad simulation was completed successfully. The hands-on hardware implementation will be completed later when the physical components arrive.

[Open Task 2 Documentation](./Task-2-DC-Motor-Control-and-Obstacle-Avoidance)

## Folder Structure

```text
Electrical/
├── README.md
├── Task-1-Servo-Motors/
│   ├── README.md
│   └── files/
│       ├── servo-code.ino
│       └── tinkercad-circuit.png
└── Task-2-DC-Motor-Control-and-Obstacle-Avoidance/
    ├── README.md
    └── Subtask-1-Tinkercad-Simulation/
        ├── README.md
        └── files/
            ├── simulation-circuit.png
            ├── simulation-code.png
            ├── simulation-demo.gif
            └── simulation-code.ino
```

## Tools and Topics

Through the Electrical track tasks, the following tools and topics were practiced:

- Basic circuits
- Arduino Uno
- Tinkercad Circuits
- Breadboard wiring
- Power and ground rails
- Arduino C/C++
- Servo motors
- DC motors
- L293D motor drivers
- Ultrasonic sensor HC-SR04
- Motor direction control
- Digital output pins
- Sensor input reading
- Distance measurement
- Obstacle detection
- Timing using `delay()` and `millis()`
- Simulation testing
- GitHub documentation

## Skills Practiced

Through these tasks, I practiced:

- Building circuits using Tinkercad
- Programming Arduino boards
- Controlling servo motors
- Controlling DC motors using motor drivers
- Using two L293D motor drivers to control four DC motors
- Controlling motor direction using Arduino digital pins
- Creating a movement sequence using Arduino code
- Reading distance values from an ultrasonic sensor
- Stopping motors when an obstacle is detected
- Controlling a servo motor after obstacle detection
- Combining motors, sensors, and servo movement in one system
- Organizing electrical task documentation on GitHub

## Notes

- Each Electrical task has its own folder and README page.
- The main Electrical page is used as an index and summary page.
- Detailed documentation, code files, screenshots, and outputs are stored inside each task folder.
- Tinkercad simulation is useful for testing circuit logic before building the physical circuit.
- For real hardware, motors usually need an external power supply instead of drawing all power directly from the Arduino 5V pin.
- The hands-on hardware implementation for Task 2 will be completed later when the required physical components arrive.

## Reflection

The Electrical track helped me understand how Arduino can be used to control different actuators and sensors in robotics systems.

In Task 1, I practiced controlling servo motors and understanding how servo position can be changed using code.

In Task 2, I learned how to control multiple DC motors using L293D motor drivers and how to combine motor movement with sensor-based obstacle detection. This task also showed how motors, sensors, and servo movement can work together in one robotic system.

These tasks are important steps toward building more complete robotics projects using real hardware.

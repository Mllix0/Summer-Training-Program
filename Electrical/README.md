# Electrical Track

[Back to Main Page](../README.md)

## Overview

This page documents the tasks, progress, and learning outcomes related to the Electrical track of the robotics summer training program.

The Electrical track focuses on circuits, sensors, motors, microcontrollers, wiring, simulations, and electronic components used in robotics systems.

Each task has its own folder and README file containing the circuit explanation, code, screenshots, demonstrations, results, challenges, and learning outcomes.

## Tasks

| Task No. | Task Name | Date | Status | Documentation |
|---|---|---|---|---|
| 1 | Four Servo Motors Control Using Tinkercad | 2026-07-14 | Completed | [View Task](./Task-1-Servo-Motors) |
| 2 | Arduino Motor and Sensor Control | 2026-07-27 | Completed | [View Task](./Task-2-DC-Motor-Control-and-Obstacle-Avoidance) |

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

Although both subtasks use Arduino, ultrasonic sensing, and servo control, they have different hardware configurations and objectives.

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

The HC-SR04 sensor was used to detect obstacles. When an obstacle was detected at a distance of 10 cm or less, the motors stopped and the servo moved left and right to simulate directional scanning.

The complete circuit and program were tested successfully in Tinkercad.

[Open Subtask 1 Documentation](./Task-2-DC-Motor-Control-and-Obstacle-Avoidance/Subtask-1-Tinkercad-Simulation)

#### Subtask 2: Hands-On Ultrasonic Servo Control

The second subtask focused on building a physical Arduino system using an HC-SR04 ultrasonic sensor and an SG90 servo motor.

The physical circuit included:

- Arduino Uno
- HC-SR04 ultrasonic sensor
- SG90 servo motor
- LED
- 330 Ω resistor
- Breadboard
- Jumper wires

The final system operates as follows:

1. The servo remains at its original position of `0°` while the area is clear.
2. When an object reaches `10 cm` or closer, the LED turns on while the servo moves to `90°`.
3. The servo remains at `90°` while the object is nearby.
4. When the object moves beyond `12 cm`, the LED turns on while the servo returns to `0°`.

The separate activation and return distances prevent unstable movement when the ultrasonic reading fluctuates near the detection threshold.

Different servo angles and detection distances were tested using one configurable program. The final selected values were:

| Setting | Final Value |
|---|---:|
| Original servo angle | 0° |
| Activated servo angle | 90° |
| Activation distance | 10 cm |
| Return distance | 12 cm |

The project was developed using Visual Studio Code and PlatformIO. The complete physical circuit, Serial Monitor output, source code, and demonstration video were documented.

[Open Subtask 2 Documentation](./Task-2-DC-Motor-Control-and-Obstacle-Avoidance/Subtask-2-Hands-On-Servo-Control)

[Open Complete Task 2 Documentation](./Task-2-DC-Motor-Control-and-Obstacle-Avoidance)

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
    ├── Subtask-1-Tinkercad-Simulation/
    │   ├── README.md
    │   └── files/
    │       ├── simulation-circuit.png
    │       ├── simulation-code.png
    │       ├── simulation-demo.gif
    │       └── simulation-code.ino
    └── Subtask-2-Hands-On-Servo-Control/
        ├── README.md
        └── files/
            ├── media/
            │   ├── circuit-overview.jpg
            │   ├── hands-on-demo.mov
            │   └── serial-monitor.png
            ├── src/
            │   └── main.cpp
            ├── .gitignore
            └── platformio.ini
```

## Tools and Topics

Through the Electrical track tasks, the following tools and topics were practiced:

- Basic electrical circuits
- Arduino Uno
- Arduino C/C++
- Tinkercad Circuits
- Visual Studio Code
- PlatformIO IDE
- PlatformIO Serial Monitor
- Breadboard wiring
- Power and ground connections
- Servo motors
- SG90 servo motor
- DC motors
- L293D motor drivers
- HC-SR04 ultrasonic sensor
- LEDs and current-limiting resistors
- Motor direction control
- Digital input and output pins
- Ultrasonic distance measurement
- Obstacle detection
- Sensor-based actuator control
- State-based programming logic
- Timing using `delay()` and `millis()`
- Simulation testing
- Physical circuit testing
- GitHub documentation

## Skills Practiced

Through these tasks, I practiced:

- Building and testing circuits using Tinkercad.
- Building a physical Arduino circuit using a breadboard and jumper wires.
- Programming Arduino boards using Arduino C/C++.
- Developing Arduino projects in Visual Studio Code using PlatformIO.
- Controlling multiple servo motors.
- Controlling DC motors using L293D motor drivers.
- Using two L293D motor drivers to control four DC motors.
- Controlling motor direction using Arduino digital pins.
- Creating motor movement sequences using Arduino code.
- Measuring distance using an HC-SR04 ultrasonic sensor.
- Stopping motors when an obstacle is detected.
- Controlling a servo motor based on measured distance.
- Using an LED as a servo-movement indicator.
- Using separate activation and return thresholds to improve system stability.
- Testing different servo angles and detection distances.
- Reading and interpreting Serial Monitor output.
- Combining motors, sensors, servos, and indicators in Arduino systems.
- Organizing related projects into clear GitHub tasks and subtasks.

## Notes

- Each Electrical task has its own folder and README page.
- The main Electrical page is used as an index and summary page.
- Detailed documentation, code files, screenshots, and demonstrations are stored inside each task folder.
- Task 2 contains two related but different subtasks: a Tinkercad motor-control simulation and a physical ultrasonic-servo project.
- Tinkercad is useful for testing circuit logic before building physical circuits.
- PlatformIO was used to develop, upload, and monitor the hands-on Arduino project.
- A 330 Ω resistor was used with the LED in the hands-on circuit.
- The SG90 servo was tested separately before being combined with the ultrasonic sensor and LED.
- For larger physical projects, motors and servos may require an external regulated power supply instead of drawing all power directly from the Arduino 5V pin.
- When an external supply is used, its ground must be connected to the Arduino ground.

## Reflection

The Electrical track helped me understand how Arduino can be used to control different actuators and process sensor input in robotics systems.

In Task 1, I practiced controlling multiple servo motors and learned how servo positions and movement sequences can be managed using Arduino code.

In Task 2 Subtask 1, I learned how to control four DC motors using L293D motor drivers and how to combine motor movement with ultrasonic obstacle detection and servo-based scanning.

In Task 2 Subtask 2, I moved from simulation to physical hardware. I learned how to wire and test an HC-SR04 sensor, SG90 servo motor, and LED. I also learned how to use sensor measurements to control an actuator, display system information through the Serial Monitor, and improve stability using separate activation and return distances.

These tasks provided practical experience with circuit design, Arduino programming, simulation, physical testing, troubleshooting, and project documentation. They are important steps toward building more complete robotic systems that combine sensors, motors, actuators, and decision-making logic.

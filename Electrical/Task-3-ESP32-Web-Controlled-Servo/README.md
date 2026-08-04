# Task 3: ESP32 Web-Controlled Servo Motor

[Back to Electrical Track](../README.md)

## Overview

This task implements a web-controlled servo motor system using an ESP32.

The ESP32 operates in **Wi-Fi Access Point mode**, which means it creates its own wireless network without requiring an external router or internet connection.

After connecting a phone or computer to the ESP32 network, the user can open a locally hosted webpage and control the servo motor using two buttons:

- **OPEN**
- **CLOSE**

Two LEDs indicate the current state of the system:

- Green LED: Open
- Red LED: Closed

The project was first tested using Wokwi and then implemented using a physical ESP32 circuit.

---

## Objective

The objective of this task was to:

- Configure the ESP32 as a Wi-Fi Access Point
- Host a webpage directly from the ESP32
- Control a servo motor from a browser
- Use LEDs to display the current servo state
- Test the system using both simulation and physical components
- Document the circuit, code, results, and implementation process

---

## System Behavior

### Open State

When the **OPEN** button is pressed:

- The servo moves to `90°`
- The green LED turns on
- The red LED turns off
- The webpage displays `OPEN`
- The Serial Monitor prints `State: OPEN`

### Closed State

When the **CLOSE** button is pressed:

- The servo returns to `0°`
- The red LED turns on
- The green LED turns off
- The webpage displays `CLOSED`
- The Serial Monitor prints `State: CLOSED`

---

## Components Used

| Component | Quantity |
|---|---:|
| ESP32 38-pin development board | 1 |
| Micro servo motor | 1 |
| Green LED | 1 |
| Red LED | 1 |
| 220 Ω resistor | 2 |
| Breadboard | 1 |
| Jumper wires | Several |
| Micro-USB cable | 1 |

---

## ESP32 Board

The physical project uses a 38-pin ESP32 development board with an ESP-WROOM-32 module.

The PlatformIO board configuration used was:

```ini
board = esp32dev
```

The following GPIO pins were used:

| Component | ESP32 connection |
|---|---|
| Servo signal | GPIO 18 |
| Green LED | GPIO 26 |
| Red LED | GPIO 27 |
| Servo power | VCC / 5V |
| Servo ground | GND |
| LED ground | GND |

The flash-memory pins were not used:

```text
SD0
SD1
SD2
SD3
CLK
CMD
```

---

## Circuit Connections

### Servo Motor

| Servo wire | Function | ESP32 connection |
|---|---|---|
| Orange, yellow, or white | Signal | GPIO 18 |
| Red | Power | VCC / 5V |
| Brown or black | Ground | GND |

### Green LED

```text
GPIO 26 → 220 Ω resistor → Green LED anode
Green LED cathode → GND
```

### Red LED

```text
GPIO 27 → 220 Ω resistor → Red LED anode
Red LED cathode → GND
```

All components share a common ground.

---

## Software and Tools

The following software and tools were used:

- Visual Studio Code
- PlatformIO
- Arduino framework
- ESP32Servo library
- Wokwi
- Web browser
- GitHub

---

## PlatformIO Configuration

The PlatformIO configuration is stored in:

```text
platformio.ini
```

Configuration:

```ini
[env:esp32dev]
platform = espressif32
board = esp32dev
framework = arduino

monitor_speed = 115200

lib_deps =
    madhephaestus/ESP32Servo
```

---

## Wi-Fi Access Point

The ESP32 creates its own Wi-Fi network using Access Point mode.

The network details used in this project are:

```text
Network name: ESP32-Servo-Control
Password: 12345678
IP address: 192.168.4.1
```

After connecting to the ESP32 network, the control webpage is opened using:

```text
http://192.168.4.1
```

The project uses HTTP because the webpage is hosted locally on the ESP32 and no HTTPS server or certificate is configured.

The connected device may display a **No Internet Connection** warning. This is expected because the ESP32 provides a local control network rather than internet access.

---

## Web Server Routes

The web server runs on port 80.

| Route | Function |
|---|---|
| `/` | Displays the control webpage |
| `/open` | Moves the servo to the open position |
| `/close` | Moves the servo to the closed position |

After an Open or Close command is executed, the browser is redirected back to the main page so the updated state is displayed.

---

## Web Interface

The webpage contains:

- Project title
- Current servo status
- Green Open button
- Red Close button
- Responsive design for phones and computers

The status text changes color depending on the current state:

- Green for `OPEN`
- Red for `CLOSED`

---

## Wokwi Simulation

The circuit was first created and tested using Wokwi.

The simulation was used to verify:

- Servo movement
- Green LED operation
- Red LED operation
- GPIO assignments
- Wi-Fi Access Point initialization
- Web server initialization
- Initial closed state

The standard online Wokwi simulation could initialize the Access Point and web server, but the simulated local IP address could not be accessed directly from the computer browser.

The final webpage control was therefore tested using the physical ESP32.

The Wokwi files are stored inside:

```text
wokwi/
```

---

## Physical Implementation

After confirming the component behavior in Wokwi, the circuit was recreated using the physical ESP32.

The ESP32 was connected to the computer through USB, and the code was compiled and uploaded using PlatformIO.

The physical implementation successfully:

- Created the ESP32 Wi-Fi network
- Hosted the control webpage
- Accepted Open and Close commands
- Moved the servo between `0°` and `90°`
- Controlled the red and green LEDs
- Updated the webpage status
- Printed system information in the Serial Monitor

---

## Open State

In the open state:

- The servo moves to `90°`
- The green LED turns on
- The red LED turns off
- The webpage displays `OPEN`

<p align="center">
  <img src="./media/servo-open-state.png" alt="Physical servo open state with green LED on" width="45%">
  <img src="./media/web-control-open-page.png" alt="Web control page displaying open state" width="45%">
</p>

---

## Closed State

In the closed state:

- The servo moves to `0°`
- The red LED turns on
- The green LED turns off
- The webpage displays `CLOSED`

<p align="center">
  <img src="./media/servo-close-state.png" alt="Physical servo closed state with red LED on" width="45%">
  <img src="./media/web-control-close-page.png" alt="Web control page displaying closed state" width="45%">
</p>

---

## Serial Monitor Output

The Serial Monitor displays:

- Access Point startup
- Network name
- Network password
- ESP32 IP address
- Web server startup
- Open commands
- Close commands

<p align="center">
  <img src="./media/serial-monitor-output.png" alt="ESP32 Serial Monitor output" width="85%">
</p>

Example output:

```text
Starting ESP32 Access Point...
Wi-Fi Access Point created successfully
Network name: ESP32-Servo-Control
Password: 12345678
IP address: 192.168.4.1
Web server started

State: OPEN
State: CLOSED
```

---

## Source Code

The complete PlatformIO source code is stored in:

```text
src/main.cpp
```

The program includes:

- ESP32 Wi-Fi Access Point configuration
- Web server configuration
- HTML and CSS webpage
- Servo control functions
- LED control functions
- Open and Close routes
- Serial Monitor messages
- Error handling for Access Point startup

---

## Testing Process

The system was tested using the following sequence:

1. Power the ESP32 through USB.
2. Confirm that the red LED turns on.
3. Confirm that the servo starts in the closed position.
4. Connect a phone to `ESP32-Servo-Control`.
5. Open `http://192.168.4.1`.
6. Press the Open button.
7. Confirm the servo moves to `90°`.
8. Confirm the green LED turns on.
9. Confirm the webpage displays `OPEN`.
10. Press the Close button.
11. Confirm the servo returns to `0°`.
12. Confirm the red LED turns on.
13. Confirm the webpage displays `CLOSED`.
14. Repeat the sequence several times.

The repeated tests were completed successfully without losing the Wi-Fi connection or restarting the ESP32.

---

## Results

The final system operated successfully.

The ESP32 created a stable local Wi-Fi Access Point and hosted a responsive control webpage.

Both browser commands worked correctly:

| Command | Servo position | Green LED | Red LED |
|---|---:|---|---|
| Open | 90° | On | Off |
| Close | 0° | Off | On |

The webpage, servo position, LEDs, and Serial Monitor output remained synchronized during repeated testing.

---

## Challenges and Solutions

### Accessing the Wokwi Web Server

The Wokwi simulation successfully started the Access Point and web server, but the simulated IP address could not be opened directly from the normal computer browser.

**Solution:**  
The web interface was tested using the physical ESP32, where the phone could connect directly to the ESP32 network.

### HTTP Instead of HTTPS

The local ESP32 webpage used:

```text
http://192.168.4.1
```

The browser connection did not use HTTPS.

**Explanation:**  
The ESP32 program creates a standard HTTP server on port 80. HTTPS would require additional certificate and encryption configuration, which was not required for this local project.

### Servo Power

A servo motor can draw more current than a GPIO pin can provide.

**Solution:**  
The servo signal was connected to GPIO 18, while the power wire was connected to the 5 V supply rather than the 3.3 V pin. A common ground was used between the ESP32 and servo.

For a larger or higher-current servo, a separate regulated 5 V power supply should be used with a shared ground.

---

## What I Learned

Through this task, I learned how to:

- Configure the ESP32 as a Wi-Fi Access Point
- Host a webpage directly from a microcontroller
- Create HTTP routes using the ESP32 WebServer library
- Control a servo motor using browser commands
- Control LEDs using GPIO outputs
- Build a responsive webpage using HTML and CSS
- Use PlatformIO with an ESP32 project
- Add external libraries through `platformio.ini`
- Upload code and use the Serial Monitor in VS Code
- Test a project first in simulation and then using physical components
- Synchronize hardware state with a web interface

---

## Project Structure

```text
Task-3-ESP32-Web-Controlled-Servo/
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
```

---

## Conclusion

This task demonstrated how an ESP32 can create its own local Wi-Fi network and host a webpage for controlling physical hardware.

The completed system allowed a user to control a servo motor from a phone browser while receiving clear visual feedback through red and green LEDs.

The project successfully combined embedded programming, circuit wiring, Wi-Fi communication, web development, servo control, and physical testing.

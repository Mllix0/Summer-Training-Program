#include <WiFi.h>
#include <WebServer.h>
#include <ESP32Servo.h>

const int SERVO_PIN = 18;
const int GREEN_LED_PIN = 26;
const int RED_LED_PIN = 27;

const int CLOSED_ANGLE = 0;
const int OPEN_ANGLE = 90;

const char* WIFI_NAME = "ESP32-Servo-Control";
const char* WIFI_PASSWORD = "12345678";

Servo servoMotor;
WebServer server(80);

String currentState = "CLOSED";

void showClosedState() {
  servoMotor.write(CLOSED_ANGLE);

  digitalWrite(GREEN_LED_PIN, LOW);
  digitalWrite(RED_LED_PIN, HIGH);

  currentState = "CLOSED";
  Serial.println("State: CLOSED");
}

void showOpenState() {
  servoMotor.write(OPEN_ANGLE);

  digitalWrite(GREEN_LED_PIN, HIGH);
  digitalWrite(RED_LED_PIN, LOW);

  currentState = "OPEN";
  Serial.println("State: OPEN");
}

String createWebPage() {
  String statusColor;

  if (currentState == "OPEN") {
    statusColor = "#16a34a";
  } else {
    statusColor = "#dc2626";
  }

  String page = R"rawliteral(
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <title>ESP32 Servo Control</title>

  <style>
    * {
      box-sizing: border-box;
    }

    body {
      margin: 0;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      background: #f1f5f9;
      font-family: Arial, sans-serif;
      color: #0f172a;
    }

    .card {
      width: min(90%, 480px);
      padding: 36px;
      background: white;
      border-radius: 20px;
      box-shadow: 0 12px 35px rgba(15, 23, 42, 0.15);
      text-align: center;
    }

    h1 {
      margin-top: 0;
      margin-bottom: 12px;
      font-size: 30px;
    }

    .description {
      margin-bottom: 28px;
      color: #475569;
      line-height: 1.6;
    }

    .status-box {
      margin-bottom: 30px;
      padding: 18px;
      border-radius: 12px;
      background: #f8fafc;
      border: 2px solid #e2e8f0;
    }

    .status-label {
      display: block;
      margin-bottom: 8px;
      font-size: 15px;
      color: #64748b;
    }

    .status-value {
      font-size: 28px;
      font-weight: bold;
      color: STATUS_COLOR;
    }

    .buttons {
      display: flex;
      gap: 16px;
    }

    .button {
      flex: 1;
      padding: 16px;
      border: none;
      border-radius: 12px;
      color: white;
      font-size: 18px;
      font-weight: bold;
      text-decoration: none;
      cursor: pointer;
    }

    .open-button {
      background: #16a34a;
    }

    .close-button {
      background: #dc2626;
    }

    .button:hover {
      opacity: 0.88;
    }

    @media (max-width: 480px) {
      .card {
        padding: 26px 20px;
      }

      .buttons {
        flex-direction: column;
      }
    }
  </style>
</head>

<body>
  <div class="card">
    <h1>ESP32 Servo Control</h1>

    <p class="description">
      Use the buttons below to control the servo motor and status LEDs.
    </p>

    <div class="status-box">
      <span class="status-label">Current Status</span>
      <span class="status-value">CURRENT_STATE</span>
    </div>

    <div class="buttons">
      <a class="button open-button" href="/open">OPEN</a>
      <a class="button close-button" href="/close">CLOSE</a>
    </div>
  </div>
</body>
</html>
)rawliteral";

  page.replace("CURRENT_STATE", currentState);
  page.replace("STATUS_COLOR", statusColor);

  return page;
}

void handleHomePage() {
  server.send(200, "text/html", createWebPage());
}

void handleOpenCommand() {
  showOpenState();
  server.sendHeader("Location", "/");
  server.send(303);
}

void handleCloseCommand() {
  showClosedState();
  server.sendHeader("Location", "/");
  server.send(303);
}

void handleNotFound() {
  server.send(404, "text/plain", "Page not found");
}

void setup() {
  Serial.begin(115200);

  pinMode(GREEN_LED_PIN, OUTPUT);
  pinMode(RED_LED_PIN, OUTPUT);

  servoMotor.setPeriodHertz(50);
  servoMotor.attach(SERVO_PIN, 500, 2400);

  showClosedState();

  Serial.println();
  Serial.println("Starting ESP32 Access Point...");

  WiFi.softAP(WIFI_NAME, WIFI_PASSWORD);

  IPAddress accessPointIP = WiFi.softAPIP();

  Serial.println("Wi-Fi Access Point created successfully");
  Serial.print("Network name: ");
  Serial.println(WIFI_NAME);
  Serial.print("Password: ");
  Serial.println(WIFI_PASSWORD);
  Serial.print("IP address: ");
  Serial.println(accessPointIP);

  server.on("/", handleHomePage);
  server.on("/open", handleOpenCommand);
  server.on("/close", handleCloseCommand);
  server.onNotFound(handleNotFound);

  server.begin();

  Serial.println("Web server started");
}

void loop() {
  server.handleClient();
}
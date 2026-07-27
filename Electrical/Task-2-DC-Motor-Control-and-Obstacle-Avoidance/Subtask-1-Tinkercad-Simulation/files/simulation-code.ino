#include <Servo.h>

// First L293D - Motor 1 and Motor 2
int motor1Pin1 = 2;
int motor1Pin2 = 3;

int motor2Pin1 = 4;
int motor2Pin2 = 5;

// Second L293D - Motor 3 and Motor 4
int motor3Pin1 = 6;
int motor3Pin2 = 7;

int motor4Pin1 = 8;
int motor4Pin2 = 9;

// Servo motor
int servoPin = 10;
Servo scanServo;

// Ultrasonic sensor
int trigPin = 11;
int echoPin = 12;

// Obstacle distance limit
int obstacleDistance = 10;

void setup() {
  Serial.begin(9600);

  pinMode(motor1Pin1, OUTPUT);
  pinMode(motor1Pin2, OUTPUT);

  pinMode(motor2Pin1, OUTPUT);
  pinMode(motor2Pin2, OUTPUT);

  pinMode(motor3Pin1, OUTPUT);
  pinMode(motor3Pin2, OUTPUT);

  pinMode(motor4Pin1, OUTPUT);
  pinMode(motor4Pin2, OUTPUT);

  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  scanServo.attach(servoPin);
  scanServo.write(90);

  stopMotors();
}

void loop() {
  // 1. Move forward for 30 seconds
  runMovementForTime("Forward", 30000);

  // 2. Move backward for 60 seconds
  runMovementForTime("Backward", 60000);

  // 3. Move right and left alternately for 60 seconds
  unsigned long startTime = millis();

  while (millis() - startTime < 60000) {
    runTurnForTime("Right", 5000);
    runTurnForTime("Left", 5000);
  }

  // 4. Stop motors at the end
  stopMotors();

  while (true) {
    stopMotors();
  }
}

void runMovementForTime(String direction, unsigned long duration) {
  unsigned long startTime = millis();

  while (millis() - startTime < duration) {
    int distance = getDistance();

    Serial.print("Distance: ");
    Serial.print(distance);
    Serial.println(" cm");

    if (distance > 0 && distance <= obstacleDistance) {
      handleObstacle();
    } else {
      if (direction == "Forward") {
        moveForward();
      } else if (direction == "Backward") {
        moveBackward();
      }
    }

    delay(200);
  }

  stopMotors();
}

void runTurnForTime(String direction, unsigned long duration) {
  unsigned long startTime = millis();

  while (millis() - startTime < duration) {
    int distance = getDistance();

    Serial.print("Distance: ");
    Serial.print(distance);
    Serial.println(" cm");

    if (distance > 0 && distance <= obstacleDistance) {
      handleObstacle();
    } else {
      if (direction == "Right") {
        turnRight();
      } else if (direction == "Left") {
        turnLeft();
      }
    }

    delay(200);
  }

  stopMotors();
}

int getDistance() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  long duration = pulseIn(echoPin, HIGH, 30000);

  if (duration == 0) {
    return -1;
  }

  int distance = duration * 0.034 / 2;
  return distance;
}

void handleObstacle() {
  stopMotors();

  Serial.println("Obstacle detected. Motors stopped.");

  scanServo.write(30);
  delay(500);

  scanServo.write(150);
  delay(500);

  scanServo.write(90);
  delay(500);
}

void moveForward() {
  // Motor 1
  digitalWrite(motor1Pin1, HIGH);
  digitalWrite(motor1Pin2, LOW);

  // Motor 2 - reversed to match Motor 1
  digitalWrite(motor2Pin1, LOW);
  digitalWrite(motor2Pin2, HIGH);

  // Motor 3
  digitalWrite(motor3Pin1, HIGH);
  digitalWrite(motor3Pin2, LOW);

  // Motor 4 - reversed to match Motor 3
  digitalWrite(motor4Pin1, LOW);
  digitalWrite(motor4Pin2, HIGH);
}

void moveBackward() {
  // Motor 1
  digitalWrite(motor1Pin1, LOW);
  digitalWrite(motor1Pin2, HIGH);

  // Motor 2 - reversed to match Motor 1
  digitalWrite(motor2Pin1, HIGH);
  digitalWrite(motor2Pin2, LOW);

  // Motor 3
  digitalWrite(motor3Pin1, LOW);
  digitalWrite(motor3Pin2, HIGH);

  // Motor 4 - reversed to match Motor 3
  digitalWrite(motor4Pin1, HIGH);
  digitalWrite(motor4Pin2, LOW);
}

void turnRight() {
  // Left side motors forward
  digitalWrite(motor1Pin1, HIGH);
  digitalWrite(motor1Pin2, LOW);

  digitalWrite(motor2Pin1, LOW);
  digitalWrite(motor2Pin2, HIGH);

  // Right side motors backward
  digitalWrite(motor3Pin1, LOW);
  digitalWrite(motor3Pin2, HIGH);

  digitalWrite(motor4Pin1, HIGH);
  digitalWrite(motor4Pin2, LOW);
}

void turnLeft() {
  // Left side motors backward
  digitalWrite(motor1Pin1, LOW);
  digitalWrite(motor1Pin2, HIGH);

  digitalWrite(motor2Pin1, HIGH);
  digitalWrite(motor2Pin2, LOW);

  // Right side motors forward
  digitalWrite(motor3Pin1, HIGH);
  digitalWrite(motor3Pin2, LOW);

  digitalWrite(motor4Pin1, LOW);
  digitalWrite(motor4Pin2, HIGH);
}

void stopMotors() {
  digitalWrite(motor1Pin1, LOW);
  digitalWrite(motor1Pin2, LOW);

  digitalWrite(motor2Pin1, LOW);
  digitalWrite(motor2Pin2, LOW);

  digitalWrite(motor3Pin1, LOW);
  digitalWrite(motor3Pin2, LOW);

  digitalWrite(motor4Pin1, LOW);
  digitalWrite(motor4Pin2, LOW);
}
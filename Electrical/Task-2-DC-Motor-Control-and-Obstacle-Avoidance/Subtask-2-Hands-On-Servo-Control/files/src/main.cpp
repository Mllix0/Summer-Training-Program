#include <Arduino.h>
#include <Servo.h>

// -------------------------
// Pin assignments
// -------------------------
const int SERVO_PIN = 6;
const int LED_PIN = 3;
const int TRIG_PIN = 9;
const int ECHO_PIN = 10;

// -------------------------
// Adjustable project settings
// -------------------------

// Change these values to experiment with the servo angles.
const int ORIGINAL_ANGLE = 0;
const int ACTIVATED_ANGLE = 90;

// The servo activates at or below this distance.
const float ACTIVATION_DISTANCE_CM = 10.0;

// The servo returns only after the object moves beyond this distance.
// This prevents unstable switching near 10 cm.
const float RETURN_DISTANCE_CM = 12.0;

// Estimated time required for the servo to finish moving.
const unsigned long SERVO_MOVEMENT_TIME_MS = 500;

// Delay between ultrasonic measurements.
const unsigned long SENSOR_DELAY_MS = 250;

// -------------------------
// Objects and system state
// -------------------------
Servo servoMotor;

bool objectDetected = false;

// -------------------------
// Measure distance
// -------------------------
float measureDistanceCm()
{
    digitalWrite(TRIG_PIN, LOW);
    delayMicroseconds(2);

    digitalWrite(TRIG_PIN, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIG_PIN, LOW);

    const unsigned long duration =
        pulseIn(ECHO_PIN, HIGH, 30000UL);

    if (duration == 0)
    {
        return -1.0;
    }

    return (duration * 0.0343) / 2.0;
}

// -------------------------
// Move servo and operate LED
// -------------------------
void moveServoWithLed(const int targetAngle)
{
    digitalWrite(LED_PIN, HIGH);

    servoMotor.write(targetAngle);
    delay(SERVO_MOVEMENT_TIME_MS);

    digitalWrite(LED_PIN, LOW);
}

// -------------------------
// Initial setup
// -------------------------
void setup()
{
    pinMode(TRIG_PIN, OUTPUT);
    pinMode(ECHO_PIN, INPUT);
    pinMode(LED_PIN, OUTPUT);

    digitalWrite(TRIG_PIN, LOW);
    digitalWrite(LED_PIN, LOW);

    servoMotor.attach(SERVO_PIN);
    servoMotor.write(ORIGINAL_ANGLE);

    Serial.begin(9600);

    delay(1000);

    Serial.println();
    Serial.println("Ultrasonic Servo Control System");
    Serial.println("--------------------------------");
    Serial.print("Original angle: ");
    Serial.print(ORIGINAL_ANGLE);
    Serial.println(" degrees");

    Serial.print("Activated angle: ");
    Serial.print(ACTIVATED_ANGLE);
    Serial.println(" degrees");

    Serial.print("Activation distance: ");
    Serial.print(ACTIVATION_DISTANCE_CM, 1);
    Serial.println(" cm");

    Serial.print("Return distance: ");
    Serial.print(RETURN_DISTANCE_CM, 1);
    Serial.println(" cm");

    Serial.println("--------------------------------");
}

// -------------------------
// Main program
// -------------------------
void loop()
{
    const float distance = measureDistanceCm();

    if (distance < 0)
    {
        Serial.println("No echo received");
        delay(SENSOR_DELAY_MS);
        return;
    }

    Serial.print("Distance: ");
    Serial.print(distance, 1);
    Serial.print(" cm | ");

    // Activate when an object reaches 10 cm or closer.
    if (!objectDetected &&
        distance <= ACTIVATION_DISTANCE_CM)
    {
        objectDetected = true;

        Serial.print("Object detected | Servo moving to ");
        Serial.print(ACTIVATED_ANGLE);
        Serial.println(" degrees");

        moveServoWithLed(ACTIVATED_ANGLE);
    }

    // Return only after the object moves beyond 12 cm.
    else if (objectDetected &&
             distance > RETURN_DISTANCE_CM)
    {
        objectDetected = false;

        Serial.print("Object removed | Servo returning to ");
        Serial.print(ORIGINAL_ANGLE);
        Serial.println(" degrees");

        moveServoWithLed(ORIGINAL_ANGLE);
    }

    // No state change is required.
    else
    {
        if (objectDetected)
        {
            Serial.print("Object remains detected | Servo at ");
            Serial.print(ACTIVATED_ANGLE);
            Serial.println(" degrees");
        }
        else
        {
            Serial.print("Area clear | Servo at ");
            Serial.print(ORIGINAL_ANGLE);
            Serial.println(" degrees");
        }
    }

    delay(SENSOR_DELAY_MS);
}
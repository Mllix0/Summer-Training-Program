#include <Arduino.h>
#include <Servo.h>

Servo frontLeft;
Servo frontRight;
Servo rearLeft;
Servo rearRight;

// Neutral positions
int frontLeftNeutral  = 90;
int frontRightNeutral = 95;
int rearLeftNeutral   = 95;
int rearRightNeutral  = 95;

// Forward movement settings
int moveAmount = 20;
int moveDelay = 350;

void neutralPosition() {
  frontLeft.write(frontLeftNeutral);
  frontRight.write(frontRightNeutral);
  rearLeft.write(rearLeftNeutral);
  rearRight.write(rearRightNeutral);

  delay(250);
}

void moveForward() {

  // Diagonal pair 1
  frontLeft.write(frontLeftNeutral + moveAmount);
  rearRight.write(rearRightNeutral - moveAmount);

  frontRight.write(frontRightNeutral);
  rearLeft.write(rearLeftNeutral);

  delay(moveDelay);

  neutralPosition();

  // Diagonal pair 2
  frontRight.write(frontRightNeutral - moveAmount);
  rearLeft.write(rearLeftNeutral + moveAmount);

  frontLeft.write(frontLeftNeutral);
  rearRight.write(rearRightNeutral);

  delay(moveDelay);

  neutralPosition();
}

void setup() {

  frontLeft.attach(3);
  frontRight.attach(4);
  rearLeft.attach(6);
  rearRight.attach(7);

  neutralPosition();

  // Time to place the robot on the ground
  delay(3000);
}

void loop() {

  // Move forward for an extended period
  for (int i = 0; i < 12; i++) {
    moveForward();
  }

  neutralPosition();

  // Pause before repeating
  delay(3000);
}

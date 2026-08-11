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

// Dance movement settings
int frontDanceAmount = 20;
int rearDanceAmount  = 5;
int danceDelay = 300;

void neutralPosition() {
  frontLeft.write(frontLeftNeutral);
  frontRight.write(frontRightNeutral);
  rearLeft.write(rearLeftNeutral);
  rearRight.write(rearRightNeutral);

  delay(500);
}

void dance() {

  for (int i = 0; i < 6; i++) {

    // Dance position 1
    frontLeft.write(frontLeftNeutral + frontDanceAmount);
    frontRight.write(frontRightNeutral + frontDanceAmount);

    rearLeft.write(rearLeftNeutral - rearDanceAmount);
    rearRight.write(rearRightNeutral - rearDanceAmount);

    delay(danceDelay);

    // Dance position 2
    frontLeft.write(frontLeftNeutral - frontDanceAmount);
    frontRight.write(frontRightNeutral - frontDanceAmount);

    rearLeft.write(rearLeftNeutral + rearDanceAmount);
    rearRight.write(rearRightNeutral + rearDanceAmount);

    delay(danceDelay);
  }

  neutralPosition();
}

void setup() {

  frontLeft.attach(3);
  frontRight.attach(4);
  rearLeft.attach(6);
  rearRight.attach(7);

  neutralPosition();

  // Time to position the robot
  delay(3000);
}

void loop() {

  dance();

  // Pause before repeating
  delay(3000);
}

#include<Servo.h>
Servo servoLeft;
Servo servoRight;


void setup() {
  //circle



  servoLeft.attach(13);                      // Attach left signal to pin 13
  servoRight.attach(12);                     // Attach right signal to pin 12
  servoLeft.writeMicroseconds(1500);        // Calibrate left servo
  servoRight.writeMicroseconds(1500);

for(int i=0; i<=10; i++)
{
  servoLeft.writeMicroseconds(1700);   // Left wheel counterclockwise
  servoRight.writeMicroseconds(1700); // Right wheel counterclockwise
  delay(250);

  
  servoLeft.writeMicroseconds(1300);   // Left wheel counterclockwise
  servoRight.writeMicroseconds(1700); // Right wheel counterclockwise
  delay(200);
  
  servoLeft.writeMicroseconds(1700);   // Left wheel counterclockwise
  servoRight.writeMicroseconds(1300); // Right wheel counterclockwise
  delay(200);
}
  servoLeft.writeMicroseconds(1500);   // Left wheel counterclockwise
  servoRight.writeMicroseconds(1500); // Right wheel counterclockwise

}







void loop() {



}

#include <Servo.h>
int leftWhiskerPin=5;
int rightWhiskerPin=7;
int rightWhiskerValue=0;
int leftWhiskerValue=0;
Servo servoRight;
Servo servoLeft;


void setup() {
  // put your setup code here, to run once:

  pinMode(leftWhiskerPin,INPUT);
  pinMode(rightWhiskerPin, INPUT);
  Serial.begin(9600);
  servoLeft.attach(13);
  servoRight.attach(12);
  servoLeft.writeMicroseconds(1500);
  servoRight.writeMicroseconds(1500);
}

void loop() {
  // put your main code here, to run repeatedly:
  leftWhiskerValue=digitalRead(leftWhiskerPin);
  rightWhiskerValue=digitalRead(rightWhiskerPin);

   if (leftWhiskerValue== 0 && rightWhiskerValue== 0){
      moveback(800);
      turnright(400);
   }
    else if(leftWhiskerValue==0){
      moveback(800);
      turnright(400);
    }
    else if(rightWhiskerValue==0){
      moveback(800);
      turnleft(400);
    }
    else{
      moveforward(20);
    }
  delay(200);
}
   void moveforward(int time){
    servoLeft.writeMicroseconds(1700);
    servoRight.writeMicroseconds(1300);
    delay(time);
  }
  void moveback(int time){
    servoLeft.writeMicroseconds(1300);
    servoRight.writeMicroseconds(1700);
    delay(time);
  }
  void turnleft(int time){
    servoLeft.writeMicroseconds(13 00);
    servoRight.writeMicroseconds(1300);
    delay(time); 
  }
  void turnright(int time){
    servoLeft.writeMicroseconds(1700);
    servoRight.writeMicroseconds(1700);
    delay(time);
  }

#include <Servo.h>

Servo steer;
Servo esc;

const int escIn = 8;
const int steerIn = 9;

const int steerOut = 3;
const int escOut = 5;

void setup(){
  Serial.begin(9600);
  
  pinMode(escIn, INPUT);
  pinMode(steerIn, INPUT);
  
  pinMode(steerOut, OUTPUT);
  pinMode(escOut, OUTPUT);
  
  steer.attach(steerOut);
  esc.attach(escOut);
}

void loop(){
  int escCommand = map(pulseIn(i, HIGH), 1901, 959, 1000, 2000);
  int steerCommand = map(pulseIn(i, HIGH), 1220, 1490, 1000, 2000);
  esc.writeMicroseconds(escCommand);
  steer.writeMicroseconds(steerCommand);
  Serial.print("e");
  Serial.println(escCommand);
  Serial.print("s");
  Serial.println(steerCommand);
}

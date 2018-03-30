#include <Servo.h>

enum State{
  recvSteering,
  recvEsc
};
State state = recvSteering;

Servo steer;
Servo esc;

int steerPin = 3;
int escPin = 5;

void setup(){
  Serial.begin(9600);
  pinMode(steerPin, OUTPUT);
  pinMode(escPin, OUTPUT);

  steer.attach(steerPin);
  esc.attach(escPin);

  // Calibrate the esc
  esc.writeMicroseconds(2000);
  delay(3000);
  esc.writeMicroseconds(1000);
  delay(3000);
  esc.writeMicroseconds(1500);
}

void loop(){
  if(Serial.available()){
    switch((char)Serial.read()){
    case 's': 
      state = recvSteering;
      break;
    case 'e': 
      state = recvEsc;
      break;
    default: 
      switch(state){
        int x;
      case recvSteering: 
        x = Serial.parseInt();
        steer.write(x);
        Serial.println(x);
        break;
      case recvEsc: 
        x = Serial.parseInt();
        esc.writeMicroseconds(x);
        Serial.println(x);
        break;
      default: 
        break;
      }
    } 
  }
}

#include <Servo.h>

enum State{
  recvSteering,
  recvEsc
};
State state = recvSteering;

Servo steer;
Servo esc;

int steerPin = 9;//3;
int escPin = 10;//5;

void setup(){
  Serial.begin(9600);
  pinMode(steerPin, OUTPUT);
  pinMode(escPin, OUTPUT);

  steer.attach(steerPin);
  esc.attach(escPin);
  

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
        break;
      case recvEsc: 
        x = Serial.parseInt();
        esc.writeMicroseconds(x);
        break;
      default: 
        break;
      }
    } 
  }
}

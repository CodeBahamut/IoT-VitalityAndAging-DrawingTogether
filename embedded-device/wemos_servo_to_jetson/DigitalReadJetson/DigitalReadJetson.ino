#define COMMAND_PIN D2
#define SERVO_PIN D4
#define SERVO_UP 0 
#define SERVO_DOWN 180 
#define SERIAL_ID 115200
#define START_DELAY 1000
#define LOOP_DELAY 100

#include <Servo.h>
Servo servo;

// the setup routine runs once when you press reset:
void setup() {
  Serial.begin(SERIAL_ID);
  pinMode(COMMAND_PIN, INPUT_PULLUP);
  servo.attach(SERVO_PIN);

  delay(START_DELAY);
  servo.write(SERVO_UP);
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input pin:
  int inputState = digitalRead(COMMAND_PIN);
  // print out the state of the servo:
  Serial.println(inputState);
  if(inputState == HIGH){
    servo.write(SERVO_DOWN);
  } else if(inputState == LOW){
    servo.write(SERVO_UP);  
  }

  delay(LOOP_DELAY);
}
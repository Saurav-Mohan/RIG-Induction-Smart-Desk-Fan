#include <Servo.h>
String inputString;
Servo left_right;
Servo up_down;
void setup()
{
  left_right.attach(2);
  up_down.attach(3);
  Serial.begin(9600);
}
void loop()
{
  while(Serial.available())
  {
    inputString = Serial.readStringUntil('\r');
    Serial.println(inputString);
    int x_axis = inputString.substring(0, inputString.indexOf(',')).toInt();
    int y_axis = inputString.substring(inputString.indexOf(',') + 1).toInt();

    int y = map(y_axis, 0, 480, 180, 0);
    int x = map(x_axis, 0, 720, 180, 0);

    left_right.write(x);
    up_down.write(y);
  }
}
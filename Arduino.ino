#include <DHT.h>
#define Type DHT11
int sensepin=A0;
DHT HT(sensepin,Type);
float tempC;

#include <Servo.h>
String inputString;
int dir1=6;
int dir2=7;
int servox=11;
int servoy=3;
int motorspeed=9;
float speed;

Servo left_right;
Servo up_down;

void setup()
{pinMode(dir1,OUTPUT);
pinMode(dir2,OUTPUT);
pinMode(sensepin,INPUT);
pinMode(servox,OUTPUT);
pinMode(servoy,OUTPUT);

  left_right.attach(servox);
  up_down.attach(servoy);
  Serial.begin(9600);
  HT.begin();
}


void loop()
{
  while(Serial.available())
  {tempC=HT.readTemperature();
  if (tempC<=24){

digitalWrite(dir1,LOW);
digitalWrite(dir2,HIGH);
analogWrite(motorspeed,75);

  }

  else{
speed=255+20*(tempC-29);

digitalWrite(dir1,LOW);
digitalWrite(dir2,HIGH);
analogWrite(motorspeed,speed);
  }

    inputString = Serial.readStringUntil('\r');
    Serial.println(inputString);
    int x_axis = inputString.substring(0, inputString.indexOf(',')).toInt();
    int y_axis = inputString.substring(inputString.indexOf(',') + 1).toInt();

    int y = map(y_axis, 0, 480, 180, 0);
    int x = map(x_axis, 0, 720, 180, 0);
    left_right.write(x);
    up_down.write(y);
    // Print the parsed values
    Serial.print("First Integer: ");
    Serial.println(x);
    Serial.print("Second Integer: ");
    Serial.println(y);
  }
}

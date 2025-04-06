
import serial
import time
import numpy as np
import cv2

arduinoData = serial.Serial('COM3', 9600) 

def send_coordinates_to_arduino(x, y, w, h):
   
    coordinates = f"{x},{y}\r"
    arduinoData.write(coordinates.encode())
    print(f"X{x}Y{y}\n")    #Send coordinates in "X,Y" format

capture = cv2.VideoCapture(0) 
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    isTrue, frame = capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.05, 8, minSize=(120,120))
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 5)
        send_coordinates_to_arduino(x, y, w, h)

    cv2.imshow('Video', frame)

    if cv2.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv2.destroyAllWindows()

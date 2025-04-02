import cv2
import serial
import time

# Set up Serial Communication with Arduino (Change 'COM3' to your port)
arduino = serial.Serial('COM3', 9600)
time.sleep(2)  # Wait for connection to establish

# Load Haar Cascade Classifier for Face Detection
classifierFace = cv2.CascadeClassifier("C:/OPENCV/haarcascade_frontalface_default.xml")

# Start Webcam
videoCam = cv2.VideoCapture(0)

if not videoCam.isOpened():
    print("The camera is not accessible")
    exit()

while True:
    ret, framework = videoCam.read()  # Capture a frame from the webcam

    if ret:  # Check if the frame was captured successfully
        gray = cv2.cvtColor(framework, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
        faces = classifierFace.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=2)

        for (x, y, w, h) in faces:
            cv2.rectangle(framework, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Print and Send coordinates to Arduino
            print(f"Face detected at: x={x}, y={y}, width={w}, height={h}")
            data = f"{x},{y},{w},{h}\n"  # Format as a string
            arduino.write(data.encode())  # Send data over Serial

            # Display coordinates on the video feed
            cv2.putText(framework, f"({x}, {y})", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 
                        0.5, (0, 255, 0), 1)

        teks = "Faces Detected = " + str(len(faces))
        cv2.putText(framework, teks, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1)

        cv2.imshow("Results", framework)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release Resources
videoCam.release()
cv2.destroyAllWindows()
arduino.close()

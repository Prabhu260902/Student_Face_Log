import face_recognition
import cv2
import csv
import numpy as np
import os
from dum import save_known_encodings, load_known_encodings
from win32com.client import Dispatch
import time
from datetime import datetime,date
import threading




c = ["Name","Data"]
def speak(str1):
    speak=Dispatch(("SAPI.SpVoice"))
    speak.Speak(str1)


def load_known_persons():
    CurrentFolder = os.getcwd()+"/images"
    image_files = [file for file in os.listdir(CurrentFolder) if file.lower().endswith(('.png', '.jpg', '.jpeg'))]
    known_face_encodings = []
    known_face_names = []

    for image_file in image_files:
        person_name = os.path.splitext(image_file)[0]
        image_path = os.path.join(CurrentFolder, image_file)

        image = face_recognition.load_image_file(image_path)
        face_encoding = face_recognition.face_encodings(image)[0]

        known_face_encodings.append(face_encoding)
        known_face_names.append(person_name)

    return known_face_names, known_face_encodings

stop_display = False
def display_frame():
    global stop_display
    while not stop_display:
        ret, frame = video_capture.read()

        cv2.imshow('Video', frame)
        

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("data save")
            stop_display = True

video_capture = cv2.VideoCapture(0)

known_face_names, known_face_encodings = load_known_encodings()

if not known_face_encodings or not known_face_names:
    known_face_names, known_face_encodings = load_known_persons()
    save_known_encodings(known_face_names, known_face_encodings)


face_locations = []
face_encodings = []
face_names = []



display_thread = threading.Thread(target=display_frame)
display_thread.start()

while not stop_display:
    
    ret, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]
        
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    # face_names = []
    
    if(len(face_encodings) > 0):
        face_encoding = face_encodings[0]
        # Example of adjusting the tolerance
        tolerance = 0.5
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=tolerance)

        name = "Unknown"

        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        
        if(name == "Unknown"):
            speak("Not Registered")
        elif((name not in face_names) and (name != "Unknown")):
            ts=time.time()
            date=datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
            timestamp=datetime.fromtimestamp(ts).strftime("%H:%M-%S")

            exist=os.path.isfile("E:\Student_Attendance/attendence/attendance_" + date + ".csv")
            if exist:
                with open("E:\Student_Attendance/attendence/attendance_" + date + ".csv", "+a") as csvfile:
                    writer=csv.writer(csvfile)
                    writer.writerow([name,str(timestamp)])
                csvfile.close()
            else:
                with open("E:\Student_Attendance/attendence/attendance_" + date + ".csv", "+a") as csvfile:
                    writer=csv.writer(csvfile)
                    writer.writerow(c)
                    writer.writerow([name,str(timestamp)])
                csvfile.close()
            speak(name+" Attendence Taken")  
            print(name," taken")
            face_names.append(name)
            speak("next student")  
        else:
            speak("already taken")
            speak("next student")




    if cv2.waitKey(1) & 0xff==ord('q'):   
        print("data save")
        
        stop_display = True
        break


display_thread.join()
video_capture.release()
cv2.destroyAllWindows()

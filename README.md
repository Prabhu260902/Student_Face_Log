# Student Face Attendance Project

## Description

The "Student Face Attendance" project is a Python-based application that utilizes the `face_recognition` library and OpenCV to perform real-time face recognition and attendance tracking. The application captures video from a webcam, detects faces, and matches them with known faces to mark the attendance of recognized students.

## Modules Used

- `face_recognition`: A powerful library for face recognition that provides easy-to-use APIs for face detection and face encoding.
- `cv2` (OpenCV): Used for video capture, image processing, and displaying frames.
- `csv`: Utilized to read and write attendance data in CSV format.
- `numpy`: Required for numerical operations in face recognition.
- `os`: Used to handle file operations and path manipulation.
- `win32com.client`: Utilized to enable text-to-speech functionality.

## Workflow

1. The application initializes by loading the known face encodings and names from the "images" folder using the `load_known_encodings()` function. If no known face encodings are found, the application loads the images from the "images" folder, processes them, and saves the encodings.

2. A separate thread (`display_thread`) is started to continuously display frames from the webcam while the face recognition process is running.

3. The application captures a frame from the webcam, resizes it, and converts it to RGB format to be processed by the `face_recognition` library.

4. The `face_recognition` library is used to find face locations and face encodings in the current frame.

5. If any face encodings are found, the application compares them with the known face encodings with a given tolerance to determine if there's a match. If a match is found, the person's name is retrieved.

6. If the name is "Unknown," the application uses text-to-speech to announce that the person is not registered.

7. If the name is recognized and hasn't already been marked for attendance, the application records the attendance for that person by saving their name and timestamp in a CSV file with the current date as the filename. If the file already exists, the data is appended to it; otherwise, a new CSV file is created.

8. The application then announces that the attendance has been taken for that person and moves on to the next person.

9. The process continues until the user presses the 'q' key, which terminates the attendance marking process, and the data is saved.
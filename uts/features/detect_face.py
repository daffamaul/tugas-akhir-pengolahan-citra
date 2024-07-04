import cv2 as cv
import numpy as np

face_cascade = cv.CascadeClassifier('./detectors/haarcascade_frontalface_default.xml')

def detect_face(image_file):
    image = np.array(image_file.convert('RGB'))
    faces = face_cascade.detectMultiScale(image, 1.01, 2)
    for (x, y, w, h) in faces:
        cv.rectangle(image, (x, y), (x + w, w + h), (255, 0, 0))
    return image, faces
    
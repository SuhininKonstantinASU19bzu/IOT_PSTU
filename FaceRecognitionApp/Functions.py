import os
import cv2
import imutils
import face_recognition as fr
import numpy as np

def CreateEncoding(contents):
    rgbImg = GetRgbImg(contents)
    encImg = fr.face_encodings(rgbImg)[0]

    return encImg


def GetRgbImg(contents):
    buffer = np.fromstring(contents, np.uint8)
    npImg = cv2.imdecode(buffer, cv2.IMREAD_COLOR)
    rgbImg = cv2.cvtColor(npImg, cv2.COLOR_BGR2RGB)

    return rgbImg


def CheckFolder(folder) -> None:
    if not os.path.isdir(folder):
        os.mkdir(folder)


def PeopleCounter(rgbImg):
    return len(fr.face_locations(rgbImg))

def FaceCapture():
    capture = cv2.VideoCapture(0)

    frame = capture.read()
    frame = imutils.resize(frame, width=300)
    scaled = cv2.resize(frame,None, fx=0.5, fy=0.5)
    face_locations = fr.face_locations(scaled)

    for top,right,bottom,left in face_locations:

        cv2.rectangle(scaled,(left, top), (right, bottom), (255,0,0), 3)
            
        top *= 2
        bottom *= 2
        right *= 2
        left *= 2

        faceImg = frame[top:bottom, left:right]

    capture.release()
    cv2.destroyAllWindows()

    return faceImg
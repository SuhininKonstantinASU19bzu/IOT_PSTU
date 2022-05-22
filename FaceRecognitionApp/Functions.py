import os
import cv2
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
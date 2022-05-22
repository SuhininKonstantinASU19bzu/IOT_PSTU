import enum
import os
import sqlite3
import cv2
import face_recognition as fc
import numpy as np
from typing import Dict, List, Tuple
from datetime import datetime as dt
from Functions import *

class UploadedPhotosStatus(enum.Enum):
    processed = 0
    to_process = 1

class FaceIdentifier:
    def __init__(self):
        self._connectiondb = sqlite3.connect("Faces.db")
        self._encodings_dir = os.path.join(os.path.dirname(__file__), "face_encodings")
        self._str_person_encoding = "person_encoding"

        self._frame_resizing = 0.25
        self._known_face_encodings = []
        self._known_face_names = []

        CheckFolder(self._encodings_dir)

        self._load_images()
        self._uploaded_photos_status = UploadedPhotosStatus.processed

    def ExecuteQuery(self, query: str) -> None:

    def GetQueryResult(self, query: str) -> List[Tuple]:

    def SaveEncoding(self, encoding) -> str:

    def ReadEncoding(self, file_path) -> np.ndarray:

    def LoadImages(self):

    def AddPerson(self, name, contents) -> bool:

    def LoadNewImages(self) -> None:

    def DetectKnownFaces(self, contents) -> List[str]:

    def KnownFaces(self):

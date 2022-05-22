import enum
import os
import sqlite3 as database
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
        self._connectiondb = database.connect("Faces.db")
        self._encodings_dir = os.path.join(os.path.dirname(__file__), "face_encodings")
        self._str_person_encoding = "person_encoding"

        self._frame_resizing = 0.25
        self._known_face_encodings = []
        self._known_face_names = []

        CheckFolder(self._encodings_dir)

        self.LoadImages()
        self._uploaded_photos_status = UploadedPhotosStatus.processed

    def ExecuteQuery(self, query: str) -> None:
        cursor = self._connectiondb.cursor()
        cursor.execute(query)
        self._connectiondb.commit()
        cursor.close()

    def GetQueryResult(self, query: str) -> List[Tuple]:
        cursor = self._connectiondb.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        self._connectiondb.commit()
        cursor.close()

        return result

    def SaveEncoding(self, encoding) -> str:
        while os.path.exists(
                file := os.path.join(self._encodings_dir, dt.now().strftime("%Y-%m-%dT%H_%M_%S") + ".npy")
        ):
            pass

        with open(file, "wb") as f:
            np.save(f, encoding)

        return file

    def ReadEncoding(self, file) -> np.ndarray:
        with open(os.path.join(self._encodings_dir, file), 'rb') as f:
            return np.load(f)

    def LoadImages(self):
        self._known_face_names = []
        self._known_face_encodings = []

        for row in self.GetQueryResult(f"SELECT * FROM {self._str_person_encoding}"):
            name = row[0]
            file_path = row[1]

            self._known_face_encodings.append(self.ReadEncoding(file_path))
            self._known_face_names.append(name)

    def AddPerson(self, name, contents) -> bool:

    def LoadNewImages(self) -> None:

    def DetectKnownFaces(self, contents) -> List[str]:

    def KnownFaces(self):

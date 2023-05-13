import face_recognition
import cv2
import numpy as np
from models import Member


class FaceRecognition:
    def __init__(self):
        print("[얼굴인식 모델 로딩]")
        self.known_face_encodings = []
        self.known_face_names = []
        self.load_known_face()

    def load_known_face(self):
        members = Member.objects.all()
        self.known_face_encodings = [np.loads(member.face_encoding) for member in members]
        self.known_face_names = [np.array(member.name) for member in members]

    @staticmethod
    def face_encoding(image):
        face_locations = []
        face_encodings = []

        small_image = cv2.resize(image, (0, 0), fx=0.25, fy=0.25)
        rbg_small_image = np.ascontiguousarray(small_image[:, :, ::-1])
        face_locations = face_recognition.face_locations(rbg_small_image)
        face_encodings = face_recognition.face_encodings(rbg_small_image, face_locations)

        return face_encodings

    def face_recognition(self, image):
        face_encodings = self.face_encoding(image)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            name = "Unknown"

            face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = self.known_face_names[best_match_index]

            face_names.append(name)
            break

        return face_names



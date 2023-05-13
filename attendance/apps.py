from django.apps import AppConfig
from FaceRecognition import FaceRecognition


class AttendanceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'attendance'

    def __init__(self, app_name, app_module):
        super().__init__(app_name, app_module)
        self.face_recognition = None

    def ready(self):
        print("ok")
        self.face_recognition = FaceRecognition()

    def get_face_recognition(self):
        return self.face_recognition

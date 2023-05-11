from django.urls import path

from . import views

urlpatterns = [
    path("members/sign_up", views.sign_up, name="sign_up"),
    path("members/<int:member_id>", views.member_detail, name="member_detail"),
    path("members/all", views.member_all, name="member_all"),
    path("members/makePredictData", views.makePredictData, name="makePredictData"),
    path("face_recognition", views.face_recognition, name="face_recognition"),
]
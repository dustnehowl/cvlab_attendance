import uuid

import boto3
from django.conf import settings
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from rest_framework.decorators import api_view, parser_classes
from rest_framework import serializers
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from attendance.models import Member, Image
from attendance.serializer import MemberSerializer


class S3ImgUploader:
    def __init__(self, file):
        self.file = file
        self.originalName = self.file.name
        self.ext = self.file.name.split(".")[-1]
        self.url = 'cvlab_clock/' + str(uuid.uuid4()) + '.' + self.ext

    def upload(self):
        s3_client = boto3.client(
            's3',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
        )
        s3_client.upload_fileobj(
            self.file,
            settings.AWS_STORAGE_BUCKET_NAME,
            self.url,
            ExtraArgs={
                "ContentType": self.file.content_type
            }
        )
        return self.originalName, self.url


@transaction.atomic()
@api_view(['POST'])
@parser_classes([MultiPartParser])
def sign_up(request):
    data = request.data
    file = data['file']
    name = data['name']
    pin = data['pin']

    s3imgUploader = S3ImgUploader(file)
    originalName, storeFileName = s3imgUploader.upload()
    image = Image(originalFileName=originalName, storeFileName=storeFileName)
    image.save()

    member = Member(name=name, pin=pin, image=image, regist_time=timezone.now())
    member.save()

    return Response({'message': 'File uploaded successfully.'})


@api_view(['GET'])
def member_detail(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    data = {'name': member.name, 'pin': member.pin, 'regist_time': member.regist_time}
    return JsonResponse(data)


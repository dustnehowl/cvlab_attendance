from django.db import models
from django.utils import timezone


# Create your models here.
class Image(models.Model):
    originalFileName = models.CharField(max_length=200)
    storeFileName = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.storeFileName


class Member(models.Model):
    name = models.CharField(max_length=100)
    pin = models.CharField(default="1234", max_length=4)
    image = models.ForeignKey(
        Image,
        on_delete=models.CASCADE,
    )
    regist_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class ClockInOut(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    attendTime = models.DateTimeField(default=timezone.now)


from django.contrib import admin

from attendance.models import Member, Image, ClockInOut

# Register your models here.
admin.site.register(Member)
admin.site.register(Image)
admin.site.register(ClockInOut)

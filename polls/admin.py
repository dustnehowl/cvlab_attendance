from django.contrib import admin

# Register your models here.
from .models import Question, Writer, Choice

admin.site.register(Question)
admin.site.register(Writer)
admin.site.register(Choice)

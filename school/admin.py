from django.contrib import admin
from .models import School, Teacher, Student, Subject

# Register your models here.
admin.site.register(School)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Student)
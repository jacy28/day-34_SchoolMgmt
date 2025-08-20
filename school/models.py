from django.db import models

# Create your models here.
class School(models.Model):
    name=models.CharField(max_length=255)
    address=models.TextField()

    def __str__(self):
        return self.name
    
class Subject(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    name=models.CharField(max_length=200)
    subjects=models.ManyToManyField(Subject, related_name='teachers')

    def __str__(self):
        return self.name
    
class Student(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    school=models.ForeignKey(School, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return f"{self.name} - {self.school.name}"

from rest_framework import viewsets
from .models import School, Teacher, Student, Subject
from .serializers import SchoolSerializer, TeacherSerializer, StudentSerializer, SubjectSerializer

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.prefetch_related('students__school'  )
    serializer_class = SchoolSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.prefetch_related('subjects')
    serializer_class = TeacherSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.select_related('school')
    serializer_class = StudentSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

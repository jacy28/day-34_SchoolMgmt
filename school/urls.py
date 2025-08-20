from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SchoolViewSet, TeacherViewSet, SubjectViewSet, StudentViewSet

router=DefaultRouter()
router.register(r"schools", SchoolViewSet)
router.register(r"teachers", TeacherViewSet)
router.register(r"students", StudentViewSet)
router.register(r"subjects", SubjectViewSet)

urlpatterns=[
    path('', include(router.urls)),
]
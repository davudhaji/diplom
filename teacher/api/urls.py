from rest_framework import routers
from django.urls import path,include
from teacher.api.viewset import *


router = routers.SimpleRouter()
router.register(r'teacher',  TeacherViewSet, basename='template')


urlpatterns = [
    path('', include(router.urls))

]
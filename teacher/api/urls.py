from rest_framework import routers
from django.urls import path,include
from teacher.api.viewset import *


router = routers.SimpleRouter()
router.register(r'teacher',  TeacherViewSet, basename='template')
router.register(r'ixtisas',  IxtisasViewSet, basename='ixtisas')
router.register(r'fen',  FenViewSet, basename='fen')
router.register(r'meqale',  MeqaleViewSet, basename='meqale')
router.register(r'meqale-tipi',  MeqaleTipiViewSet, basename='meqale-tipi')



urlpatterns = [
    path('', include(router.urls))

]

from dataclasses import field
from rest_framework import serializers
from teacher.models import *

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class FenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fen
        fields = '__all__'


class IxtisasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ixtisas
        fields = '__all__'


from dataclasses import field
from rest_framework import serializers
from teacher.models import *

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.update({"elmi_meqalelerin_sayi":instance.meqale_set.count()})
        return data

class FenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fen
        fields = '__all__'


class IxtisasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ixtisas
        fields = '__all__'


class MeqaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meqale
        fields = '__all__'



class MeqaleTipiSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeqaleTipi
        fields = '__all__'


#process of going from python objct to jason

from rest_framework import serializers
from .models import Films

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Films
        fields = ['id', 'name', 'foto', 'description']

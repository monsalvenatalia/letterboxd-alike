from rest_framework import serializers
from .models import Movie
from users.models import Director

class MovieSerializer(serializers.ModelSerializer):
    director_name = serializers.CharField(source='director.name', read_only=True)

    class Meta:
        model= Movie
        fields= [
            'id', 'title', 'slug', 'year', 'genre', 'director', 'director_name', 'synopsis'
        ]

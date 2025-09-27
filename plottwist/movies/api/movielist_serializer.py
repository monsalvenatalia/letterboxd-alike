from rest_framework import serializers
from .models import MovieList
from .movie_serializer import MovieSerializer
from users.api import UserSerializer


class MovieListSerializer(serializers.ModelSerializer):
    
    user= UserSerializer(read_only=True)
    movies= MovieSerializer(many= True, read_only=True)

    class Meta: 
        model= MovieList
        fields= [
            'id', 'user', 'name', 'description', 'movies', 'created_at', 'updated_at'
        ]

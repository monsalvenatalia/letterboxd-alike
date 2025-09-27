from rest_framework import serializers
from .models import Review
from .movie_serializer import MovieSerializer
from users.api import UserSerializer

class ReviewSerializer(serializers.ModelSerializer):
    user= UserSerializer(read_only=True)
    movie= MovieSerializer(read_only=True)

    class Meta:
        model= Review
        fields= [
            'id', 'user', 'movie', 'rating', 'review', 'created_at', 'updated_at'
        ]
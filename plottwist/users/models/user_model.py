from django.contrib.auth.models import AbstractUser
from django.utils.translations import gettext_lazy as _ 
from movies.models import Movie


class User(AbstractUser):

    email = models.EmailField(
        _('Email'),
        unique=True
    )

    avatar= models.ImageField(
        _('Avatar'),
        upload_to="avatars/", 
        blank=True, 
        default="avatars/default.png"
    )

    movies = models.ManyToManyField(
        "movies.Movie",          
        through= "movies.MovieUser",
        related_name= "users", 
        verbose_name= "Watched movies"
    )

    def __str__(self):
        return self.username
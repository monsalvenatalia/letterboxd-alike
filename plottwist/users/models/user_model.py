from django.contrib.auth.models import AbstractUser
from django.utils.translations import gettext_lazy as _ 
from django.db import models


class User(AbstractUser):

    email = models.EmailField(
        _('Email'),
        unique=True
    )

    avatar= models.ImageField(
        _('Avatar'),
        upload_to="avatars/", 
        blank=True, 
        default="default.png"
    )

    movies = models.ManyToManyField(
        "movies.Movie",          
        through= "movies.Review",
        related_name= "users", 
        verbose_name= "Watched movies"
    )

    class Meta:
        ordering= ["email"]
        verbose_name= _("User")
        verbose_name_plural= _("Users")

    def __str__(self):
        return self.username

    
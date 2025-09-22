from django.db import models

from django.utils.translations import gettext_lazy as _ 
import datetime

def current_year():
    return datetime.date.today().year

def maximum_value(value):
    if value > current_year():
        raise ValidationError("This year has not arrived yet")

class Movie(models.Model):

    class Genre(models.TextChoices):
        ACTION= 'AC', 'Action'
        COMEDY= 'CO', 'Comedy'
        DRAMA= 'DR', 'Drama'
        HORROR= 'HO', 'Horror'
        ROMANCE= 'RO', 'Romance'
        SCIENCE_FICTION= 'SF', 'Science Fiction'
        ANIMATION= 'AN', 'Animation'
        DOCUMENTARY= 'DO', 'Documentary'
        MUSICAL= 'MU', 'Musical'
        THRILLER= 'TH', 'Thriller'

    title = models.CharField(
        _("Title"), 
        max_length= 250, 
        unique= True
    )

    slug = models.SlugField(
        _('Slug'), 
        max_length= 250, 
        unique= True
    )

    year = models.PositiveIntegerField(
        _('Release Year'), 
        blank= True, 
        null= True,
        validators=[MinValueValidator(1888), maximum_value]
    )

    genre = models.CharField(
        _('Genre'),
        max_length= 2, 
        choices= Genre, 
        blank= True, 
        null= True
    )

    synopsis = models.TextField(
        _('Synopsis'), 
        blank= True
    )

    def __str__(self):
        return self.title


class MovieUser(models.Model):

    user = models.ForeignKey(
        _('User'),
        on_delete= models.CASCADE
    )

    movie = models.ForeignKey(
        _('Movie'),
        on_delete= models.CASCADE
    )

    watched = models.BooleanField(
        default= False
    )

    rating = models.PositiveSmallIntegerField(
        _('Rating'),
        null= True,
        blank= True, 
        validators= [MinValueValidator(1), MaxValueValidator(5)]
    )

    class Meta:
        unique_together = ('user', 'movie')  




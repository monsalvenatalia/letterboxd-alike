from django.db import models

from django.utils.translations import gettext_lazy as _ 


class Review(models.Model):

    user = models.ForeignKey(
        "users.User", 
        verbose_name= _('User'),
        related_name= "reviews",
        on_delete= models.CASCADE
    )

    movie = models.ForeignKey(
        "movies.Movie", 
        verbose_name= _('Movie'),
        related_name= "reviews",
        on_delete= models.CASCADE
    )

    rating = models.PositiveSmallIntegerField(
        verbose_name= _('Rating'),
        blank= True, 
        validators= [MinValueValidator(1), MaxValueValidator(5)]
    )

    review = models.TextField(
        verbose_name= _('Review'),
        blank= True, 
        max_length= 8000, 
        help_text= _('The review length must not exceed 8000 characters')
    )

    created_at = models.DateTimeField(
        auto_now_add= True
    )

    updated_at = models.DateTimeField(
        auto_now= True
    )

    class Meta:
        constraints= [
            models.UniqueConstraint(
                fields=["user", "movie"], 
                name= "unique_user_movie_review"
            )
        ]
        ordering = ["-created_at"]
        verbose_name= _("Review")
        verbose_name_plural= _("Reviews")
    
    def __str__(self):
        return f"{self.user} - {self.movie} ({self.rating}/5)"




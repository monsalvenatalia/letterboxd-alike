from django.db import models

from django.utils.translations import gettext_lazy as _ 

 class MovieList(models.Model):
    user = models.ForeignKey(
        "users.User",
        verbose_name=_("User"),
        related_name="movie_lists",
        on_delete=models.CASCADE
    )

    name = models.CharField(
        max_length=100,
        verbose_name=_("List name")
    )

    description = models.TextField(
        blank=True,
        verbose_name=_("Description")
    )

    movies = models.ManyToManyField(
        "Movie",
        related_name="in_lists",
        verbose_name=_("Movies"),
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Movie list"
        verbose_name_plural = "Movie lists"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} ({self.user})"
   
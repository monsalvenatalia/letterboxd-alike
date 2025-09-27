from django.contrib import admin
from .models import Movie, Review, MovieList

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "year", "genre", "director"]
    list_filter = ["genre", "year", "director"]
    search_fields = ["title", "director__name", "genre"]
    prepopulated_fields= {"slug":("title",)}
    ordering = ["title", "year"]

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["user", "movie", "rating", "created_at"]
    list_filter = ["rating", "user"]
    search_fields = ["user__username", "movie__title"]
    ordering = ["-created_at"]

@admin.register(MovieList)
class MovieListAdmin(admin.ModelAdmin):
    list_display = ["name", "user", "created_at", "updated_at"]
    search_fields = ["name", "user__username"]
    filter_horizontal = ("movies",)  # Para que sea cómodo seleccionar películas
    ordering = ["name", "-created_at"]

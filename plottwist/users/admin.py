from django.contrib import admin
from .models import User, Director

admin.site.register(User, UserAdmin)

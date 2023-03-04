from django.contrib import admin
from .models import Recipe, AboutPage, HomePage

admin.site.register([Recipe, AboutPage, HomePage])

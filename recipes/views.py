from django.shortcuts import render
from .models import Recipe, AboutPage, HomePage


def home(request):
    # Retrieve the HomePage object and its related Recipe objects
    home_page = HomePage.objects.first()
    recipes = home_page.recipes.all()

    # Render the home page template with the home_page and recipes data
    return render(request, 'recipes/index.html', {'home_page': home_page, 'recipes': recipes})


def about(request):
    # Retrieve the AboutPage object
    about_page = AboutPage.objects.first()

    # Render the about page template with the about_page data
    return render(request, 'recipes/about.html', {'about_page': about_page})

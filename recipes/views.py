from django.shortcuts import render


def index(request):
    return render(request, 'recipes/index.html')


def about(request):
    return render(request, 'recipes/about.html')


def apple_cake_recipe(request):
    return render(request, 'recipes/apple_cake_recipe.html')


def carrot_cake_recipe(request):
    return render(request, 'recipes/carrot_cake_recipe.html')


def pumpkin_cake_recipe(request):
    return render(request, 'recipes/pumpkin_cake_recipe.html')

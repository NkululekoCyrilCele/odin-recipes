from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('apple-cake-recipe/', views.apple_cake_recipe, name='apple_cake_recipe'),
    path('carrot-cake-recipe/', views.carrot_cake_recipe,
         name="carrot_cake_recipe"),
    path('pumpkin-cake-recipe/', views.pumpkin_cake_recipe,
         name='pumpkin_cake_recipe'),
]

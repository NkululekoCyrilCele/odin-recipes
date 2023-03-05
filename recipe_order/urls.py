from django.urls import path
from . import views
from . import api_views

urlpatterns = [
    path('', views.recipe_order, name='recipe_order'),
    path('login/', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('recipe-items/', api_views.RecipeOrderView.as_view(),
         name='recipe_item_list'),
    path('recipe-items/<int:pk>',
         api_views.SingleRecipeOrderView.as_view(), name='recipe_detail'),
]

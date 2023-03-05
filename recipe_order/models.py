from django.db import models


class RecipeOrder(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    recipe_type = models.CharField(max_length=50)
    frosting_type = models.CharField(max_length=50)
    delivery_date = models.DateField()
    quantity = models.IntegerField()

from rest_framework import generics
from .models import RecipeOrder
from .serializers import RecipeOrderSerializer


class RecipeOrderView(generics.ListCreateAPIView):
    queryset = RecipeOrder.objects.all()
    serializer_class = RecipeOrderSerializer


class SingleRecipeOrderView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RecipeOrder.objects.all()
    serializer_class = RecipeOrderSerializer

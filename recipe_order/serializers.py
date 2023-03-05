from rest_framework import serializers
from .models import RecipeOrder
import bleach
from rest_framework.validators import UniqueTogetherValidator, UniqueValidator


class RecipeOrderSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()

    class Meta:
        model = RecipeOrder
        fields = ['id', 'name', 'email', 'recipe_type',
                  'frosting_type', 'delivery_date', 'quantity']
        extra_kwargs = {
            'recipe_type': {'required': True},
            'frosting_type': {'required': True},
            'delivery_date': {'required': True},
            'quantity': {'required': True},
            'email': {
                'validators': [
                    UniqueValidator(
                        queryset=RecipeOrder.objects.all()
                    )
                ]
            },
            'recipe_type': {
                'validators': [
                    UniqueTogetherValidator(
                        queryset=RecipeOrder.objects.all(),
                        fields=('name', 'recipe_type')
                    )
                ]
            },
        }

    def to_representation(self, instance):
        instance.name = bleach.clean(instance.name)
        instance.email = bleach.clean(instance.email)
        return super().to_representation(instance)

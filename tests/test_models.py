from django.test import TestCase
from datetime import date
from recipe_order.models import RecipeOrder
from django.core.exceptions import ValidationError


class RecipeOrderTestCase(TestCase):
    def setUp(self):
        self.order = RecipeOrder.objects.create(
            name='John Doe',
            email='johndoe@example.com',
            recipe_type='Chocolate Cake',
            frosting_type='Buttercream',
            delivery_date=date(2022, 12, 24),
            quantity=2,
        )

    def test_order_has_correct_string_representation(self):
        expected_string = 'Chocolate Cake'
        self.assertEqual(str(self.order), expected_string)

    def test_order_is_ordered_by_recipe_type(self):
        order1 = RecipeOrder.objects.create(
            name='Jane Doe',
            email='janedoe@example.com',
            recipe_type='Vanilla Cake',
            frosting_type='Cream Cheese',
            delivery_date=date(2022, 12, 25),
            quantity=1,
        )
        order2 = RecipeOrder.objects.create(
            name='Jack Smith',
            email='jacksmith@example.com',
            recipe_type='Carrot Cake',
            frosting_type='Cream Cheese',
            delivery_date=date(2022, 12, 23),
            quantity=1,
        )
        expected_order = [order2, self.order, order1]
        self.assertQuerysetEqual(
            RecipeOrder.objects.all(),
            expected_order,
            transform=lambda x: x,
            ordered=True,
        )

    def test_order_email_field_is_valid(self):
        invalid_email_order = RecipeOrder(
            name='John Smith',
            email='johnsmithexample.com',
            recipe_type='Chocolate Cake',
            frosting_type='Buttercream',
            delivery_date=date(2022, 12, 24),
            quantity=2,
        )
        with self.assertRaises(ValidationError):
            invalid_email_order.full_clean()

    def test_order_quantity_field_is_valid(self):
        valid_quantity_order = RecipeOrder.objects.create(
            name='John Smith',
            email='johnsmith@example.com',
            recipe_type='Chocolate Cake',
            frosting_type='Buttercream',
            delivery_date=date(2022, 12, 24),
            quantity=2,
        )
        valid_quantity_order.full_clean()

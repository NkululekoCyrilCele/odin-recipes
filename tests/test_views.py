from datetime import date
from recipe_order.serializers import RecipeOrderSerializer
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from django.contrib.auth import authenticate, login
from recipe_order.forms import RecipeOrderForm, LoginForm
from recipe_order.models import RecipeOrder
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse


class AppleCakeRecipeViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_apple_cake_recipe_view_GET(self):
        response = self.client.get(reverse('apple_cake_recipe'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/apple_cake_recipe.html')

    def test_apple_cake_recipe_view_contains_ingredients(self):
        response = self.client.get(reverse('apple_cake_recipe'))
        self.assertContains(response, 'flour')
        self.assertContains(response, 'sugar')
        self.assertContains(response, 'eggs')

    def test_apple_cake_recipe_view_does_not_contain_wrong_ingredients(self):
        response = self.client.get(reverse('apple_cake_recipe'))
        self.assertNotContains(response, 'chocolate chips')
        self.assertNotContains(response, 'spinach')
        self.assertNotContains(response, 'mushrooms')


class CarrotCakeRecipeViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_carrot_cake_recipe_view_GET(self):
        response = self.client.get(reverse('carrot_cake_recipe'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/carrot_cake_recipe.html')

    def test_carrot_cake_recipe_view_contains_ingredients(self):
        response = self.client.get(reverse('carrot_cake_recipe'))
        self.assertContains(response, 'carrots')
        self.assertContains(response, 'flour')
        self.assertContains(response, 'sugar')
        self.assertContains(response, 'eggs')

    def test_carrot_cake_recipe_view_does_not_contain_wrong_ingredients(self):
        response = self.client.get(reverse('carrot_cake_recipe'))
        self.assertNotContains(response, 'chocolate chips')
        self.assertNotContains(response, 'spinach')
        self.assertNotContains(response, 'mushrooms')


class PumpkinCakeRecipeViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_pumpkin_cake_recipe_view_GET(self):
        response = self.client.get(reverse('pumpkin_cake_recipe'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/pumpkin_cake_recipe.html')

    def test_pumpkin_cake_recipe_view_contains_ingredients(self):
        response = self.client.get(reverse('pumpkin_cake_recipe'))
        self.assertContains(response, 'pumpkin')
        self.assertContains(response, 'flour')
        self.assertContains(response, 'sugar')
        self.assertContains(response, 'eggs')

    def test_pumpkin_cake_recipe_view_does_not_contain_wrong_ingredients(self):
        response = self.client.get(reverse('pumpkin_cake_recipe'))
        self.assertNotContains(response, 'chocolate chips')
        self.assertNotContains(response, 'spinach')
        self.assertNotContains(response, 'mushrooms')


class RecipeOrderViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.url = reverse('recipe_order')

    def test_get_request(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], RecipeOrderForm)
        self.assertTemplateUsed(response, 'recipe_order/order_form.html')

    def test_post_request_valid_form(self):
        data = {
            'name': 'Test User',
            'email': 'testuser@example.com',
            'recipe_type': 'Chocolate Cake',
            'frosting_type': 'Buttercream',
            'delivery_date': '2023-03-10',
            'quantity': 1,
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe_order/thankyou.html')
        self.assertContains(
            response, 'We have received your order and will process it shortly.')
        self.assertEqual(RecipeOrder.objects.count(), 1)
        order = RecipeOrder.objects.first()
        self.assertEqual(order.name, 'Test User')
        self.assertEqual(order.email, 'testuser@example.com')
        self.assertEqual(order.recipe_type, 'Chocolate Cake')
        self.assertEqual(order.frosting_type, 'Buttercream')
        self.assertEqual(str(order.delivery_date), '2023-03-10')
        self.assertEqual(order.quantity, 1)

    def test_post_request_invalid_form(self):
        data = {
            'name': '',
            'email': 'testuser@example.com',
            'recipe_type': '',
            'frosting_type': 'Buttercream',
            'delivery_date': '2023-03-10',
            'quantity': -1,
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe_order/order_form.html')
        self.assertIsInstance(response.context['form'], RecipeOrderForm)
        self.assertContains(response, 'This field is required.', count=2)
        self.assertEqual(RecipeOrder.objects.count(), 0)


class LoginViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('login')
        self.user = User.objects.create_user(
            username='testuser', password='testpass123')
        self.form_data = {'username': 'testuser', 'password': 'testpass123'}
        self.invalid_form_data = {
            'username': 'testuser', 'password': 'wrongpass'}

    def test_login_view(self):
        response = self.client.post(self.url, self.form_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('recipe_order'))

        response = self.client.post(self.url, self.invalid_form_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid username or password.')

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

        response = self.client.get(self.url)
        form = response.context['form']
        self.assertIsInstance(form, LoginForm)


class LogoutViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('logout')
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass'
        )

    def test_logout(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertRedirects(response, reverse('login'))
        self.assertFalse('_auth_user_id' in self.client.session)


class RegistrationViewTestCase(TestCase):

    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.valid_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword',
        }

    def test_register(self):
        response = self.client.post(self.register_url, data=self.valid_data)

        self.assertRedirects(response, self.login_url,
                             status_code=302, target_status_code=200)

        self.assertTrue(User.objects.filter(
            username=self.valid_data['username']).exists())

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]), 'Your account has been created. You can now log in.')

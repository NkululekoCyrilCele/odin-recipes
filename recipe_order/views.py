from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegistrationForm, RecipeOrderForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='/recipe_order/login')
def recipe_order(request):
    if request.method == 'POST':
        form = RecipeOrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            cart, created = Cart.objects.get_or_create(user=request.user)
            cart.items.add(order)
            messages.success(
                request, 'Your order has been added to your cart.')
            return render(request, 'recipe_order/thankyou.html')
    else:
        form = RecipeOrderForm()
    return render(request, 'recipe_order/order_form.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('recipe_order')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(
                request, 'Your account has been created. You can now log in.')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

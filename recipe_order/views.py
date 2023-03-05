from django.shortcuts import render
from .forms import RecipeOrderForm


def recipe_order(request):
    if request.method == 'POST':
        form = RecipeOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'recipe_order/thankyou.html')
    else:
        form = RecipeOrderForm()
    return render(request, 'recipe_order/order_form.html', {'form': form})

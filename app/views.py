from django.shortcuts import redirect, render
from .models import Food, Store
from .forms import FoodForm


def food_list(request):
    foods = Food.objects.all()
    return render(request, 'app/food_list.html', {'foods': foods, 'form': FoodForm()})


def create_food(request):
    form = FoodForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('food_list')
    return redirect('food_list')


def store_list(request):
    stores = Store.objects.all()
    print(stores)
    return render(request, 'app/store_list.html', {'stores': stores})

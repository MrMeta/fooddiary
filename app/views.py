from django.shortcuts import render
from .models import Food
from .forms import FoodForm


def food_list(request):
    foods = Food.objects.all()
    return render(request, 'app/food_list.html', {'foods': foods, 'form': FoodForm()})

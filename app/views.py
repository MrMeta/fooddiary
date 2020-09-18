from django.shortcuts import get_object_or_404, redirect, render
from .models import Food, FoodReview, Store
from .forms import FoodForm, StoreForm, FoodReviewForm


def food_list(request):
    foods = Food.objects.all().order_by('-created_date')
    return render(request, 'app/food_list.html', {'foods': foods, 'form': FoodForm()})


def create_food(request):
    form = FoodForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('food_list')
    return redirect('food_list')


def food_detail(request, food_id):
    food = get_object_or_404(Food, pk=food_id)
    reviews = FoodReview.objects.filter(food=food_id).order_by('-created_date')
    return render(request, 'app/food_detail.html', {'food': food, 'reviews': reviews, 'form': FoodReviewForm()})


def store_list(request):
    stores = Store.objects.all()
    return render(request, 'app/store_list.html', {'stores': stores, 'form': StoreForm()})


def create_store(request):
    form = StoreForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('store_list')
    return redirect('store_list')


def create_review(request, food_id):
    form = FoodReviewForm(data=request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.food_id = food_id
        review.save()
        return redirect('food_detail', food_id)
    return redirect('food_detail', food_id)


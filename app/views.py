from django.shortcuts import render


def food_list(request):
    return render(request, 'app/food_list.html', {})
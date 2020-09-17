from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve
from app.views import food_list


class FoodListTest(TestCase):

    def test_root_url_resolves_to_food_list_view(self):
        found = resolve('/')
        self.assertEqual(found.func, food_list)

    def test_food_list_returns_correct_html(self):
        request = HttpRequest()
        response = food_list(request)
        self.assertTrue(response.content.startswith(b'\n<html>'))
        self.assertTrue(response.content.endswith(b'</html>\n'))
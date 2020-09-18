from django.test import TestCase
from app.models import Food


class FoodListTest(TestCase):

    def test_uses_list_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'app/food_list.html')

    def test_passes_correct_food_list(self):
        Food.objects.bulk_create([
            Food(name='베이컨 베스트 토스트'),
            Food(name='햄 치즈 토스트'),
        ])
        response = self.client.get('/')
        self.assertEqual(list(response.context['foods']), list(Food.objects.all()))


class CreateFoodTest(TestCase):

    def test_redirect_if_form_is_invalid(self):
        response = self.client.post(
            '/create',
            data={'description': 'test'},
        )
        self.assertRedirects(response, '/')

    def save_food_if_form_is_invalid(self):
        response = self.client.post(
            '/create',
            data={'name': 'food', 'description': 'test'},
        )
        new_item = Food.objects.first()
        self.assertEqual(new_item.name, 'food')
        self.assertEqual(new_item.description, 'test')

    def test_redirect_if_form_is_valid(self):
        response = self.client.post(
            '/create',
            data={'name': 'food', 'description': 'test'},
        )
        self.assertRedirects(response, '/')
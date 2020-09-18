from django.test import TestCase
from app.forms import (
    FoodForm,
    FoodReviewForm,
    REQUIRED_ERROR_MESSAGE,
)


class FoodFormTest(TestCase):

    def test_from_validates_required_items(self):
        form = FoodForm(data={'name': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], [REQUIRED_ERROR_MESSAGE])


class FoodReviewFormTest(TestCase):

    def test_validates_that_title_is_input(self):
        form = FoodReviewForm(data={'content': 'hihihihihi'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['title'], [REQUIRED_ERROR_MESSAGE])

    def test_validates_that_content_is_input(self):
        form = FoodReviewForm(data={'title': 'hihihihi'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['content'], [REQUIRED_ERROR_MESSAGE])
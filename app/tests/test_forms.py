from django.test import TestCase
from app.forms import (
    FoodForm,
    REQUIRED_ERROR_MESSAGE,
)


class FoodFormTest(TestCase):

    def test_from_validates_required_items(self):
        form = FoodForm(data={'name': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], [REQUIRED_ERROR_MESSAGE])

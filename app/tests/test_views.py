from unittest.case import skip

from django.utils import timezone

from fooddiary.test import TestCase

from app.models import Store, Food, FoodReview


class TestStoreViewSet(TestCase):
    def test_list(self):
        Store.objects.create(name='Store #1', address='Address #1')
        Store.objects.create(name='Store #2', address='Address #2')
        Store.objects.create(name='Store #3', address='Address #3', deleted_date=timezone.now())

        res = self.client.get('/stores/')

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data['count'], 2)

        for item in res.data['results']:
            with self.subTest(key=item['id']):
                store = Store.objects.get(pk=item['id'])
                self.assertEqual(item['name'], store.name)
                self.assertEqual(item['address'], store.address)

    def test_retrieve(self):
        store = Store.objects.create(name='Store #1', address='Address #1')

        res = self.client.get(f'/stores/{store.id}/')

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data['name'], store.name)
        self.assertEqual(res.data['address'], store.address)

    def test_return_404_if_retrieve_non_existent_store(self):
        res = self.client.get('/stores/1/')

        self.assertEqual(res.status_code, 404)

    def test_return_404_if_retrieve_deleted_store(self):
        Store.objects.create(name='Store #1', address='Address #1', deleted_date=timezone.now())

        res = self.client.get('/stores/1/')

        self.assertEqual(res.status_code, 404)

    def test_create(self):
        data = {
            'name': 'Store #1',
            'address': 'Address #1',
        }

        res = self.client.post('/stores/', data=data)

        store = Store.objects.first()

        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.data['name'], store.name)
        self.assertEqual(res.data['address'], store.address)

    def test_partial_update(self):
        data = {'address': 'New Address'}
        store = Store.objects.create(name='Store #1', address='Address #1')

        res = self.client.patch(f'/stores/{store.id}/', data=data)

        store.refresh_from_db()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data['address'], data['address'])

    def test_return_404_if_partial_update_non_existent_store(self):
        data = {'address': 'New Address'}

        res = self.client.patch('/stores/1/', data=data)

        self.assertEqual(res.status_code, 404)

    def test_return_404_if_partial_update_undeleted_store(self):
        data = {'address': 'New Address'}
        Store.objects.create(name='Store #1', address='Address #1', deleted_date=timezone.now())

        res = self.client.patch('/stores/1/', data=data)

        self.assertEqual(res.status_code, 404)

    def test_update_api_returns_405(self):
        data = {'address': 'New Address'}

        res = self.client.put('/stores/1/', data=data)

        self.assertEqual(res.status_code, 405)

    def test_destroy(self):
        store = Store.objects.create(name='Store #1', address='Address #1')
        res = self.client.delete(f'/stores/{store.id}/')

        self.assertEqual(res.status_code, 204)

        store.refresh_from_db()

        self.assertIsNotNone(store.created_date)

    def test_return_404_if_delete_non_existent_store(self):
        res = self.client.delete('/stores/1/')

        self.assertEqual(res.status_code, 404)

    def test_return_404_if_delete_undeleted_store(self):
        store = Store.objects.create(
            name='Store #1',
            address='Address #1',
            deleted_date=timezone.now(),
        )
        res = self.client.delete(f'/stores/{store.id}/')

        self.assertEqual(res.status_code, 404)


class TestFoodViewSet(TestCase):
    def test_list(self):
        store = Store.objects.create(name='Store #1', address='Address #1')
        Food.objects.create(store=store, name='Food #1')
        Food.objects.create(store=store, name='Food #2')
        Food.objects.create(
            store=store,
            name='Food #3',
            deleted_date=timezone.now(),
        )

        res = self.client.get('/foods/')

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data['count'], 2)

        for item in res.data['results']:
            with self.subTest(key=item['id']):
                food = Food.objects.get(pk=item['id'])

                self.assertEqual(item['name'], food.name)
                self.assertEqual(item['store']['name'], store.name)

    def test_retrieve(self):
        store = Store.objects.create(name='Store #1', address='Address #1')
        food = Food.objects.create(store=store, name='Food #1')

        res = self.client.get(f'/foods/{food.id}/')

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data['name'], food.name)
        self.assertEqual(res.data['store']['name'], store.name)

    def test_return_404_if_retrieve_non_existent_food(self):
        res = self.client.get('/foods/1/')

        self.assertEqual(res.status_code, 404)

    def test_return_404_if_retrieve_deleted_food(self):
        store = Store.objects.create(name='Store #1', address='Address #1')
        food = Food.objects.create(
            store=store,
            name='Food #1',
            deleted_date=timezone.now(),
        )

        res = self.client.get(f'/foods/{food.id}/')

        self.assertEqual(res.status_code, 404)

    def test_return_404_if_retrieve_food_of_deleted_store(self):
        store = Store.objects.create(
            name='Store #1',
            address='Address #1',
            deleted_date=timezone.now(),
        )
        food = Food.objects.create(store=store, name='Food #1')

        res = self.client.get(f'/foods/{food.id}/')

        self.assertEqual(res.status_code, 404)

    def test_create(self):
        store = Store.objects.create(name='Store #1', address='Address #1')
        data = {
            'name': 'Food #1',
            'description': 'hmm',
            'store_id': store.id,
        }

        res = self.client.post('/foods/', data=data)

        food = Food.objects.first()

        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.data['name'], food.name)

    def test_return_400_if_create_food_of_deleted_store(self):
        store = Store.objects.create(
            name='Store #1',
            address='Address #1',
            deleted_date=timezone.now(),
        )
        data = {
            'name': 'Food #1',
            'store_id': store.id,
        }

        res = self.client.post('/foods/', data=data)

        self.assertEqual(res.status_code, 400)

    def test_partial_update(self):
        store = Store.objects.create(name='Store #1', address='Address #1')
        new_store = Store.objects.create(name='Store #1', address='Address #1')
        food = Food.objects.create(name='Store #1', store=store)
        data = {
            'description': 'hmm',
            'store_id': new_store.id,
        }

        res = self.client.patch(f'/foods/{food.id}/', data=data)

        food.refresh_from_db()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data['description'], data['description'])
        self.assertEqual(res.data['store_id'], data['store_id'])

    def test_return_404_if_partial_update_non_existent_food(self):
        data = {'description': 'hmm'}

        res = self.client.patch('/foods/1/', data=data)

        self.assertEqual(res.status_code, 404)

    def test_return_404_if_partial_update_deleted_food(self):
        store = Store.objects.create(name='Store #1', address='Address #1')
        data = {'address': 'New Address'}
        food = Food.objects.create(
            store=store,
            name='Food #1',
            deleted_date=timezone.now(),
        )

        res = self.client.patch(f'/foods/{food.id}/', data=data)

        self.assertEqual(res.status_code, 404)

    def test_return_404_if_partial_update_food_of_deleted_store(self):
        store = Store.objects.create(
            name='Store #1',
            address='Address #1',
            deleted_date=timezone.now(),
        )
        food = Food.objects.create(store=store, name='Food #1')
        data = {'address': 'New Address'}

        res = self.client.patch(f'/foods/{food.id}/', data=data)

        self.assertEqual(res.status_code, 404)

    @skip('To implement')
    def test_return_404_if_partial_update_food_to_belong_to_deleted_store(self):
        store = Store.objects.create(
            name='Store #1',
            address='Address #1',
        )
        new_store = Store.objects.create(
            name='Store #2',
            address='Address #2',
            deleted_date=timezone.now(),
        )
        data = {
            'address': 'New Address',
            'store_id': new_store.id,
        }
        food = Food.objects.create(store=store, name='Food #1')

        res = self.client.patch(f'/foods/{food.id}/', data=data)

        self.assertEqual(res.status_code, 404)

    def test_update_api_returns_405(self):
        data = {'address': 'New Address'}

        res = self.client.put('/foods/1/', data=data)

        self.assertEqual(res.status_code, 405)

    def test_destroy(self):
        store = Store.objects.create(name='Store #1', address='Address #1')
        food = Food.objects.create(store=store, name='Food #1')

        res = self.client.delete(f'/foods/{food.id}/')

        self.assertEqual(res.status_code, 204)

        food.refresh_from_db()

        self.assertIsNotNone(food.created_date)

    def test_return_404_if_delete_non_existent_food(self):
        res = self.client.delete('/foods/1/')

        self.assertEqual(res.status_code, 404)

    def test_return_404_if_delete_deleted_food(self):
        store = Store.objects.create(name='Store #1', address='Address #1')
        food = Food.objects.create(
            store=store,
            name='Food #1',
            deleted_date=timezone.now(),
        )

        res = self.client.delete(f'/foods/{food.id}/')

        self.assertEqual(res.status_code, 404)

    def test_return_404_if_delete_food_of_deleted_store(self):
        store = Store.objects.create(
            name='Store #1',
            address='Address #1',
            deleted_date=timezone.now(),
        )
        food = Food.objects.create(store=store, name='Food #1')

        res = self.client.delete(f'/foods/{food.id}/')

        self.assertEqual(res.status_code, 404)


class TestFoodReviewViewSet(TestCase):
    def test_list(self):
        store = Store.objects.create(name='Store #1', address='Address #1')
        food = Food.objects.create(name='Food #1', description='hmm', store=store)
        FoodReview.objects.create(food=food, title='Title #1', content='hmm')
        FoodReview.objects.create(food=food, title='Title #2', content='hmm')
        FoodReview.objects.create(
            food=food,
            title='Title #2',
            content='hmm',
            deleted_date=timezone.now(),
        )

        res = self.client.get('/food-reviews/')

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data['count'], 2)

        for item in res.data['results']:
            with self.subTest(key=item['id']):
                food_review = FoodReview.objects.get(pk=item['id'])

                self.assertEqual(item['title'], food_review.title)
                self.assertEqual(item['food']['name'], food.name)

    def test_retrieve(self):
        store = Store.objects.create(name='Store #1', address='Address #1')
        food = Food.objects.create(name='Food #1', description='hmm', store=store)
        food_review = FoodReview.objects.create(food=food, title='Title #1', content='hmm')

        res = self.client.get(f'/food-reviews/{food_review.id}/')

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data['title'], food_review.title)
        self.assertEqual(res.data['food']['name'], food.name)

    def test_return_404_if_retrieve_non_existent_review(self):
        res = self.client.get('/food-reviews/1/')

        self.assertEqual(res.status_code, 404)

    def test_return_404_if_retrieve_deleted_review(self):
        store = Store.objects.create(name='Store #1', address='Address #1')
        food = Food.objects.create(name='Food #1', description='hmm', store=store)
        food_review = FoodReview.objects.create(
            food=food,
            title='Title #1',
            content='hmm',
            deleted_date=timezone.now(),
        )

        res = self.client.get(f'/food-reviews/{food_review.id}/')

        self.assertEqual(res.status_code, 404)

    def test_return_404_if_retrieve_review_for_deleted_food(self):
        store = Store.objects.create(name='Store #1', address='Address #1')
        food = Food.objects.create(
            store=store,
            name='Food #1',
            description='hmm',
            deleted_date=timezone.now(),
        )
        food_review = FoodReview.objects.create(
            food=food,
            title='Title #1',
            content='hmm',
        )

        res = self.client.get(f'/food-reviews/{food_review.id}/')

        self.assertEqual(res.status_code, 404)

    def test_create(self):
        store = Store.objects.create(name='Store #1', address='Address #1')
        food = Food.objects.create(
            store=store,
            name='Food #1',
            description='hmm',
        )
        data = {
            'title': 'Title #1',
            'content': 'hmm',
            'food_id': food.id,
        }

        res = self.client.post('/food-reviews/', data=data)

        food_review = FoodReview.objects.first()

        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.data['title'], food_review.title)

    def test_return_400_if_create_review_for_deleted_food(self):
        store = Store.objects.create(
            name='Store #1',
            address='Address #1',
        )
        food = Food.objects.create(
            store=store,
            name='Food #1',
            description='hmm',
            deleted_date=timezone.now(),
        )
        data = {
            'name': 'Food #1',
            'food_id': food.id,
        }

        res = self.client.post('/food-reviews/', data=data)

        self.assertEqual(res.status_code, 400)

    def test_partial_update(self):
        store = Store.objects.create(name='Store #1', address='Address #1')
        food = Food.objects.create(name='Store #1', store=store)
        new_food = Food.objects.create(name='Store #2', store=store)
        food_review = FoodReview.objects.create(food=food, title='Title #1', content='hmm')
        data = {
            'title': 'Title #2',
            'content': 'hmm.....',
            'food_id': new_food.id,
        }

        res = self.client.patch(f'/food-reviews/{food_review.id}/', data=data)

        food_review.refresh_from_db()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data['title'], data['title'])
        self.assertEqual(res.data['content'], data['content'])
        self.assertEqual(res.data['food_id'], data['food_id'])

    def test_return_404_if_partial_update_non_existent_review(self):
        data = {'content': 'hmm'}

        res = self.client.patch('/food-reviews/1/', data=data)

        self.assertEqual(res.status_code, 404)

    def test_return_404_if_partial_update_deleted_review(self):
        store = Store.objects.create(name='Store #1', address='Address #1')
        food = Food.objects.create(store=store, name='Food #1')
        food_review = FoodReview.objects.create(
            food=food,
            title='Title #1',
            content='hmm',
            deleted_date=timezone.now(),
        )
        data = {'content': 'hmm'}

        res = self.client.patch(f'/food-reviews/{food_review.id}/', data=data)

        self.assertEqual(res.status_code, 404)

    def test_return_404_if_partial_update_review_for_deleted_food(self):
        store = Store.objects.create(name='Store #1', address='Address #1')
        food = Food.objects.create(
            store=store,
            name='Food #1',
            deleted_date=timezone.now(),
        )
        food_review = FoodReview.objects.create(
            food=food,
            title='Title #1',
            content='hmm',
        )
        data = {'content': 'hmm'}

        res = self.client.patch(f'/food-reviews/{food_review.id}/', data=data)

        self.assertEqual(res.status_code, 404)

    @skip('To implement')
    def test_return_404_if_partial_update_review_to_belong_to_deleted_food(self):
        store = Store.objects.create(name='Store #1', address='Address #1')
        food = Food.objects.create(
            store=store,
            name='Food #1',
        )
        new_food = Food.objects.create(
            store=store,
            name='Food #1',
            deleted_date=timezone.now(),
        )
        data = {
            'content': 'hmm',
            'store_id': new_food.id,
        }
        food_review = FoodReview.objects.create(food=food, title='Title #1', content='hmm')

        res = self.client.patch(f'/food-reviews/{food_review.id}/', data=data)

        self.assertEqual(res.status_code, 404)

    def test_update_api_returns_405(self):
        data = {'content': 'hmm'}

        res = self.client.put('/food-reviews/1/', data=data)

        self.assertEqual(res.status_code, 405)

    def test_destroy(self):
        store = Store.objects.create(name='Store #1', address='Address #1')
        food = Food.objects.create(store=store, name='Food #1')
        food_review = FoodReview.objects.create(
            food=food,
            title='Title #1',
            content='hmm',
        )

        res = self.client.delete(f'/food-reviews/{food_review.id}/')

        self.assertEqual(res.status_code, 204)

        food_review.refresh_from_db()

        self.assertIsNotNone(food_review.deleted_date)

    def test_return_404_if_delete_non_existent_review(self):
        res = self.client.delete('/food-reviews/1/')

        self.assertEqual(res.status_code, 404)

    def test_return_404_if_delete_deleted_review(self):
        store = Store.objects.create(name='Store #1', address='Address #1')
        food = Food.objects.create(store=store, name='Food #1')
        food_review = FoodReview.objects.create(
            food=food,
            title='Title #1',
            content='hmm',
            deleted_date=timezone.now(),
        )

        res = self.client.delete(f'/food-reviews/{food_review.id}/')

        self.assertEqual(res.status_code, 404)

    def test_return_404_if_delete_review_for_deleted_food(self):
        store = Store.objects.create(name='Store #1', address='Address #1')
        food = Food.objects.create(
            store=store,
            name='Food #1',
            deleted_date=timezone.now(),
        )
        food_review = FoodReview.objects.create(
            food=food,
            title='Title #1',
            content='hmm',
        )

        res = self.client.delete(f'/food-reviews/{food_review.id}/')

        self.assertEqual(res.status_code, 404)



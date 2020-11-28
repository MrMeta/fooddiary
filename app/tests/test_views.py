from django.utils import timezone

from fooddiary.test import TestCase

from app.models import Store


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

    def test_return_404_if_partial_update_non_existent_store(self):
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

class TestFoodViewSet(TestCase):
    def test_list(self):
        pass

    def test_retrieve(self):
        pass

    def test_create(self):
        pass

    def test_cannot_create_if_store_does_not_exist(self):
        pass

    def test_partial_update(self):
        pass

    def test_update_api_returns_405(self):
        pass

    def test_delete(self):
        pass


class TestFoodReviewViewSet(TestCase):
    def test_list(self):
        pass

    def test_retrieve(self):
        pass

    def test_create(self):
        pass

    def test_cannot_create_if_food_does_not_exist(self):
        pass

    def test_partial_update(self):
        pass

    def test_update_api_returns_405(self):
        pass

    def test_delete(self):
        pass

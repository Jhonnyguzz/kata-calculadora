from django.contrib.auth.models import User
from django.test import TestCase, Client

# Create your tests here.
from .models import Image, Portfolio, Product
import json

# Create your tests here.
class GalleryTestCase(TestCase):

    def test_list_images_status(self):
        url = '/gallery/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_count_images_list(self):
        user_model = User.objects.create_user(username='test', password='kd8wke-DE34', first_name='test', last_name='test', email='test@test.com')
        Image.objects.create(name='nuevo', url='No', description='testImage', type='jpg', user=user_model)
        Image.objects.create(name='nuevo2', url='No', description='testImage', type='jpg', user=user_model)

        response=self.client.get('/gallery/')
        current_data=json.loads(response.content)
        print(current_data)
        self.assertEqual(len(current_data),2)

    def test_verify_first_from_images_list(self):
        user_model = User.objects.create_user(username='test', password='kd8wke-DE34', first_name='test', last_name='test', email='test@test.com')
        Image.objects.create(name='nuevo', url='No', description='testImage', type='jpg', user=user_model)
        Image.objects.create(name='nuevo2', url='No', description='testImage', type='jpg', user=user_model)

        response=self.client.get('/gallery/')
        current_data=json.loads(response.content)

        self.assertEqual(current_data[0]['fields']['name'],"nuevo")

    def test_list_user_portfolios(self):
        user_model = User.objects.create_user(username='test', password='kd8wke-DE34', first_name='test',
                                              last_name='test', email='test@test.com')
        portfolio_1 = Portfolio.objects.create(user=user_model)
        image_1 = Image.objects.create(name='nuevo', url='No', description='testImage', type='jpg', user=user_model)
        Product.objects.create(image=image_1, portfolio=portfolio_1)
        user_model_2 = User.objects.create_user(username='test2', password='kd8wke-DE34', first_name='test2',
                                              last_name='test2', email='test2@test.com')
        portfolio_2 = Portfolio.objects.create(user=user_model_2)
        image_2 = Image.objects.create(name='nuevo', url='No', description='testImage', type='jpg', user=user_model_2)
        Product.objects.create(image=image_2, portfolio=portfolio_2)

        response = self.client.get('/gallery/listPortfolio/')
        current_data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEquals(len(current_data), 2)

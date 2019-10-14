from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.core import serializers

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

    def test_informacion_usuario(self):
        url = '/gallery/addUser/'
        data = {"username":"user1235", "first_name": "John", "last_name":"Doe", "password":"asdfasdf", "email":"john@hotmail.com"}
        to_json = json.dumps(data)
        response = self.client.post(path=url, data=to_json, content_type="json", format="json")
        current_data = json.loads(response.content)
        element = current_data[0]['fields']
        
        self.assertEquals(element['username'], "user1235")
        self.assertEquals(element['first_name'], "John")
        self.assertEquals(element['last_name'], "Doe")
        self.assertEquals(element['email'], "john@hotmail.com")

    def test_get_public_information(self):
        user_model = User.objects.create_user(username='test', password='kd8wke-DE34', first_name='test',
                                              last_name='test', email='test@test.com')
        portfolio_1 = Portfolio.objects.create(user=user_model)
        image_1 = Image.objects.create(name='nuevo', url='No', description='testImage', type='jpg', user=user_model)
        image_2 = Image.objects.create(name='nuevo2', url='No', description='testImage', type='jpg', user=user_model)
        Product.objects.create(image=image_1, portfolio=portfolio_1)
        Product.objects.create(image=image_2, portfolio=portfolio_1, private=False)
        token = Token.objects.create()
        response = self.client.get('/gallery/userPublicData/?{}'.format(user_model.id))
        self.assertEqual(response.status_code, 200)
        current_data = json.loads(response.content)
        self.assertEquals(len(current_data["portfolio"]["products"]), 1)
        self.assertEquals(current_data["portfolio"]["products"][0].image, image_2)


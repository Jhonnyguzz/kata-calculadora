from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from .models import Image, Portfolio, Product
import json


# Create your views here.
@csrf_exempt
def index(request):
    images_list = Image.objects.all()
    return HttpResponse(serializers.serialize("json", images_list))


@csrf_exempt
def add_user_view(request):
    if request.method == 'POST':
        json_user = json.loads(request.body)
        username = json_user['username']
        first_name = json_user['first_name']
        last_name = json_user['last_name']
        password = json_user['password']
        email = json_user['email']

        user_model = User.objects.create_user(username=username, password=password)
        user_model.first_name = first_name
        user_model.last_name = last_name
        user_model.email = email
        user_model.save()
    return HttpResponse(serializers.serialize("json", [user_model]))


@csrf_exempt
def update_user_view(request):
    if request.method == 'PATCH':
        json_user = json.loads(request.body)
        user_id = json_user.pop('id')
        user_model = User.objects.filter(id=user_id).update(**json_user)
        return HttpResponse(serializers.serialize("json", [user_model]))


@csrf_exempt
def login_user_view(request):
    user_data = json.loads(request.body)
    user_model = authenticate(**user_data)
    if user_model is not None:
        login(request, user_model)
        return HttpResponse(serializers.serialize("json", [user_model]))
    else:
        return HttpResponse({'status': 'invalid credentials'})


@csrf_exempt
def list_products(request):
    if request.method == 'GET':
        return HttpResponse(serializers.serialize("json", Portfolio.objects.all()))

@csrf_exempt
def view_portfolio(request, id):
    if request.method == 'GET':
        products = []
        response = {"portfolio":{"products":products}}

        portfolios = Portfolio.objects.filter(user_id=id)
        for portfolio in portfolios:
            public_products = Product.objects.filter(portfolio=portfolio, private=False)
            for product in public_products:
                products.append({"image_name":product.image.name})
            break
        return JsonResponse(response)
    
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addUser/', views.add_user_view, name='addUser'),
    path('updateUser/', views.update_user_view, name='updateUser'),
    path('login/', views.login_user_view, name='login'),
    path('listPortfolio/', views.list_products, name='listPortfolio'),
]

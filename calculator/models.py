from django.db import models

# Create your models here.


def calculadora(param:str):
    return 0 if param == "" else len(param.split(","))

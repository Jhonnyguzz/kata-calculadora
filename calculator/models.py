from django.db import models

# Create your models here.


def calculadora(param: str):
    if param == "":
        return [0,0]
    else:
        list_of_numbers = [float(str_number) for str_number in param.split(",")]
        return [len(list_of_numbers)]

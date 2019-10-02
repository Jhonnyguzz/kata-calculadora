from django.test import TestCase

# Create your tests here.
from calculator.models import calculadora


class CalculadoraTest(TestCase):
    def test_iteracion_1c1(self):
        self.assertEquals(calculadora(""), 0)

    def test_iteracion_1c2(self):
        self.assertEquals(calculadora("1"), 1)

    def test_iteracion_1c3(self):
        self.assertEquals(calculadora("1,2"), 2)

    def test_iteracion_1c4(self):
        self.assertEquals(calculadora("1,2,3,4,5,6,6,8"), 8)
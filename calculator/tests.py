from unittest import TestCase

# Create your tests here.
from calculator.models import calculadora


class CalculadoraTest(TestCase):
    def test_iteracion_1c1(self):
        arr = calculadora("")
        self.assertEquals(arr[0], 0)

    def test_iteracion_1c2(self):
        arr = calculadora("1")
        self.assertEquals(arr[0], 1)

    def test_iteracion_1c3(self):
        arr = calculadora("1,2")
        self.assertEquals(arr[0], 2)

    def test_iteracion_1c4(self):
        arr = calculadora("1,2,3,4,5,6,6,8")
        self.assertEquals(arr[0], 8)

    def test_iteracion_2c1(self):
        arr = calculadora("")
        self.assertEquals(arr[0], 0)
        self.assertEquals(arr[1], 0)

    def test_iteracion_2c2(self):
        arr = calculadora("1")
        self.assertEquals(arr[0], 1)
        self.assertEquals(arr[1], 1)

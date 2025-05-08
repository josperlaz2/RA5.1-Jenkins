# test_calculadora.py
import unittest
from calculadora import multiplicar

class TestCalculadora(unittest.TestCase):

    def test_multiplicar_positivos(self):
        self.assertEqual(multiplicar(2, 3), 6)

    def test_multiplicar_negativos(self):
        self.assertEqual(multiplicar(-2, 3), -6)
        self.assertEqual(multiplicar(-2, -3), 6)

    def test_multiplicar_cero(self):
        self.assertEqual(multiplicar(5, 0), 0)
        self.assertEqual(multiplicar(0, -3), 0)

    def test_multiplicar_decimales(self):
        self.assertEqual(multiplicar(2.5, 2), 5.0)
        self.assertEqual(multiplicar(1.5, 0.5), 0.75)

    def test_multiplicar_mixtos(self):
        self.assertEqual(multiplicar(-1.5, 4), -6.0)

if __name__ == '__main__':
    unittest.main()

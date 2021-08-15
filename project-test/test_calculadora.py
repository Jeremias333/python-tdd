from unittest import TestCase, main
from calculadora import soma

class TestCalculadora(TestCase):
    def test_soma_5_e_5_deve_retornar_10(self):
        self.assertEqual(soma(5,5), 10)

    def test_soma_5_negativo_e_5_deve_retornar_0(self):
        self.assertEqual(soma(-5, 5), 0)

    def test_soma_varias_entradas(self):
        x_y_saidas = (
            (10, 10, 20),
            (15, 10, 25),
            (1, 2, 3),
            (-10, 10, 0),
            (10, 20, 30),
            (3.5, 0.5, 4),
            (15, -15, 0),
        )
        
        for x_y_saidas in x_y_saidas:
            with self.subTest(x_y_saidas=x_y_saidas):
                x, y, saida = x_y_saidas
                self.assertEqual(soma(x, y), saida)

    def test_soma_x_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(TypeError):
            soma('11', 0)

    def test_soma_y_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(TypeError):
            soma(11, '0')
main(verbosity=2)
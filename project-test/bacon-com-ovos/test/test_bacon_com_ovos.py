try:
    import sys
    import os
    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__), '../src'
            )
        )
    )
except:
    raise

from unittest import TestCase, main
from bacon_com_ovos import bacon_com_ovos
"""
TDD - Test Driven Development (Desenvolvimento dirigido a testes)

Red
Parte 1 -> crirar o teste e ver falhar


Green
Parte 2 -> Criar o código e ver o teste passar

Refactor
parte 3 -> Melhorar o código

"""

class TesteBaconComOvos(TestCase):
    def test_bacon_com_ovos_deve_levantar_assertion_error_se_nao_receber_int(self):
        with self.assertRaises(AssertionError):
            bacon_com_ovos("")
    
    def test_bacon_com_ovos_deve_retornar_bacon_com_ovos_se_entrada_for_multiplo_de_3_e_5(self):
        entradas = (15, 30, 45, 60)
        saida = "Bacon com ovos"
        
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada),
                    saida,
                    msg=f"{entrada} não retornou {saida}"
                )
    
    def test_bacon_com_ovos_deve_retornar_bacon_se_entrada_for_multiplo_de_3(self):
        entradas = (3, 6, 9, 12, 18)
        saida = "Bacon"
        
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada),
                    saida,
                    msg=f"{entrada} não retornou {saida}"
                )
    
    def test_bacon_com_ovos_deve_retornar_ovos_se_entrada_for_multiplo_de_5(self):
        entradas = (10, 50, 25)
        saida = "Ovos"
        
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada),
                    saida,
                    msg=f"{entrada} não retornou {saida}"
                )

    def test_bacon_com_ovos_deve_retornar_passa_fome_se_entrada_nao_for_multiplo_de_3_e_5(self):
        entradas = (1, 2, 4, 8)
        saida = "Passa fome"
        
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada),
                    saida,
                    msg=f"{entrada} não retornou {saida}"
                )

if __name__ == "__main__":
    main(verbosity=2)
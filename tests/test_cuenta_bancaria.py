import sys
import os
import unittest

 
# Agrega el directorio 'src' al path de Python para poder importar 'cuenta_bancaria'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import cuenta_bancaria
from cuenta_bancaria import CuentaBancaria 

class TestCalcular(unittest.TestCase):
    # Todo Adiciona tus pruebas unitarias aquí.
    # Ejemplo:   
    # def test_suma(self):
    #     valor_esperado = 3
    #     valor_actual = calcular(1, 2, '+')
    #     self.assertEqual(valor_esperado, valor_actual)

    def setUp(self):
        self.cuenta = cuenta_bancaria.CuentaBancaria("Juan Pérez", "123456789", 1000.0)


    def test_ingresar(self):
        self.cuenta.ingresar(500.0)
        self.assertEqual(self.cuenta.get_saldo(), 1500.0)
        self.cuenta.ingresar(-100.0)
        self.assertEqual(self.cuenta.get_saldo(), 1500.0)  # No debería cambiar

    def test_retirar(self):
        self.cuenta.retirar(200.0)
        self.assertEqual(self.cuenta.get_saldo(), 800.0)
        self.cuenta.retirar(900.0)
        self.assertEqual(self.cuenta.get_saldo(), 800.0)  # No debería cambiar
    


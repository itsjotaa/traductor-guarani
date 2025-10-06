# -*- coding: utf-8 -*-
from translator.traductor import traducir

def test_traduccion_simple ():
    # prueba básica
    entrada = "yo comer comida"
    salida_esperada = "che karu tembi’u"
    assert traducir(entrada) == salida_esperada
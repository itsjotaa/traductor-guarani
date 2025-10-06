# -*- coding: utf-8 -*-
from translator import diccionario

def traducir(oracion):
    palabras_es = oracion.lower().split()
    traduccion = []

    for p in palabras_es:
        if p in diccionario.palabras:
            traduccion.append(diccionario.palabras[p])
        elif p in diccionario.Verbos:
            traduccion.append(diccionario.Verbos[p])
        elif p in diccionario.Adjetivos:
            traduccion.append(diccionario.Adjetivos[p])
        elif p in diccionario.Pronombres:
            traduccion.append(diccionario.Pronombres[p])
        else:
            traduccion.append(p)
    
    return " ".join(traduccion)



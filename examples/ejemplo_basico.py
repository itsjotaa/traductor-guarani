# -*- coding: utf-8 -*-
from translator.traductor import traducir

def probar_interactivo():
    print("Escribe el texto a traducir del Espanol al Guarani")
    print("Escribe 'salir' para cerrar el programa")

    while True:
        texto = input("Escribe texto en Espanol: ")

        if texto.lower() == "salir":
            print("Saliendo")
            break
        if texto.split():
            resultado = traducir(texto)
            print(f"Guarani: {resultado}\n")
        else:
            print("El texto no es valido\n")

if __name__ == "__main__":
    probar_interactivo()

# -*- coding: utf-8 -*-
import requests

def probar_api_interactivo ():
    print("Probando API del traductor")
    print("Asegurate de ejecutar primero examples/api_basica.py")
    print("Escribe 'salir' para terminar la aplicacion\n")

    while True:
        texto = input("Texto a traducir: ")

        if texto.lower() == "salir":
            print("Saliendo del programa")
            break

        try:
            response = requests.post(
                "http://localhost:5000/translate",
                json={"text": texto}
            )
            if response.status_code == 200:
                data = response.json()
                print(f" Original: {data['original']}")
                print(f" Traducido: {data['traducido']}")
            else:
                print(f" Error: {response.status_code}): {response.json()}\n")

        except Exception as e:
            print(f" No se pudo conectar a la API: {e}")
            print(" Ejecutaste la API en otra terminal?\n")

if __name__ == "__main__":
    probar_api_interactivo()
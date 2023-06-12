palabra= input("Ingrese su palabra a verificar: ")

def palindromo(palabra):
    palabra = palabra.lower()
    if palabra == palabra[::-1]:
        print(f"La palabra {palabra.title()}, es un palindromo")
    else:
        print(f"Esta palabra {palabra.title()} no es un palindromo")
palindromo(palabra)
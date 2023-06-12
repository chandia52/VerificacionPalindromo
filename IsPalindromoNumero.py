numero = int(input("Ingrese su numero a verificar: "))
def isPalindromo(numero):
    if str(numero)[::-1] == str(numero):
        print(f"El numero {numero} es un palindromo")
    else:
        print(f"El numero {numero} no es un palindromo")

isPalindromo(numero)
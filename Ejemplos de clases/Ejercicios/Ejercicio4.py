posicion = int(input("Escribe la posición"))
Longitud = int(input("Escribe la longitud"))
Frase = str(input("Escribe la frase"))

Frase2 = Frase[posicion:posicion+Longitud]

print(f"resultado {Frase2}")
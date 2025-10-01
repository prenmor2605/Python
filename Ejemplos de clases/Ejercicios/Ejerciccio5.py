
frase = input("Pon la frase")
Letraremplazar = input("Pon la letra")
Letraponer = input("Pon la letra")

Contador = frase.count(Letraremplazar)
Remplazo = frase.replace(Letraremplazar, Letraponer)

print (f"{Contador} apariciones, {Remplazo}")
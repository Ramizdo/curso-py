buscar = 3

for numero in range(5):
    print(numero)
    if numero == buscar:
        print("Numero encontrado", buscar)
        break
else:
    print("No se encontro el numero buscado")

for char in "Ultimate Python":
    print(char)

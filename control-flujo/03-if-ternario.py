edad = input("Que edad tienes? ")

edad = int(edad)

mensaje = "Es mayor" if edad > 17 else "Es menor"

""" if edad > 17:
    mensaje = "Es mayor"     # Es otra forma valida de hacerlo
else:
    mensaje = "Es menor" """

print(mensaje)

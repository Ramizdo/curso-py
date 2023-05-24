def hola(nombre, apellido, edad):
    print("Hola mundo")
    print(f"Bienvenido {nombre} {apellido}")
    print(f"Tu edad es: {edad}")


hola("Douglas", "Ramirez", "32")

# Asi se pasan parametros opcionales


def hola2(nombre, apellido="Perez"):
    print("Hola mundo")
    print(f"Bienvenido {nombre} {apellido}")


hola2("Douglas")

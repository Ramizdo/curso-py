print("""
      Bienvenidos a la calculadora,
      Para salir de aqui escribe: Salir,
      Las operaciones son: suma, resta, multi, divi
      """)

numero1 = ""  # String vacio se evalua en Falso
while True:
    if not numero1:  # Esto evalua en falso
        numero1 = input("Ingrese el primer numero: ")
        if numero1.lower() == "salir":
            break
    numero1 = int(numero1)
    operador = input("Que operacion desea realizar: ")
    if operador.lower() == "salir":
        break
    numero2 = input("Ingrese el segundo numero: ")
    if numero2.lower() == "salir":
        break
    numero2 = int(numero2)

    if operador.lower() == "suma":
        numero1 += numero2
        # print("El resultado de la suma es:", numero1)
    elif operador.lower() == "resta":
        numero1 -= numero2
        # print("El resultado de la resta es:", numero1)
    elif operador.lower() == "multi":
        numero1 *= numero2
        # print("El resultado de la multiplicacion es:", numero1)
    elif operador.lower() == "divi":
        numero1 /= numero2
        # print("El resultado de la division es:", numero1)
    else:
        print("Operacion no valida")
        break
    print(f"El resultado de la {operador} es: {numero1}\n")

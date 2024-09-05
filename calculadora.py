number1=int(input("Pon un numero:"))
number2=int(input("Pon otro numero:"))

elección = 0

while elección != 6:
    print("""
    Indique la operación a realizar:
    1) Suma
    2) Resta
    3) Multiplicación
    4) División
    5) Cambio de valores
    6) Salir
    """)

    elección = int(input())

    if elección == 1:
        print(" ")
        print("Resultado: ", number1, "+", number2, "=", number1+number2)

    if elección == 2:
        print(" ")
        print("Resultado: ", number1, "-", number2, "=", number1-number2)
    
    if elección == 3:
        print("")
        print("Resultado: ", number1, "x", number2, "=", number1*number2)

    if elección == 4:
        print("")
        print("Resultado: ", number1, "/", number2, "=", number1/number2)

    if elección == 5:
        number1=int(input("Pon un numero:"))
        number2=int(input("Pon otro numero:"))

    if elección == 6:
        print("Gracias por usar la calculadora de putos peruana.")
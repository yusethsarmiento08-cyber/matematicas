# Algoritmo CalculoGeometrico

def menu():
    opcion = 0

    while opcion != 4:

        print("CALCULADORA GEOMÉTRICA")
        print("1. Figuras planas")
        print("2. Sólidos regulares")
        print("3. Sólido irregular")
        print("4. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:

            print("FIGURAS PLANAS")
            print("1. Rectángulo")
            print("2. Triángulo")
            print("3. Círculo")
            print("4. Cuadrado")

            figura = int(input("Seleccione una figura: "))

            if figura == 1:

                base = int(input("Ingrese la base del rectángulo: "))
                altura = int(input("Ingrese la altura del rectángulo: "))

                perimetro = 2 * (base + altura)
                area = base * altura

                print("Perímetro:", perimetro)
                print("Área:", area)

            elif figura == 2:

                lado1 = int(input("Ingrese el lado 1 del triángulo: "))
                lado2 = int(input("Ingrese el lado 2 del triángulo: "))
                lado3 = int(input("Ingrese el lado 3 del triángulo: "))
                base = int(input("Ingrese la base del triángulo: "))
                altura = int(input("Ingrese la altura del triángulo: "))

                perimetro = lado1 + lado2 + lado3
                area = (base * altura) / 2

                print("Perímetro:", perimetro)
                print("Área:", area)

            elif figura == 3:

                Pi = 3.1416
                radio = int(input("Ingrese el radio del círculo: "))

                perimetro = 2 * Pi * radio
                area = Pi * radio * radio

                print("Perímetro:", perimetro)
                print("Área:", area)

            elif figura == 4:

                lado = int(input("Ingrese el lado del cuadrado: "))

                perimetro = 4 * lado
                area = lado * lado

                print("Perímetro:", perimetro)
                print("Área:", area)

            else:
                print("Figura no válida")

        elif opcion == 2:

            print("SÓLIDOS REGULARES")
            print("Esta parte será realizada por el otro integrante.")

        elif opcion == 3:

            volumen_inicial = int(input("Ingrese el volumen inicial: "))
            volumen_final = int(input("Ingrese el volumen final: "))

            volumen = volumen_final - volumen_inicial

            print("Volumen del sólido irregular:", volumen)

        elif opcion == 4:

            print("Programa finalizado")

        else:

            print("Opción inválida")


menu()


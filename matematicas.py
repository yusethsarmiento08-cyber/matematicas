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
            print("1. Cubo")
            print("2. Prisma")
            print("3. Cilindro")
            print("4. Esfera")
            print("5. Cono")

            figura = int(input("Seleccione un sólido regular: "))

            if figura == 1:

                cubeLado = int(input("Ingrese el lado del cubo: "))
                cubeVolume = cubeLado * 3

                print("Volumen:", cubeVolume)

            elif figura == 2:

                prismLargo = int(input("Ingrese el largo del prisma: "))
                prismAncho = int(input("Ingrese el ancho del prisma: "))
                prismAlto = int(input("Ingrese el alto del prisma: "))

                prismVolume = prismLargo * prismAncho * prismAlto

                print("Volumen del prisma:", prismVolume)

            elif figura == 3:

                Pi = 3.1416
                cilinderRadio = int(input("Ingrese el radio del cilindro: "))
                cilinderAlto = int(input("Ingrese la altura del cilindro: "))

                cilinderVolume = Pi * cilinderRadio * 2 * cilinderAlto

                print("Volumen del cilindro:", cilinderVolume)

            elif figura == 4:

                Pi = 3.1416
                sphereRadio = int(input("Ingrese el radio de la esfera: "))

                sphereVolume = (4 * Pi * sphereRadio * 3) / 3

                print("Volumen de la esfera:", sphereVolume)

            elif figura == 5:

                Pi = 3.1416
                coneRadio = int(input("Ingrese el radio del cono: "))
                coneAlto = int(input("Ingrese la altura del cono: "))

                coneVolume = (Pi * coneRadio * 2 * coneAlto) / 3

                print("Volumen del cono:", coneVolume)

            else:
                print("Sólido no válido")

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

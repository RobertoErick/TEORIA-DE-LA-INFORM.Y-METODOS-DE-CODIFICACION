#   Principio de inclusión-exclusión
#   Tecnica de conteo para calcular la interaccion de varios elementos que cumplen al menos una de varias propiedades

#Funcion para 2 valores y sus interacciones
def inclusion_exclusion_2():
    A = int(input("Ingrese el primer valor (A): "))
    B = int(input("Ingrese el segundo valor (B): "))
    A_B = int(input("Ingrese el valor de la intersección (A∩B): "))
    union = A + B - A_B
    print("\n|A|  +  |B|  -  |A∩B|  =  |A∪B|")
    print(A, " + ", B, " - ", A_B, " = ", union)
    return union

#Funcion para 3 valores y sus interacciones
def inclusion_exclusion_3():
    A = int(input("Ingrese el primer valor (A): "))
    B = int(input("Ingrese el segundo valor (B): "))
    C = int(input("Ingrese el tercer valor (C): "))
    A_B = int(input("Ingrese el valor de la intersección (A∩B): "))
    A_C = int(input("Ingrese el valor de la intersección (A∩C): "))
    B_C = int(input("Ingrese el valor de la intersección (B∩C): "))
    A_B_C = int(input("Ingrese el valor de la intersección triple (A∩B∩C): "))
    print("\n|A|  +  |B|  +  |C|  -  |A∩B|  -  |A∩C|  -  |B∩C|  +  |A∩B∩C|  =  |A∪B∪C|")
    union = A + B + C - (A_B + A_C + B_C) + A_B_C
    print(A, " + ", B, " + ", C, " - (", A_B, " + ", A_C, " + ", B_C, " ) + ", A_B_C, " = ", union)
    return union

print("================================\nPrincipio de inclusión-exclusión\n================================")
print("Tecnica de conteo para calcular la interaccion de varios elementos que cumplen al menos una de varias propiedades")
print("Escoja una de las siguientes opciones:")
decision = int(input("1) Problema con dos datos a ingresar \n2) Problema con tres datos a ingresar \nIngrese la opción del número: "))

if decision == 1:
    print("\nPrincipio de inclusión-exclusión con 2 datos:")
    resultado = inclusion_exclusion_2()
    print(f"\nTamaño de la unión de A y B: {resultado} \n")
elif decision == 2:
    print("Principio de inclusión-exclusión con 3 datos:")
    resultado = inclusion_exclusion_3()
    print(f"\nTamaño de la unión de A, B y C: {resultado} \n")
else:
    print("Opción no válida.")

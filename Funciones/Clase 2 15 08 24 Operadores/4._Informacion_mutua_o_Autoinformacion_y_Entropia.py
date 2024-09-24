#   Informacion mutua o Autoinformacion
#   Cuantifica la dependencia entre la distribución conjunta de X e Y y la que tendrían si X e Y fuesen independientes

#   Entropia
#   Medida de la incertidumbre o de la cantidad de información requerida para describir una variable. Se define como la suma, para cada símbolo, de la probabilidad de ese símbolo por el logaritmo base dos de uno entre la probabilidad de ese símbolo.

import numpy as np
import math

#   Funcion que vamos a usar cuando el problema se seleccione sea cuantificable
def cuantificables():
    #   Total de Informacion mutua o autoinformacion
    Total_I_E = 0
    #   Total de Entropia
    Total_H_E = 0
    #   Matriz que vamos a usar
    matriz = np.array([
    ["  P(E)    ", "    I(E)    ", "    H(E)    "]
    ])
    #   A partir de la respuesta va a calcular la cantidad de filas que ingrese
    N = int(input("¿Cual es la cantidad del espacio muestral?: ")) 
    for i in range(N):
        P_E = float(input(f"Ingresa la probabilidad de la fila {i+1} P(E): "))
        I_E = -math.log10(P_E)
        H_E = P_E * I_E
        Total_I_E += I_E
        Total_H_E += H_E
        nueva_fila = np.array([P_E, I_E, H_E])
        #   Se agrega a la fila a la matriz
        matriz = np.append(matriz, [nueva_fila], axis=0)
    #   Una vez terminadas todas las filas, la suma de de I_E y H_E se agregan a la matriz
    ultima_fila = np.array(["       ", Total_I_E, Total_H_E])
    matriz = np.append(matriz, [ultima_fila], axis=0)
    print(matriz)

#   Funcion que vamos a usar cuando el problema se seleccione sea transmision de datos binaria
def transmision_de_datos_binaria():
    #   Total de Informacion mutua o autoinformacion
    Total_I_E = 0
    #   Total de Entropia
    Total_H_E = 0
    #   Matriz que vamos a usar
    matriz = np.array([
    ["  P(E)    ", "    I(E)    ", "    H(E)    "]
    ])
    N = int(input("¿Cual es la cantidad del espacio muestral?: ")) 
    for i in range(N):
        P_E = float(input(f"Ingresa la probabilidad de la fila {i+1} P(E): "))
        I_E = -math.log2(P_E)
        H_E = P_E * I_E
        Total_I_E += I_E
        Total_H_E += H_E
        nueva_fila = np.array([P_E, I_E, H_E])
        #   Se agrega a la fila a la matriz
        matriz = np.append(matriz, [nueva_fila], axis=0)
    #   Una vez terminadas todas las filas, la suma de de I_E y H_E se agregan a la matriz
    ultima_fila = np.array(["       ", Total_I_E, Total_H_E])
    matriz = np.append(matriz, [ultima_fila], axis=0)
    print(matriz)

#   Funcion que vamos a usar cuando el problema se seleccione sea transmision entre estados
def transmision_entre_estados(matriz_2, Total_I_E, Total_H_E):
    #   Total de Informacion mutua o autoinformacion
    Total_I_E = 0
    #   Total de Entropia
    Total_H_E = 0
    #   Matriz que vamos a usar
    matriz_2 = np.array([
    ["  Estados ","  P(E)    ", "    I(E)    ", "    H(E)    "]
    ])
    N = int(input("¿Cual es la cantidad del espacio muestral?: ")) 
    for i in range(N):
        E = float(input(f"Ingresa los estados posibles en la fila {i+1}: "))
        P_E = float(input(f"Ingresa la probabilidad de la fila {i+1} P(E): "))
        I_E = -np.log(P_E) * E
        H_E = P_E * I_E
        Total_I_E += I_E
        Total_H_E += H_E
        nueva_fila = np.array([E, P_E, I_E, H_E])
         #   Se agrega a la fila a la matriz
        matriz = np.append(matriz_2, [nueva_fila], axis=0)
    #   Una vez terminadas todas las filas, la suma de de I_E y H_E se agregan a la matriz
    ultima_fila = np.array(["       ", Total_I_E, Total_H_E])
    matriz = np.append(matriz, [ultima_fila], axis=0)
    print(matriz)

print("====================================")
print("Informacion mutua o Autoinformacion")
print("             Entropia               ")
print("===================================\n")
print("Seleccione el tipo de proceso")
Opcion = int(input("1) Cuantificables (hartleys/simbolo) \n2) Transmision de datos binaria (bits/simbolo) \n3) Transmision entre estados (nats/simbolo) \nSelección: "))

if Opcion == 1:
    print("\nCuantificables\n")
    cuantificables()
elif Opcion == 2:
    print("\nTransmision de datos binaria\n")
    transmision_de_datos_binaria()
elif Opcion == 3:
    print("\nTransmision entre estados\n")
    transmision_entre_estados()
else:
    print("\nOpcion no valida\n")
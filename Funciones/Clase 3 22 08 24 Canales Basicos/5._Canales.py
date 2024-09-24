import itertools

def generar_secuencias(longitud, alfabeto):
    """
    Genera todas las posibles secuencias de una longitud dada usando un alfabeto.
    
    :param longitud: La longitud de las secuencias.
    :param alfabeto: El alfabeto que se usará para generar las secuencias.
    :return: Lista de secuencias posibles.
    """
    return [''.join(seq) for seq in itertools.product(alfabeto, repeat=longitud)]

def calcular_nA_nB(L, alfabeto_entrada, alfabeto_salida):
    """
    Calcula las secuencias posibles para A y B y sus respectivos tamaños (nA y nB).
    
    :param L: Longitud de las secuencias (cantidad de caracteres agrupados).
    :param alfabeto_entrada: Alfabeto proporcionado por el usuario para A.
    :param alfabeto_salida: Alfabeto proporcionado por el usuario para B.
    :return: Diccionario con secuencias A, secuencias B, nA y nB.
    """
    # Generar secuencias para A y B
    secuencias_A = generar_secuencias(L, alfabeto_entrada)
    secuencias_B = generar_secuencias(L, alfabeto_salida)
    
    # Calcular nA y nB
    nA = len(secuencias_A)
    nB = len(secuencias_B)
    
    # Retornar resultados
    return {
        "A": secuencias_A,
        "B": secuencias_B,
        "nA": nA,
        "nB": nB
    }

def mostrar_resultados(resultados):
    """
    Muestra las secuencias generadas y la cantidad de combinaciones.
    
    :param resultados: Diccionario con los resultados calculados.
    """
    print(f"\nSecuencias de entrada (A) generadas:")
    print(', '.join(resultados["A"]))
    
    print(f"\nSecuencias de salida (B) generadas:")
    print(', '.join(resultados["B"]))
    
    print(f"\nNúmero de combinaciones (nA): {resultados['nA']}")
    print(f"Número de combinaciones (nB): {resultados['nB']}\n")

# Solicitar los valores al usuario
L = int(input("Ingresa el valor de L (longitud de las secuencias): "))
alfabeto_entrada = input("Ingresa los caracteres del alfabeto de entrada separados por comas: ").split(',')
alfabeto_salida = input("Ingresa los caracteres del alfabeto de salida separados por comas: ").split(',')

# Calcular las secuencias y tamaños de nA y nB
resultados = calcular_nA_nB(L, alfabeto_entrada, alfabeto_salida)

# Mostrar los resultados
mostrar_resultados(resultados)

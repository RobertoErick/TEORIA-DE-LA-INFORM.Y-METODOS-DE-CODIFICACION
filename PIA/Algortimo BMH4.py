import numpy as np

def faoso_search(text, pattern, max_errors):
    """
    Implementa el algoritmo FAOSO para buscar un patrón en un texto permitiendo hasta max_errors errores.
    """
    n = len(text)
    m = len(pattern)

    # Crear una matriz de distancia de edición
    dist_matrix = np.zeros((n + 1, m + 1), dtype=int)

    # Inicializar la primera fila y columna
    for i in range(n + 1):
        dist_matrix[i][0] = i
    for j in range(m + 1):
        dist_matrix[0][j] = j

    # Llenar la matriz de distancia de edición
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = 0 if text[i - 1] == pattern[j - 1] else 1
            dist_matrix[i][j] = min(
                dist_matrix[i - 1][j] + 1,  # Eliminación
                dist_matrix[i][j - 1] + 1,  # Inserción
                dist_matrix[i - 1][j - 1] + cost  # Sustitución
            )

    # Buscar coincidencias en la matriz
    matches = []
    for i in range(n):
        if dist_matrix[i + 1][m] <= max_errors:
            matches.append(i - m + 1)

    return matches if matches else [-1]


# Ejemplo de uso para secuencias de ADN
secuencia_biologica = "ATGCCCCAACTAAATACCGCCGTATGACCCACCATAATTACCCCCATACTCCTGACACTATTTCTCGTCACCCAACTAAAAATATTAAATTCAAATTACCATCTACCCCCCTCACCAAAACCCATAAAAATAAAAAACTACAATAAACCCTGAGAACCAAAATGAACGAAAATCTATTCGCTTCATTCGCTGCCCCCACAATCCTAG"
patron = "TCTA"  # Patrón que buscamos en la secuencia biológica
max_errors = 2  # Número máximo de errores permitidos

# Buscar coincidencias en la secuencia biológica
coincidencias = faoso_search(secuencia_biologica, patron, max_errors)

if coincidencias == [-1]:
    print("No se encontraron coincidencias")
else:
    print("Coincidencias del patrón en los índices:", coincidencias)

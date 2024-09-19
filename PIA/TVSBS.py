def precompute_shift_tvsbs(pattern):
    """
    Precalcula la tabla de desplazamientos (shift table) basada en 2-grams (pares de caracteres).
    """
    m = len(pattern)
    shift_table = {}

    # Crear la tabla de desplazamientos para todos los pares de caracteres en el patrón
    for i in range(m - 1):
        pair = pattern[i:i+2]  # Crear el 2-gram
        shift_table[pair] = m - i - 2  # Calcular el desplazamiento

    return shift_table


def tvsbs_search(text, pattern):
    """
    Implementa el algoritmo TVSBS para la búsqueda exacta de un patrón en una secuencia.
    """
    n = len(text)
    m = len(pattern)

    # Obtener la tabla de desplazamientos
    shift_table = precompute_shift_tvsbs(pattern)

    # Desplazamiento del patrón respecto al texto
    s = 0

    while s <= n - m:
        # Compara el patrón con el texto desde la derecha (utilizando 2-grams)
        j = m - 2

        while j >= 0 and pattern[j:j+2] == text[s + j:s + j + 2]:
            j -= 2  # Comparar dos caracteres a la vez (2-gram)

        # Si el patrón coincide
        if j < 0:
            print(f"Patrón encontrado en el índice {s}")
            s += 1
        else:
            # Obtener el 2-gram del texto en la posición que causó el desajuste
            if s + m - 2 < n:
                current_2gram = text[s + m - 2:s + m]
                # Desplazar el patrón según la tabla de desplazamientos, si no está en la tabla se mueve 2 posiciones
                s += shift_table.get(current_2gram, 2)
            else:
                s += 1


# Ejemplo de uso:
texto = "ATGCCCCAACTAAATACCGCCGTATGACCCACCATAATTACCCCCATACTCCTGACACTATTTCTCGTCACCCAACTAAAAATATTAAATTCAAATTACCATCTACCCCCCTCACCAAAACCCATAAAAATAAAAAACTACAATAAACCCTGAGAACCAAAATGAACGAAAATCTATTCGCTTCATTCGCTGCCCCCACAATCCTAG"
patron = "TCTA"

tvsbs_search(texto, patron)

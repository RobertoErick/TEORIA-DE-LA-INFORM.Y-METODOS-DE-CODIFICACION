def bad_char_heuristic_bmh(pattern):
    """
    Genera la tabla de malas coincidencias para Boyer-Moore-Horspool (BMH).
    """
    bad_char = {}
    m = len(pattern)

    # Rellenar la tabla con la última aparición de cada carácter en el patrón
    for i in range(m - 1):
        bad_char[pattern[i]] = i

    return bad_char


def boyer_moore_horspool_search(text, pattern):
    """
    Implementa el algoritmo Boyer-Moore-Horspool (BMH) para la búsqueda de un patrón en un texto.
    """
    n = len(text)
    m = len(pattern)

    # Obtener la tabla de malas coincidencias
    bad_char = bad_char_heuristic_bmh(pattern)

    # Desplazamiento del patrón respecto al texto
    s = 0

    while s <= n - m:
        j = m - 1

        # Comparar el patrón con el texto de derecha a izquierda
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        if j < 0:
            print(f"Patrón encontrado en el índice {s}")
            s += 1  # Si se encuentra el patrón, desplazar el patrón una posición
        else:
            # Desplazar el patrón hacia adelante basado en el carácter que causó el desajuste
            bad_char_shift = bad_char.get(text[s + j], -1)
            s += max(1, j - bad_char_shift)


# Ejemplo de uso:
texto = "GCTAGCTCTACGAGTCTA"
patron = "TCTA"

boyer_moore_horspool_search(texto, patron)

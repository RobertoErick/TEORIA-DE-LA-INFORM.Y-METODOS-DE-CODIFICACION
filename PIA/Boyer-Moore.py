def bad_char_heuristic(pattern):
    """
    Esta función genera la tabla de malas coincidencias (bad character heuristic)
    que indica cómo mover el patrón cuando hay un desajuste.
    """
    bad_char = [-1] * 256  # Suponemos que el tamaño del alfabeto es 256 (ASCII)

    # Rellenar la tabla con la última aparición de cada carácter en el patrón
    for i in range(len(pattern)):
        bad_char[ord(pattern[i])] = i

    return bad_char


def boyer_moore_search(text, pattern):
    """
    Esta función implementa el algoritmo Boyer-Moore para la búsqueda de una cadena patrón
    dentro de un texto dado.
    """
    m = len(pattern)
    n = len(text)

    # Obtener la tabla de malas coincidencias
    bad_char = bad_char_heuristic(pattern)

    # `s` es el desplazamiento del patrón con respecto al texto
    s = 0
    while s <= n - m:
        j = m - 1

        # Desplazar el patrón para que coincida con el texto de derecha a izquierda
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        # Si el patrón coincide completamente
        if j < 0:
            print(f"Patrón encontrado en el índice {s}")
            # Mover el patrón hacia la derecha de manera que coincida el siguiente carácter
            s += (m - bad_char[ord(text[s + m])] if s + m < n else 1)
        else:
            # Mover el patrón hacia la derecha para alinear la última aparición del carácter desajustado
            s += max(1, j - bad_char[ord(text[s + j])])


# Ejemplo de uso:
texto = "GCTAGCTCTACGAGTCTA"
patron = "TCTA"

boyer_moore_search(texto, patron)

def bad_char_heuristic_bmhq(pattern):
    """
    Genera la tabla de malas coincidencias para Boyer-Moore-Horspool Quick Search (BMHq).
    """
    bad_char = {}
    m = len(pattern)

    # Rellenar la tabla con la última aparición de cada carácter en el patrón
    for i in range(m):
        bad_char[pattern[i]] = i

    return bad_char


def bmhq_search(text, pattern):
    """
    Implementa el algoritmo Boyer-Moore-Horspool Quick Search (BMHq) para la búsqueda de un patrón en un texto.
    """
    n = len(text)
    m = len(pattern)

    # Obtener la tabla de malas coincidencias
    bad_char = bad_char_heuristic_bmhq(pattern)

    # Desplazamiento del patrón respecto al texto
    s = 0

    while s <= n - m:
        # Comparar solo el último carácter del patrón con el texto
        if pattern[m - 1] == text[s + m - 1]:
            # Si el último carácter coincide, comparar todo el patrón
            j = m - 2
            while j >= 0 and pattern[j] == text[s + j]:
                j -= 1

            if j < 0:
                print(f"Patrón encontrado en el índice {s}")
                s += 1  # Si se encuentra el patrón, desplazar el patrón una posición
            else:
                # Desplazar el patrón hacia adelante basado en el carácter que causó el desajuste
                bad_char_shift = bad_char.get(text[s + m - 1], -1)
                s += max(1, m - bad_char_shift - 1)
        else:
            # Desplazar el patrón hacia adelante basado en el carácter que causó el desajuste
            bad_char_shift = bad_char.get(text[s + m - 1], -1)
            s += max(1, m - bad_char_shift - 1)


# Ejemplo de uso:
texto = "GCTAGCTCTACGAGTCTA"
patron = "TCTA"

bmhq_search(texto, patron)

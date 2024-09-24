def bad_character_heuristic(pattern):
    """
    Crea la tabla de la regla del mal carácter (Bad Character Rule) para el patrón dado.
    """
    bad_char = [-1] * 256  # Tabla inicializada con -1 para todos los posibles caracteres

    # Llenar la tabla con la última aparición de cada carácter en el patrón
    for i in range(len(pattern)):
        bad_char[ord(pattern[i])] = i

    return bad_char

def boyer_moore_bad_char(text, pattern):
    """
    Implementa la búsqueda de patrones usando la regla del mal carácter del algoritmo Boyer-Moore.
    """
    m = len(pattern)
    n = len(text)

    # Obtener la tabla de la regla del mal carácter
    bad_char = bad_character_heuristic(pattern)

    s = 0  # s es el desplazamiento de la cadena con respecto al texto
    while s <= n - m:
        j = m - 1

        # Reducir j mientras los caracteres de patrón y texto coincidan
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        # Si el patrón coincide completamente con el texto
        if j < 0:
            print(f"Patrón encontrado en el índice {s}")
            # Mover el patrón hacia adelante para continuar buscando
            s += (m - bad_char[ord(text[s + m])] if s + m < n else 1)
        else:
            # Mover el patrón según la regla del mal carácter
            s += max(1, j - bad_char[ord(text[s + j])])

# Ejemplo de uso
text = "GCTTCTGCTACCTTTTGCGCGCGCGCGGAA"
pattern = "CCTTTTGC"
boyer_moore_bad_char(text, pattern)

def preprocess_bad_character_rule(pattern):
    """
    Preprocesa la tabla para la Bad Character Rule. 
    Devuelve un diccionario que indica la última aparición de cada carácter en el patrón.
    """
    bad_char_table = {}
    for i in range(len(pattern)):
        bad_char_table[pattern[i]] = i
    return bad_char_table


def preprocess_good_suffix_rule(pattern):
    """
    Preprocesa el patrón para obtener el arreglo de saltos de la Good Suffix Rule.
    """
    m = len(pattern)
    suffix = [-1] * m
    border = [0] * m

    # Precomputar los bordes
    j = m
    for i in range(m - 1, -1, -1):
        while j < m and pattern[i] != pattern[j]:
            j = suffix[j]
        suffix[i] = j

    # Precomputar los saltos
    for i in range(m - 1):
        if suffix[i] != -1:
            border[i] = suffix[i] - i + m

    return border


def good_suffix_shift(pattern, border, mismatched_position):
    """
    Calcula el número de posiciones a saltar usando la Good Suffix Rule.
    """
    m = len(pattern)
    if mismatched_position == m - 1:
        return border[m - 1]
    return border[mismatched_position]


def bad_character_shift(bad_char_table, mismatched_char, mismatched_position):
    """
    Calcula el número de posiciones a saltar usando la Bad Character Rule.
    """
    if mismatched_char in bad_char_table:
        return max(1, mismatched_position - bad_char_table[mismatched_char])
    else:
        return mismatched_position + 1


def boyer_moore(text, pattern):
    """
    Implementación completa del algoritmo Boyer-Moore que combina la Good Suffix Rule y la Bad Character Rule.
    """
    n = len(text)
    m = len(pattern)

    # Preprocesar las tablas de Bad Character y Good Suffix
    bad_char_table = preprocess_bad_character_rule(pattern)
    good_suffix_table = preprocess_good_suffix_rule(pattern)

    i = 0
    while i <= n - m:
        j = m - 1
        # Comparar de derecha a izquierda
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        
        if j < 0:  # Si hay una coincidencia completa
            print(f"Patrón encontrado en la posición {i}")
            i += good_suffix_table[0]  # Saltar usando la Good Suffix Rule
        else:  # Si hay un desajuste
            bad_char_shift = bad_character_shift(bad_char_table, text[i + j], j)
            good_suffix_shift_value = good_suffix_shift(pattern, good_suffix_table, j)
            # Elegir el máximo desplazamiento entre las dos reglas
            i += max(bad_char_shift, good_suffix_shift_value)


# Ejemplo de uso:
text = "CGTGCCTACCTTACCGTT"
pattern = "CCTTAC"
boyer_moore(text, pattern)

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


def boyer_moore_good_suffix(text, pattern):
    """
    Implementación del algoritmo Boyer-Moore con Good Suffix Rule.
    """
    n = len(text)
    m = len(pattern)

    # Preprocesar el patrón para obtener los saltos
    border = preprocess_good_suffix_rule(pattern)

    i = 0
    while i <= n - m:
        j = m - 1
        # Comparar de derecha a izquierda
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        if j < 0:  # Si hay una coincidencia completa
            print(f"Patrón encontrado en la posición {i}")
            i += border[0]
        else:  # Si hay un desajuste
            i += good_suffix_shift(pattern, border, j)


# Ejemplo de uso:
text = "CGTGCCTACCTTACCGTT"
pattern = "CCTTAC"
boyer_moore_good_suffix(text, pattern)

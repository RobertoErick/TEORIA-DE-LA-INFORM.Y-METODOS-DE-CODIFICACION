def compute_fingerprint_halfwords(halfword1, halfword2):
    """
    Calcula el fingerprint para dos halfwords (subcadenas de 2 caracteres cada una).
    """
    # Mapeamos los caracteres a, c, g, t a valores únicos de 2 bits
    map_adn = {'a': 0, 'c': 1, 'g': 2, 't': 3}
    
    # Calcular fingerprint para el primer halfword
    fingerprint1 = 0
    for char in halfword1:
        fingerprint1 = (fingerprint1 << 2) | map_adn[char]
    
    # Calcular fingerprint para el segundo halfword
    fingerprint2 = 0
    for char in halfword2:
        fingerprint2 = (fingerprint2 << 2) | map_adn[char]
    
    return fingerprint1, fingerprint2

def create_shift_table_BMH4c(pattern):
    """
    Crea la tabla de desplazamientos basada en los fingerprints de los halfwords del patrón.
    """
    m = len(pattern)
    shift_table = {}

    # Crear la tabla de desplazamientos para cada par de halfwords
    for i in range(m - 4):
        halfword1 = pattern[i:i + 2]
        halfword2 = pattern[i + 2:i + 4]
        fingerprint1, fingerprint2 = compute_fingerprint_halfwords(halfword1, halfword2)
        shift_table[(fingerprint1, fingerprint2)] = m - i - 4

    # Último 4-gram tiene desplazamiento 0
    final_halfword1 = pattern[-4:-2]
    final_halfword2 = pattern[-2:]
    fingerprint1, fingerprint2 = compute_fingerprint_halfwords(final_halfword1, final_halfword2)
    shift_table[(fingerprint1, fingerprint2)] = 0
    
    return shift_table

def BMH4c_search(text, pattern):
    """
    Realiza la búsqueda utilizando el algoritmo BMH4c.
    text: Texto en el cual buscar el patrón.
    pattern: Patrón que estamos buscando.
    """
    n = len(text)
    m = len(pattern)

    if m < 4 or n < m:
        return []

    # Crear la tabla de desplazamientos basada en los halfwords
    shift_table = create_shift_table_BMH4c(pattern)

    matches = []
    s = 0  # Posición en el texto

    while s <= n - m:
        # Leer los últimos dos halfwords del texto alineados con el patrón
        halfword1 = text[s + m - 4:s + m - 2]
        halfword2 = text[s + m - 2:s + m]
        fingerprint1, fingerprint2 = compute_fingerprint_halfwords(halfword1, halfword2)

        # Obtener el desplazamiento correspondiente a estos fingerprints
        if (fingerprint1, fingerprint2) in shift_table:
            shift_value = shift_table[(fingerprint1, fingerprint2)]
        else:
            shift_value = m

        # Si hay coincidencia en los fingerprints, verificar todo el patrón
        if shift_value == 0:
            if text[s:s + m] == pattern:
                matches.append(s)
            shift_value = m  # Desplazar completamente si se encuentra una coincidencia

        s += shift_value  # Desplazar la ventana de búsqueda

    return matches

# Ejemplo de uso
text = "acgttgctacgttgcttacgacgt"
pattern = "acgttgct"
resultados = BMH4c_search(text, pattern)
print("Patrón encontrado en las posiciones:", resultados)

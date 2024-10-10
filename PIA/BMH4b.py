def compute_fingerprint_4gram(gram):
    """
    Calcula el fingerprint (huella digital) para un 4-gram, que es un entero
    basado en los caracteres de ADN (a, c, g, t).
    """
    # Mapeamos los caracteres a, c, g, t a valores únicos de 2 bits
    map_adn = {'a': 0, 'c': 1, 'g': 2, 't': 3}
    fingerprint = 0
    
    for char in gram:
        fingerprint = (fingerprint << 2) | map_adn[char]  # Desplazamos 2 bits y añadimos el valor correspondiente

    return fingerprint

def create_shift_table_BMH4b(pattern):
    """
    Crea la tabla de desplazamientos basada en los fingerprints de los 4-grams del patrón.
    """
    m = len(pattern)
    shift_table = {}

    # Crear la tabla de desplazamientos para cada 4-gram en el patrón
    for i in range(m - 4):
        qgram = pattern[i:i + 4]
        fingerprint = compute_fingerprint_4gram(qgram)
        shift_table[fingerprint] = m - i - 4

    # Último 4-gram tiene desplazamiento 0
    final_qgram = pattern[-4:]
    shift_table[compute_fingerprint_4gram(final_qgram)] = 0
    return shift_table

def BMH4b_search(text, pattern):
    """
    Realiza la búsqueda utilizando el algoritmo BMH4b.
    text: Texto en el cual buscar el patrón.
    pattern: Patrón que estamos buscando.
    """
    n = len(text)
    m = len(pattern)

    if m < 4 or n < m:
        return []

    # Crear la tabla de desplazamientos basada en fingerprints
    shift_table = create_shift_table_BMH4b(pattern)

    matches = []
    s = 0  # Posición en el texto

    while s <= n - m:
        # Leer el último 4-gram del texto alineado con el patrón
        qgram_text = text[s + m - 4:s + m]
        fingerprint = compute_fingerprint_4gram(qgram_text)

        # Obtener el desplazamiento correspondiente a este fingerprint
        if fingerprint in shift_table:
            shift_value = shift_table[fingerprint]
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
resultados = BMH4b_search(text, pattern)
print("Patrón encontrado en las posiciones:", resultados)

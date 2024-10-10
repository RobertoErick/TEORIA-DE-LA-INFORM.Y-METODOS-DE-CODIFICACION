def compute_fingerprint_2gram(gram):
    """
    Calcula el fingerprint (huella digital) para un 2-gram, que es un entero
    basado en los caracteres del alfabeto de aminoácidos.
    """
    # Mapeamos los aminoácidos a valores únicos. Utilizamos los 20 caracteres comunes en las secuencias de aminoácidos.
    map_amino = {'A': 0, 'C': 1, 'D': 2, 'E': 3, 'F': 4, 'G': 5, 'H': 6, 'I': 7, 'K': 8, 'L': 9,
                 'M': 10, 'N': 11, 'P': 12, 'Q': 13, 'R': 14, 'S': 15, 'T': 16, 'V': 17, 'W': 18, 'Y': 19}
    fingerprint = 0
    
    for char in gram:
        fingerprint = (fingerprint * 20) + map_amino[char]  # Multiplicamos por 20 para cada aminoácido
    
    return fingerprint

def create_shift_table_BMH2(pattern):
    """
    Crea la tabla de desplazamientos basada en los fingerprints de los 2-grams del patrón.
    """
    m = len(pattern)
    shift_table = {}

    # Crear la tabla de desplazamientos para cada 2-gram
    for i in range(m - 2):
        qgram = pattern[i:i + 2]
        fingerprint = compute_fingerprint_2gram(qgram)
        shift_table[fingerprint] = m - i - 2

    # Último 2-gram tiene desplazamiento 0
    final_qgram = pattern[-2:]
    shift_table[compute_fingerprint_2gram(final_qgram)] = 0
    return shift_table

def BMH2_search(text, pattern):
    """
    Realiza la búsqueda utilizando el algoritmo BMH2.
    text: Texto en el cual buscar el patrón.
    pattern: Patrón que estamos buscando.
    """
    n = len(text)
    m = len(pattern)

    if m < 2 or n < m:
        return []

    # Crear la tabla de desplazamientos basada en los 2-grams
    shift_table = create_shift_table_BMH2(pattern)

    matches = []
    s = 0  # Posición en el texto

    while s <= n - m:
        # Leer el último 2-gram del texto alineado con el patrón
        qgram_text = text[s + m - 2:s + m]
        fingerprint = compute_fingerprint_2gram(qgram_text)

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
text = "ACDEFGHIKLMNPQRSTVWYACDEFGHIK"
pattern = "ACDEFG"
resultados = BMH2_search(text, pattern)
print("Patrón encontrado en las posiciones:", resultados)

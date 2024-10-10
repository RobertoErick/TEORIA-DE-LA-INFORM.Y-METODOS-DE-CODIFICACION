def compute_fingerprint_halfword(halfword):
    """
    Calcula el fingerprint (huella digital) para un halfword (subcadena de 2 caracteres).
    """
    # Mapeamos los aminoácidos a valores únicos. Utilizamos los 20 caracteres comunes en las secuencias de aminoácidos.
    map_amino = {'A': 0, 'C': 1, 'D': 2, 'E': 3, 'F': 4, 'G': 5, 'H': 6, 'I': 7, 'K': 8, 'L': 9,
                 'M': 10, 'N': 11, 'P': 12, 'Q': 13, 'R': 14, 'S': 15, 'T': 16, 'V': 17, 'W': 18, 'Y': 19}
    fingerprint = 0
    
    for char in halfword:
        fingerprint = (fingerprint * 20) + map_amino[char]  # Multiplicamos por 20 para cada aminoácido
    
    return fingerprint

def create_shift_table_BMH2c(pattern):
    """
    Crea la tabla de desplazamientos basada en los fingerprints de los halfwords (2-grams) del patrón.
    """
    m = len(pattern)
    shift_table = {}

    # Crear la tabla de desplazamientos para cada halfword
    for i in range(m - 2):
        halfword = pattern[i:i + 2]
        fingerprint = compute_fingerprint_halfword(halfword)
        shift_table[fingerprint] = m - i - 2

    # Último halfword tiene desplazamiento 0
    final_halfword = pattern[-2:]
    shift_table[compute_fingerprint_halfword(final_halfword)] = 0
    
    return shift_table

def BMH2c_search(text, pattern):
    """
    Realiza la búsqueda utilizando el algoritmo BMH2c.
    text: Texto en el cual buscar el patrón.
    pattern: Patrón que estamos buscando.
    """
    n = len(text)
    m = len(pattern)

    if m < 2 or n < m:
        return []

    # Crear la tabla de desplazamientos basada en los halfwords
    shift_table = create_shift_table_BMH2c(pattern)

    matches = []
    s = 0  # Posición en el texto

    while s <= n - m:
        # Leer el último halfword (2-gram) del texto alineado con el patrón
        halfword = text[s + m - 2:s + m]
        fingerprint = compute_fingerprint_halfword(halfword)

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
resultados = BMH2c_search(text, pattern)
print("Patrón encontrado en las posiciones:", resultados)

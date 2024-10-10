def create_shift_table_BMH4(pattern):
    """
    Crea la tabla de desplazamientos basada en los 4-grams del patrón.
    """
    m = len(pattern)
    shift_table = {}

    # Inicializar los 4-grams con el desplazamiento del tamaño del patrón
    for i in range(m - 4):
        qgram = pattern[i:i + 4]
        shift_table[qgram] = m - i - 4

    # Último 4-gram tiene un desplazamiento de 0
    shift_table[pattern[-4:]] = 0
    return shift_table

def BMH4_search(text, pattern):
    """
    Realiza la búsqueda utilizando el algoritmo BMH4.
    text: Texto en el cual buscar el patrón.
    pattern: Patrón que estamos buscando.
    """
    n = len(text)
    m = len(pattern)

    # Verificar si el patrón es más pequeño que 4 caracteres o el texto es más corto que el patrón
    if m < 4 or n < m:
        return []

    # Crear la tabla de desplazamientos
    shift_table = create_shift_table_BMH4(pattern)

    matches = []
    s = 0  # Posición de búsqueda en el texto

    while s <= n - m:
        # Obtener el último 4-gram del texto alineado con el patrón
        qgram_text = text[s + m - 4:s + m]

        # Obtener el desplazamiento desde la tabla de desplazamientos
        if qgram_text in shift_table:
            shift_value = shift_table[qgram_text]
        else:
            shift_value = m

        # Si el desplazamiento es 0, verificar si coincide todo el patrón
        if shift_value == 0:
            if text[s:s + m] == pattern:
                matches.append(s)
            shift_value = m  # Si hay coincidencia, desplazarse completamente

        s += shift_value  # Desplazar la ventana de búsqueda

    return matches

# Ejemplo de uso
text = "acgttgctacgttgcttacgacgt"
pattern = "acgttgct"
resultados = BMH4_search(text, pattern)
print("Patrón encontrado en las posiciones:", resultados)

def create_shift_table(pattern, q):
    """
    Crea la tabla de desplazamientos basada en los q-grams del patrón.
    """
    m = len(pattern)
    shift_table = {}
    
    # Inicializar todos los posibles q-grams con el desplazamiento del tamaño del patrón
    for i in range(0, len(pattern) - q + 1):
        qgram = pattern[i:i + q]
        shift_table[qgram] = m - i - q
    
    # Desplazamiento final
    shift_table[pattern[-q:]] = 0
    return shift_table

def BMHq_search(text, pattern, q):
    """
    Realiza la búsqueda utilizando el algoritmo BMHq.
    text: Texto en el cual buscar el patrón.
    pattern: Patrón que estamos buscando.
    q: Tamaño del q-gram (subcadena).
    """
    n = len(text)
    m = len(pattern)
    
    if m < q or n < m:
        return []
    
    # Crear la tabla de desplazamientos
    shift_table = create_shift_table(pattern, q)
    
    matches = []
    s = 0  # s es la posición del texto
    
    while s <= n - m:
        # Obtener el q-gram en la posición actual del texto
        qgram_text = text[s + m - q:s + m]
        
        if qgram_text in shift_table:
            shift_value = shift_table[qgram_text]
        else:
            shift_value = m
        
        # Si el q-gram coincide, verificar el patrón completo
        if shift_value == 0:
            if text[s:s + m] == pattern:
                matches.append(s)
            shift_value = m
        
        s += shift_value
    
    return matches

# Ejemplo de uso
text = "acgttgctacgttgcttacgacgt"
pattern = "acgttgc"
q = 2  # Usamos 2-grams

resultados = BMHq_search(text, pattern, q)
print("Patrón encontrado en las posiciones:", resultados)

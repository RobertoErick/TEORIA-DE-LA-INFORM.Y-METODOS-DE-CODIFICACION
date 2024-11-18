def preprocess_shift_table(pattern, alphabet_size=4):
    m = len(pattern)
    shift_table = [m] * (alphabet_size ** 4)  # Tabla de desplazamiento para q = 4
    c = 4  # Tamaño del alfabeto
    u = c ** 4  # Número total de combinaciones de 4 caracteres (q = 4)
    
    # Inicialización de las tablas de transformación del alfabeto
    h = [[0] * 256 for _ in range(4)]
    h[0][ord('a')] = 0
    h[0][ord('c')] = 1
    h[0][ord('g')] = 2
    h[0][ord('t')] = 3

    for i in range(1, 4):
        for j in range(256):
            h[i][j] = c * h[i-1][j]

    # Preprocesamiento de la tabla de desplazamientos
    s = 0
    for i in range(1, 4):
        s = s // c + h[3][ord(pattern[i-1])]
        for j in range(s, s + u//c):
            shift_table[j] = m - i

    s = s // c + h[3][ord(pattern[3])]
    for i in range(4, m):
        shift_table[s] = m - i + 1
        s = s // c + h[3][ord(pattern[i])]

    return shift_table, h

def compute_fingerprint(text, k, h, q=4):
    # Cálculo de la huella digital usando Horner's rule
    t = 0
    for i in range(q):
        t = h[q-1-i][ord(text[k-i])] + t
    return t

def boyer_moore_horspool_dna_search(text, pattern):
    m = len(pattern)
    n = len(text)
    
    # Preprocesar la tabla de desplazamiento y la tabla de huellas
    shift_table, h = preprocess_shift_table(pattern)
    
    # Calcular huella digital del patrón
    pattern_fingerprint = compute_fingerprint(pattern, m-1, h)
    
    k = m  # Índice inicial
    results = []
    
    while k <= n:
        # Calcular la huella digital de la secuencia actual del texto
        text_fingerprint = compute_fingerprint(text, k-1, h)
        
        # Comprobar si las huellas coinciden
        if text_fingerprint == pattern_fingerprint:
            # Comparar las posiciones restantes del patrón
            if text[k-m:k] == pattern:
                results.append(k-m)  # Coincidencia encontrada
        
        # Desplazamiento basado en la huella del texto
        k += shift_table[text_fingerprint]
    
    return results

# Ejemplo de uso
text = "acgtacgtgacgtacgttt"
pattern = "acgt"
result = boyer_moore_horspool_dna_search(text, pattern)
print("Coincidencias encontradas en las posiciones:", result)

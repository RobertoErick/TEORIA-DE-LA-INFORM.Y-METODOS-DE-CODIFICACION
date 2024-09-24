def compute_prefix_function(pattern):
    m = len(pattern)
    prefix = [0] * m
    k = 0
    
    # Iterar desde el segundo caracter hasta el último en el patrón
    for q in range(1, m):
        while k > 0 and pattern[k] != pattern[q]:
            k = prefix[k - 1]
        
        if pattern[k] == pattern[q]:
            k += 1
        
        prefix[q] = k
    
    return prefix

def KMP_search(text, pattern):
    n = len(text)
    m = len(pattern)
    prefix = compute_prefix_function(pattern)
    q = 0  # Número de caracteres coincidentes
    
    # Iterar sobre el texto
    for i in range(n):
        while q > 0 and pattern[q] != text[i]:
            q = prefix[q - 1]
        
        if pattern[q] == text[i]:
            q += 1
        
        if q == m:
            print(f"Patrón encontrado en la posición {i - m + 1}")
            q = prefix[q - 1]  # Preparar para la siguiente coincidencia

# Ejemplo de uso:
text = "bacbabababacaab"
pattern = "ababaca"
KMP_search(text, pattern)
def preprocess_pattern(pattern):
    """Preprocesa el patrón para crear una tabla de bits"""
    m = len(pattern)
    B = [0] * 256
    for i in range(m):
        B[ord(pattern[i])] |= (1 << (m - 1 - i))  # Orden corregido
    return B

def sbndm_search(text, pattern):
    """Algoritmo SBNDM para buscar un patrón en el texto"""
    m = len(pattern)
    n = len(text)

    # Verificar si el patrón es más largo que el texto
    if m > n:
        return []  # Retornar vacío si el patrón es más largo que el texto
    
    B = preprocess_pattern(pattern)
    matches = []
    
    j = 0
    while j <= n - m:
        D = (1 << (m - 1))  # Inicializar D como la máscara con el bit más a la izquierda encendido
        i = m - 1
        while i >= 0 and D != 0:
            D &= B[ord(text[j + i])]
            if D != 0:
                i -= 1
                D <<= 1
        if i < 0:  # Coincidencia encontrada
            matches.append(j)
        j += 1  # Mover al siguiente índice del texto
    
    return matches if matches else [-1]  # Si no se encuentran coincidencias, devolver [-1]

# Ejemplo de uso para secuencias de aminoácidos y ADN
secuencia_biologica = "ATGCCCCAACTAAATACCGCCGTATGACCCACCATAATTACCCCCATACTCCTGACACTATTTCTCGTCACCCAACTAAAAATATTAAATTCAAATTACCATCTACCCCCCTCACCAAAACCCATAAAAATAAAAAACTACAATAAACCCTGAGAACCAAAATGAACGAAAATCTATTCGCTTCATTCGCTGCCCCCACAATCCTAG"
patron = "TCTA"  # Patrón que buscamos en la secuencia biológica

# Buscar coincidencias en la secuencia biológica
coincidencias = sbndm_search(secuencia_biologica, patron)

if coincidencias == [-1]:
    print("No se encontraron coincidencias")
else:
    print("Coincidencias del patrón en los índices:", coincidencias)

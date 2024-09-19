def ssabs_search(text, pattern):
    """
    Implementa el algoritmo SSABS para la búsqueda exacta de un patrón en una secuencia biológica.
    """
    n = len(text)  # Longitud del texto
    m = len(pattern)  # Longitud del patrón

    # Desplazamiento del patrón respecto al texto
    s = 0

    while s <= n - m:
        # Guard test: comparar el primer y último carácter del patrón
        if pattern[0] == text[s] and pattern[m - 1] == text[s + m - 1]:
            # Si pasa el guard test, comparar el patrón completo
            match = True
            for j in range(1, m - 1):
                if pattern[j] != text[s + j]:
                    match = False
                    break
            if match:
                print(f"Patrón encontrado en el índice {s}")

        # Desplazar el patrón hacia adelante
        s += 1


# Ejemplo de uso:
texto = "ATGCCCCAACTAAATACCGCCGTATGACCCACCATAATTACCCCCATACTCCTGACACTATTTCTCGTCACCCAACTAAAAATATTAAATTCAAATTACCATCTACCCCCCTCACCAAAACCCATAAAAATAAAAAACTACAATAAACCCTGAGAACCAAAATGAACGAAAATCTATTCGCTTCATTCGCTGCCCCCACAATCCTAG"
patron = "TCTA"

ssabs_search(texto, patron)


class BMHq:
    def __init__(self,text : str, pattern : str, q : int):
        self.text = text
        self.pattern = pattern
        self.q = q


    def create_shift_table(self):
        """
        Crea la tabla de desplazamientos basada en los q-grams del patrón.
        """
        m = len(self.pattern)
        shift_table = {}

        # Inicializar todos los posibles q-grams con el desplazamiento del tamaño del patrón
        for i in range(0, len(self.pattern) - self.q + 1):
            q_gram = self.pattern[i:i + self.q]
            shift_table[q_gram] = m - i - self.q

        # Desplazamiento final
        shift_table[self.pattern[-self.q:]] = 0
        return shift_table


    def q_search(self):
        """
        Realiza la búsqueda utilizando el algoritmo BMHq.
        text: Texto en el cual buscar el patrón.
        pattern: Patrón que estamos buscando.
        q: Tamaño del q-gram (subcadena).
        """
        n = len(self.text)
        m = len(self.pattern)

        if m < self.q or n < m:
            return []

        # Crear la tabla de desplazamientos
        shift_table = self.create_shift_table()

        matches = []
        s = 0  # s es la posición del texto

        while s <= n - m:
            # Obtener el q-gram en la posición actual del texto
            qgram_text = self.text[s + m - self.q:s + m]

            if qgram_text in shift_table:
                shift_value = shift_table[qgram_text]
            else:
                shift_value = m

            # Si el q-gram coincide, verificar el patrón completo
            if shift_value == 0:
                if self.text[s:s + m] == self.pattern:
                    matches.append(s)
                shift_value = m

            s += shift_value

        return matches


def main():
    # Ejemplo de uso
    text = "acgttgctacgttgcttacgacgt"
    pattern = "acgttgc"
    q = 2  # Usamos 2-grams

    bmh = BMHq(text, pattern, q)

    results = bmh.q_search()
    print("Patrón encontrado en las posiciones:", results)


if __name__ == '__main__':
    main()
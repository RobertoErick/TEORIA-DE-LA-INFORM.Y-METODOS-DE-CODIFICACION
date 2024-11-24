from tkinter import filedialog


def fingerprint(sequence: str) -> int:
    """Calculate the fingerprint of a q-gram."""
    r = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    fp = 0
    for i in range(len(sequence)):
        if sequence[i] in r:
            fp += r[sequence[i]] * (4 ** (len(sequence) - i - 1))
    return fp


class BMHq:
    def __init__(self, pattern: str, text: str, q: int = 4):
        self.pattern = pattern
        self.text = text
        self.q = q

        if len(pattern) < q:
            raise ValueError("Pattern length must be greater than or equal to q.")


    def _initialize_shift_table(self):
        """Initialize the shift table for the q-grams in the pattern."""
        D = {}
        m = len(self.pattern)
        for i in range(m - self.q + 1):
            q_gram = self.pattern[i:i + self.q]
            fp = fingerprint(q_gram)
            D[fp] = m - i - self.q
        return D


    def search(self):
        D = self._initialize_shift_table()
        m = len(self.pattern)
        n = len(self.text)
        matches = []

        # Add stopper to the text
        self.text += self.pattern

        # Start searching
        k = m
        while k <= n:
            q_gram = self.text[k - self.q:k]
            fp = fingerprint(q_gram)
            print(f"Text q-gram {q_gram} fingerprint {fp}")
            if fp in D:
                shift = D[fp]
            else:
                shift = m  # Full shift if q-gram not in pattern

            if shift == 0:  # Possible match found
                # Verify the full pattern
                if self.text[k - m:k] == self.pattern:
                    matches.append(k - m)
                shift = 1  # Avoid infinite loops for zero shift

            k += shift

        return matches


def main():
    text = "acgttgctacgttgcttacgacgt".upper()
    pattern = "ACGT"

    bmh = BMHq(pattern, text)
    matches = bmh.search()

    print(f"Pattern found at indices: {matches}")


if __name__ == '__main__':
    main()

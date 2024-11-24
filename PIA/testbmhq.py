

def fingerprint(sequence : str) -> int :
    r = { 'a' : 0, 'c' : 1, 'g' : 2, 't' : 3 }
    fp = []
    for i in range(len(sequence)):
        if sequence[i] not in r.keys() or i > len(r) - 1:
            fp.append(0)
        else:
            fp.append(r[sequence[i]] * (4 ** i))
    return sum(fp)


class BMHq:

    def __init__(self, pattern, text, q = 4):
        self.pattern = pattern
        self.text = text
        self.q = q


    def preprocess_shift_table(self) -> dict[int, int]:
        """
        Precompute the shift table for the pattern based on fingerprints.
        """
        m = len(self.pattern)
        D = {}
        for i in range(m - self.q + 1):
            substring = self.pattern[i:i + self.q]
            fp = fingerprint(substring)
            D[fp] = m - self.q - i
        # Default shift for missing fingerprints
        D.setdefault(0, m - self.q + 1)
        return D


    def search(self):

        n = len(self.text)
        m = len(self.pattern)
        if m < self.q:
            raise ValueError("Pattern length must be greater than or equal to q.")

        # Initialize the shift table
        D = {}

        # Add stopper to the text
        self.text += self.pattern

        p = fingerprint(self.pattern)
        r = D[p]
        D[p] = 0
        k = m
        s = D[fingerprint(self.text)]

        while s > 0:
            k += s
            s = D[fingerprint(self.text)]
        if k > n:
            return
        s = r

        return


def main():
    text = "acgttgctacgttgcttacgacgt"
    pattern = "acgttgc"

    bmh = BMHq(pattern, text)

    print('text', fingerprint(text))
    print('pattern', fingerprint(pattern))
    bmh.search()


if __name__ == '__main__':
    main()
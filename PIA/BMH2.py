import time
from tkinter import filedialog


def fingerprint(sequence: str) -> int:
    """Calculate the fingerprint of a q-gram."""
    r = {'A': 0, 'C': 1, 'D': 2, 'E': 3, 'F': 4, 'G': 5, 'H': 6, 'I': 7, 'K': 8, 'L': 9,
         'M': 10, 'N': 11, 'P': 12, 'Q': 13, 'R': 14, 'S': 15, 'T': 16, 'V': 17, 'W': 18, 'Y': 19}
    fp = 0
    for i in range(len(sequence)):
        if sequence[i] in r:
            fp += r[sequence[i]] * (20 ** (len(sequence) - i - 1))
    return fp


class BMH2:

    def __init__(self, pattern: str, text: str, q: int = 20):
        self.pattern = pattern
        self.text = text
        self.q = q

        if len(pattern) < q:
            raise ValueError("Pattern length must be greater than or equal to q.")

    def _initialize_shift_table(self) -> dict[int, int]:
        """Initialize the shift table for the q-grams in the pattern."""
        D = {}
        m = len(self.pattern)
        for i in range(m - self.q + 1):
            q_gram = self.pattern[i:i + self.q]
            fp = fingerprint(q_gram)
            D[fp] = m - i - self.q
        return D

    def search(self) -> list[int]:
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


def test_bmh2_on_protein_file(filename: str, output_file: str):
    # Read protein sequence from the input file
    with open(filename, 'r') as file:
        protein_sequence = file.read().replace("\n", "").upper()

    # Open output file to store results
    with open(output_file, 'w') as output:
        output.write("Pattern Length\tTime (ms)\tMatches Found\n")

        pattern_sequences = [4,6,8,10,12,14,16,18,20,22,24,26,28,30,40,50,60,70,80,90,100]
        # Test patterns of lengths 4 to 40
        for pattern_length in pattern_sequences:
            # Generate a pattern of the desired length from the protein sequence
            pattern = protein_sequence[:pattern_length]

            # Skip if the protein sequence is shorter than the pattern length
            if len(pattern) < pattern_length:
                break

            bmh = BMH2(pattern, protein_sequence)

            # Measure execution time
            start_time = time.time()
            matches = bmh.search()
            end_time = time.time()

            elapsed_time_ms = (end_time - start_time) * 1000
            output.write(f"{pattern_length}\t{elapsed_time_ms:.2f}\t{len(matches)}\n")

            print(f"Pattern Length: {pattern_length}, Time: {elapsed_time_ms:.2f} ms, Matches Found: {len(matches)}")


def main():
    # Ask user to select the input protein file
    input_file = filedialog.askopenfilename(title="Select Aminoacid File", filetypes=[("Text Files", "*.txt")])
    if not input_file:
        print("No file selected. Exiting.")
        return

    # Output file for results
    output_file = "bmh2_aminoacid_test_results.txt"

    # Perform the tests
    test_bmh2_on_protein_file(input_file, output_file)

    print(f"Test results saved to {output_file}")


if __name__ == '__main__':
    main()

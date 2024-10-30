import numpy as np
from utils.utils import sort_and_order_frequencies


def split_frequencies(frequencies, codes, current_code=""):
    """
    Recursively splits the list of frequencies to assign Shannon-Fano codes.
    """
    if len(frequencies) == 1:
        # Assign final code when only one character remains
        codes[frequencies[0][0]] = current_code
        return

    # Find the split point where the two halves are as equal as possible
    total = sum(f[1] for f in frequencies)
    cumulative = 0
    split_idx = 0
    for i, (_, freq) in enumerate(frequencies):
        cumulative += freq
        if cumulative >= total / 2:
            split_idx = i
            break

    # Split and assign '0' to the first half and '1' to the second
    left = frequencies[:split_idx + 1]
    right = frequencies[split_idx + 1:]

    # Recursive calls for left and right halves
    split_frequencies(left, codes, current_code + "0")
    split_frequencies(right, codes, current_code + "1")


def shanon_fano(text: str) -> dict:
    frequencies = sort_and_order_frequencies(text)
    total_freq = sum(num for _, num in frequencies)

    # Initialize base matrix for analysis (if needed)
    base_matrix = np.zeros((len(frequencies), 2))
    for i in range(len(frequencies)):
        base_matrix[i, 0] = frequencies[i][1]
        base_matrix[i, 1] = frequencies[i][1] / total_freq
    print("Frequency and Probability Matrix:\n", base_matrix)

    # Create codes dictionary and recursively assign Shannon-Fano codes
    codes = {}
    split_frequencies(frequencies, codes)

    # Display each character's binary code
    print("Shannon-Fano Codes:")
    for char, code in codes.items():
        print(f"Character: {char}, Code: {code}")

    return codes


def __run__():
    text = "Jos sä tahdot niin tullen kalioden läpi"
    codes = shanon_fano(text)
    print("Encoded Text:", ''.join(codes[char] for char in text if char in codes))


if __name__ == '__main__':
    __run__()

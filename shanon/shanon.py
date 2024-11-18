import numpy as np
import math

from utils.utils import sort_and_order_frequencies
from binary_expansion.expansion import binary_expansion


def shanon(text: str) -> None:
    frequencies = sort_and_order_frequencies(text)
    total_freq = sum(num for _, num in frequencies)
    base_matrix = np.zeros((len(frequencies), 4))
    binaries = []
    for i in range(len(frequencies)):
        base_matrix[i, 0] = frequencies[i][1]
        base_matrix[i, 1] = frequencies[i][1] / total_freq
        base_matrix[i, 2] = 0 if i == 0 else base_matrix[i - 1, 1] + base_matrix[i - 1, 2]
        base_matrix[i, 3] = math.ceil(math.log2(1 / base_matrix[i, 1]))
        num = base_matrix[i, 2]
        binaries.append("".join(map(str, binary_expansion(float(num)))))

    print(base_matrix)
    print(binaries)
    lms = sum(base_matrix[:,1] * base_matrix[:,3])
    rc = 8/lms
    print(f"lms: {lms} , rc: {rc}")


def __run__():
    text = "Jos sä tahdot niin tullen kalioden läpi"
    shanon(text)


if __name__ == '__main__':
    __run__()

import numpy as np

from utils.utils import sort_and_order_frequencies


def shanon_fano(text: str) -> None:
    frequencies = sort_and_order_frequencies(text)
    total_freq = sum(num for _, num in frequencies)
    base_matrix = np.zeros((len(frequencies), 2))
    for i in range(len(frequencies)):
        base_matrix[i, 0] = frequencies[i][1]
        base_matrix[i, 1] = frequencies[i][1] / total_freq
    print(base_matrix)


def __run__():
    text = "Jos sä tahdot niin tullen kalioden läpi"
    shanon_fano(text)


if __name__ == '__main__':
    __run__()

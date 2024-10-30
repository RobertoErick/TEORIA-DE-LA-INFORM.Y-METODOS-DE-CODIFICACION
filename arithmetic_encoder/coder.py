import numpy as np

from utils.utils import sort_and_order_frequencies
from binary_expansion import expansion


def arithmetic_encoder(text: str, word: str) -> tuple:
    frequencies = sort_and_order_frequencies(text)
    frequency_sum = sum(frequency[1] for frequency in frequencies)
    sorted_values = sorted(frequencies, key=lambda x: (not x[0].isalpha(), x[0]))
    sorted_frequencies = [(i[0], i[1], i[1] / frequency_sum) for i in sorted_values]
    base_matrix = np.zeros((3, len(sorted_frequencies)))
    for i in range(len(sorted_frequencies)):
        base_matrix[0, i] = sorted_frequencies[i][2]
        base_matrix[1, i] = base_matrix[2, i - 1] if i != 0 else 0
        base_matrix[2, i] = base_matrix[0, i] + base_matrix[1, i]
    new_matrix = np.zeros((3, len(sorted_frequencies)))
    iteration = 0
    char_index = 0
    for char in word:
        for i in range(len(sorted_frequencies)):
            if char == sorted_frequencies[i][0]:
                char_index = i
                break
        for i in range(len(sorted_frequencies)):
            if iteration == 0:
                new_matrix[0, i] = base_matrix[0, i] * base_matrix[0, char_index]
                new_matrix[1, i] = new_matrix[2, i - 1] if i != 0 else base_matrix[1, char_index]
                new_matrix[2, i] = new_matrix[0, i] + new_matrix[1, i]
            else:
                new_matrix[0, i] = base_matrix[0, i] * new_matrix[0, char_index]
        if iteration == len(word) - 1:
            break
        else:
            iteration = iteration + 1
        print(f'{char} sum {sum(new_matrix[0, :])}')
    l = new_matrix[0, char_index]
    alpha = new_matrix[1, char_index]
    beta = new_matrix[2, char_index]
    return l, alpha, beta


def method_one(l: np.float64, alpha: np.float64, beta: np.float64) -> None:
    print(f"l : {l}")
    print(f"alpha : {alpha}")
    print(f"beta : {beta}")
    base_matrix = []
    t = 1
    while True:
        t_pow = pow(0.5, t)
        if not t_pow <= l:
            base_matrix.append((t,t_pow, 0))
        else:
            base_matrix.append((t,t_pow, 1))
            break
        t = t + 1
    left_value = base_matrix[len(base_matrix) - 1][1]
    mid_value = len(base_matrix)
    right_value = 2 **(-mid_value + 1)
    print(f"base matrix : {base_matrix}")
    print(f"t: {left_value} <= {mid_value} <= {right_value}")
    upper_x = 2 ** mid_value
    left_x = upper_x * alpha
    rounded_x = round(left_x)
    initial_value = rounded_x / upper_x
    expansion.binary_expansion(initial_value)


def method_two(l: np.float64, alpha: np.float64, beta: np.float64) -> None:
    print(f"l : {l}")
    print(f"alpha : {alpha}")
    print(f"beta : {beta}")
    expansion.binary_expansion(float(alpha))
    expansion.binary_expansion(float(beta))


def __run__():
    text = """
    Two roads diverged in a yellow wood,
    And sorry I could not travel both
    And be one traveler, long I stood
    And looked down one as far as I could
    To where it bent in the undergrowth;

    Then took the other, as just as fair,
    And having perhaps the better claim,
    Because it was grassy and wanted wear;
    Though as for that the passing there
    Had worn them really about the same,
     
    And both that morning equally lay
    In leaves no step had trodden black.
    Oh, I kept the first for another day!
    Yet knowing how way leads on to way,
    I doubted if I should ever come back.
     
    I shall be telling this with a sigh
    Somewhere ages and ages hence:
    Two roads diverged in a wood, and I
    I took the one less traveled by,
    And that has made all the difference.
    """
    word = "could"
    l, alpha, beta = arithmetic_encoder(text, word)
    print("Method 1")
    method_one(l, alpha, beta)
    print("Method 2")
    method_two(l, alpha, beta)


if __name__ == "__main__":
    __run__()

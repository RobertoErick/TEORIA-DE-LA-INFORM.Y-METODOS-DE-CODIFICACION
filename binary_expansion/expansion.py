

def binary_expansion(num: float, tolerance: float = 1e-10) -> list[int]:
    expansion = []
    history = []

    while True:
        if num >= float(1):
            num = (num - 1) * 2
        else:
            num *= 2
        bit = 1 if num >= float(1) else 0
        expansion.append((num, bit))

        # Check for repeated numbers with a tolerance
        if any(abs(num - h) < tolerance for h in history):
            break
        else:
            history.append(num)
    sequence = [num for _,num in expansion]
    return sequence


def __run__():
    binary_expansion(1 / 30)


if __name__ == '__main__':
    __run__()

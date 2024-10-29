

def binary_expansion(num: float, tolerance: float = 1e-10):
    num *= 2
    expansion = [(num, 0)]
    history = {num}

    while True:
        if num >= 1:
            num = (num - 1) * 2
            bit = 1
        else:
            num *= 2
            bit = 0

        expansion.append((num, bit))

        # Check for repeated numbers with a tolerance
        if any(abs(num - h) < tolerance for h in history):
            break
        else:
            history.add(num)

    print(expansion)


def __run__():
    binary_expansion(1 / 30)


if __name__ == '__main__':
    __run__()

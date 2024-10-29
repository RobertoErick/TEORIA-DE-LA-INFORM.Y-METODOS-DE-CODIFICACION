

def binary_expansion(num: float):
    num = num * 2
    expansion = [(num, 0)]
    history = [num]
    while True:
        if num >= 1:
            num = (num - 1) * 2
        else:
            num = num * 2
        if num >= 1:
            expansion.append((num, 1))
        else:
            expansion.append((num, 0))

        if num in history:
            break
        else:
            history.append(num)
    print(expansion)


def __run__():
    binary_expansion(1 / 30)


if __name__ == '__main__':
    __run__()

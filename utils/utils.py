import collections


def sort_and_order_frequencies(text: str) -> list[tuple[str, int]]:
    frequency = collections.Counter(text.replace(" ", "").replace("\n","").lower())
    return sorted(frequency.items(), key=lambda x: (-x[1], -ord(x[0])))

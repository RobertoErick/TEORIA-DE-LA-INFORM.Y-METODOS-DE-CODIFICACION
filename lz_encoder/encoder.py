class LZ77Tuple:
    def __init__(self, offset, length, char):
        self.offset = offset
        self.length = length
        self.char = char

    def __repr__(self):
        return f"({self.offset}, {self.length}, {repr(self.char)})"


def max_of_two(a : int, b : int) -> int:
    return a if a > b else b


def compress_lz77(history : str, lookahead : str) -> list[LZ77Tuple]:
    compressed_data = []
    window_size = len(history)
    i = 0

    while i < len(lookahead):
        best_match_distance = 0
        best_match_length = 0

        # Search for the longest match in the sliding window (history)
        for j in range(max_of_two(0, len(history) - window_size), len(history)):
            length = 0
            while length < len(lookahead) - i and history[j + length] == lookahead[i + length]:
                length += 1
            if length > best_match_length:
                best_match_distance = len(history) - j
                best_match_length = length

        # If a match is found, add a tuple (offset, length, next char)
        if best_match_length > 0 and i + best_match_length < len(lookahead):
            next_char = lookahead[i + best_match_length]
            compressed_data.append(LZ77Tuple(best_match_distance, best_match_length, next_char))
            i += best_match_length + 1
        else:
            # No match found, add a tuple with zero offset and length, and the current character
            compressed_data.append(LZ77Tuple(0, 0, lookahead[i]))
            i += 1

        # Update the history window
        if i < len(lookahead):
            history += lookahead[:i]
            if len(history) > window_size:
                history = history[len(history) - window_size:]

    return compressed_data


def slice_and_compress(input_str : str, n : int) -> None:
    # Ensure n does not exceed the length of input
    if n > len(input_str):
        n = len(input_str)

    new_text = input_str[:n]
    print(f"NewText: {new_text}")

    # Calculate the 2/3 and 1/3 split
    two_thirds_index = (2 * n) // 3
    history = new_text[:two_thirds_index]
    lookahead = new_text[two_thirds_index:]

    print(f"History: {history}")
    print(f"Lookahead: {lookahead}")

    # Apply LZ77 compression on history and lookahead
    compressed_data = compress_lz77(history, lookahead)

    # Print compressed data
    print("Compressed Data:")
    for tuple_ in compressed_data:
        print(tuple_)

    # Calculate memory size of compressed data
    memory_size_compressed = 0
    for tuple_ in compressed_data:
        memory_size_compressed += len(f"{tuple_.offset}{tuple_.length}{tuple_.char}")
    memory_size_original = len(new_text)

    print(f"Memory Size of Compressed Data: {memory_size_compressed}")
    print(f"Memory Size of Original Data: {memory_size_original}")

    # Compression ratio
    compression_ratio = memory_size_compressed / memory_size_original
    print(f"Compression Ratio: {compression_ratio:.2f}")


def run():
    input_str = "In radio c'è un pulcino In radio c'è un pulcino È il pulcino pio, è il pulcino pio E il pulcino pio, e il pulcino pio"
    plaque = "2077518"

    n = sum(int(digit) for digit in plaque)  # Sum of digits in plaque
    slice_and_compress(input_str, n)


if __name__ == "__main__":
    run()

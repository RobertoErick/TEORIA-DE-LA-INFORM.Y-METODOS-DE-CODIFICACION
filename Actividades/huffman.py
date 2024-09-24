import collections

import huffman

string = "Jos sä tahdot niin tullen kalioden läpi"

frequency = collections.Counter(string.replace(" ", "").lower())

input_ = sorted(frequency.items(), key=lambda x: (-x[1], -ord(x[0])))

output = huffman.codebook(input_)

print("Sorted :", input_)
print("Huffman :", output)
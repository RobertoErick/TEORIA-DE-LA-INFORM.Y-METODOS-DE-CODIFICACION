import huffman
import utils.utils as utils

text = "Jos sä tahdot niin tullen kalioden läpi"

frequencies = utils.sort_and_order_frequencies(text)

output = huffman.codebook(frequencies)

print("Sorted :", frequencies)
print("Huffman :", output)
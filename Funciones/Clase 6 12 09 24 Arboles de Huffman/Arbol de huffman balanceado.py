import heapq
from collections import defaultdict
from graphviz import Source

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequencies):
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def generate_codes(node, current_code="", codes={}):
    if node is not None:
        if node.char is not None:
            codes[node.char] = current_code
        generate_codes(node.left, current_code + "0", codes)
        generate_codes(node.right, current_code + "1", codes)
    return codes

def huffman_encoding(data):
    frequencies = defaultdict(int)
    for char in data:
        frequencies[char] += 1

    root = build_huffman_tree(frequencies)
    huffman_codes = generate_codes(root)

    encoded_data = ''.join(huffman_codes[char] for char in data)
    return encoded_data, huffman_codes, root

def huffman_decoding(encoded_data, huffman_codes):
    reverse_codes = {v: k for k, v in huffman_codes.items()}
    current_code = ""
    decoded_data = ""

    for bit in encoded_data:
        current_code += bit
        if current_code in reverse_codes:
            decoded_data += reverse_codes[current_code]
            current_code = ""

    return decoded_data

def visualize_tree(node, graph=None):
    if graph is None:
        graph = Source('digraph G {\n')
    
    if node is not None:
        if node.char is not None:
            graph.node(str(id(node)), f"{node.char}\n{node.freq}")
        else:
            graph.node(str(id(node)), f"({node.freq})")
        
        if node.left:
            graph.edge(str(id(node)), str(id(node.left)))
            visualize_tree(node.left, graph)
        if node.right:
            graph.edge(str(id(node)), str(id(node.right)))
            visualize_tree(node.right, graph)

    return graph

if __name__ == "__main__":
    data = "hola mundo, este es un ejemplo de compresión de Huffman"
    encoded_data, huffman_codes, root = huffman_encoding(data)

    print("Códigos de Huffman:", huffman_codes)
    print("Datos codificados:", encoded_data)

    decoded_data = huffman_decoding(encoded_data, huffman_codes)
    print("Datos decodificados:", decoded_data)

    # Visualizar el árbol de Huffman
    graph = visualize_tree(root)
    graph.render("huffman_tree", format='png', cleanup=True)  # Guardar como imagen
    graph.view()  # Abrir la imagen generada

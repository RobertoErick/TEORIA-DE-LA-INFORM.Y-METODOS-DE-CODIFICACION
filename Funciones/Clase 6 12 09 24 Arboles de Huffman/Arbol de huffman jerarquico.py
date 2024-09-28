import heapq
from collections import Counter, namedtuple
import pydot
from graphviz import Source

# Nodo de Huffman
class Node(namedtuple('Node', ['left', 'right'])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")

# Hoja del árbol de Huffman
class Leaf(namedtuple('Leaf', ['char'])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"

# Construir el Árbol de Huffman
def huffman_tree(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)
    
    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1
    return h[0][-1]

# Codificar los caracteres usando el Árbol de Huffman
def huffman_code(tree):
    code = {}
    tree.walk(code, "")
    return code

# Función para visualizar el Árbol de Huffman
def visualize_huffman_tree(tree, filename='Arbol de huffman jerarquico'):
    graph = pydot.Dot(graph_type='graph')

    def add_edges(node, parent=None):
        if isinstance(node, Leaf):
            label = f'"{node.char}"'
            graph.add_node(pydot.Node(label, shape='ellipse'))
            if parent:
                graph.add_edge(pydot.Edge(parent, label))
        else:
            internal_node = f'Node_{id(node)}'
            graph.add_node(pydot.Node(internal_node, shape='circle'))
            if parent:
                graph.add_edge(pydot.Edge(parent, internal_node))
            add_edges(node.left, internal_node)
            add_edges(node.right, internal_node)

    add_edges(tree)
    graph.write_png(f"{filename}.png")
    print(f"Árbol de Huffman guardado como {filename}.png")

# Texto a comprimir
text = "Jos sä tahdot niin tullen kalioden läpi"

# Crear el árbol de Huffman y obtener el código
tree = huffman_tree(text)
code = huffman_code(tree)

# Visualizar y guardar el Árbol de Huffman
visualize_huffman_tree(tree)

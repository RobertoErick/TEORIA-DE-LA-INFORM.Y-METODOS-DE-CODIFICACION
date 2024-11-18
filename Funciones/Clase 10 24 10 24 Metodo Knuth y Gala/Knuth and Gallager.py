import matplotlib.pyplot as plt
import networkx as nx

class HuffmanNode:
    def __init__(self, symbol=None, weight=0, parent=None, left=None, right=None):
        self.symbol = symbol        # Símbolo asociado con este nodo
        self.weight = weight        # Frecuencia (peso) del nodo
        self.parent = parent        # Nodo padre
        self.left = left            # Hijo izquierdo
        self.right = right          # Hijo derecho
        self.is_leaf = True if symbol is not None else False

class AdaptiveHuffmanTree:
    def __init__(self):
        self.root = HuffmanNode()    # Nodo raíz del árbol
        self.nodes = {}              # Mapa de símbolos a nodos del árbol
        self.leaves = {}             # Mapa de hojas asociadas a símbolos

    def initialize_tree(self, symbols):
        for symbol in symbols:
            node = HuffmanNode(symbol, weight=1)
            self.nodes[symbol] = node
            self.leaves[symbol] = node

    def update_tree(self, symbol):
        if symbol not in self.leaves:
            raise ValueError(f"Símbolo {symbol} no encontrado en el árbol")

        node = self.leaves[symbol]
        self.increment_weight(node)

        while node is not None:
            self.fix_tree(node)
            node = node.parent

    def increment_weight(self, node):
        node.weight += 1
        if node.parent:
            self.increment_weight(node.parent)

    def fix_tree(self, node):
        node_to_swap = self.find_highest_equal_weight(node)
        if node_to_swap is not None and node_to_swap != node:
            self.swap_nodes(node, node_to_swap)

    def find_highest_equal_weight(self, node):
        for symbol, candidate_node in self.nodes.items():
            if candidate_node.weight == node.weight and candidate_node != node:
                return candidate_node
        return None

    def swap_nodes(self, node1, node2):
        node1.symbol, node2.symbol = node2.symbol, node1.symbol
        self.nodes[node1.symbol] = node1
        self.nodes[node2.symbol] = node2

    def plot_tree(self):
        graph = nx.DiGraph()  # Usamos un gráfico dirigido para el árbol

        def add_edges(node, graph, pos, x=0, y=0, layer=1):
            if node:
                pos[node] = (x, y)
                if node.left:
                    graph.add_edge(node, node.left)
                    add_edges(node.left, graph, pos, x - 1 / layer, y - 1, layer + 1)
                if node.right:
                    graph.add_edge(node, node.right)
                    add_edges(node.right, graph, pos, x + 1 / layer, y - 1, layer + 1)

        pos = {}
        add_edges(self.root, graph, pos)

        labels = {node: f"{node.symbol}:{node.weight}" if node.symbol else f"{node.weight}" for node in graph.nodes()}
        nx.draw(graph, pos, labels=labels, with_labels=True, node_size=2000, node_color="skyblue", font_size=10, font_weight="bold")
        plt.show()

# Ejemplo de uso
symbols = ['a', 'b', 'c', 'd', 'e']
huffman_tree = AdaptiveHuffmanTree()
huffman_tree.initialize_tree(symbols)

# Procesa los símbolos en orden y grafica
sequence = ['a', 'b', 'a', 'c', 'a', 'b', 'd']
for symbol in sequence:
    print(f"Procesando símbolo: {symbol}")
    huffman_tree.update_tree(symbol)
    huffman_tree.plot_tree()  # Muestra el árbol después de cada actualización

import heapq  # Para manejar una lista ordenada (min heap) de frecuencias.
from graphviz import Digraph  # Para la representación gráfica del árbol

# Clase para representar un nodo del árbol de Huffman
class NodoHuffman:
    def __init__(self, simbolo=None, frecuencia=0, hijos=None):
        self.simbolo = simbolo        # El símbolo o carácter
        self.frecuencia = frecuencia  # Frecuencia del símbolo
        self.hijos = hijos if hijos else []  # Lista de hijos (para nodos ternarios)

    # Método para hacer que los nodos sean comparables (por frecuencia) en el heap
    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia

# Función para construir el árbol de Huffman ternario
def construir_arbol_ternario(frecuencias):
    # Crear una lista de nodos hoja a partir de las frecuencias
    heap = [NodoHuffman(simbolo, frecuencia) for simbolo, frecuencia in frecuencias.items()]
    
    # Crear un min-heap (cola de prioridad) para manejar los nodos
    heapq.heapify(heap)
    
    # Mientras haya más de un nodo en el heap
    while len(heap) > 1:
        # Extraer los tres nodos con menor frecuencia
        nodos = []
        for _ in range(min(3, len(heap))):  # Tomamos 3 nodos o menos si hay menos disponibles
            nodos.append(heapq.heappop(heap))
        
        # Crear un nuevo nodo que sea el padre de estos tres nodos
        nueva_frecuencia = sum(nodo.frecuencia for nodo in nodos)
        nuevo_nodo = NodoHuffman(frecuencia=nueva_frecuencia, hijos=nodos)
        
        # Insertar el nuevo nodo en el heap
        heapq.heappush(heap, nuevo_nodo)
    
    # El último nodo en el heap es la raíz del árbol
    return heap[0]

# Función para asignar códigos Huffman ternarios a los símbolos
def asignar_codigos(nodo, codigo_actual="", codigos={}):
    if nodo.simbolo is not None:
        # Si es una hoja, asignamos el código al símbolo
        codigos[nodo.simbolo] = codigo_actual
    else:
        # Si no es una hoja, seguimos recorriendo sus hijos
        for i, hijo in enumerate(nodo.hijos):
            asignar_codigos(hijo, codigo_actual + str(i), codigos)
    
    return codigos

# Función para imprimir el árbol usando Graphviz
def graficar_arbol_huffman(nodo, dot=None, parent=None, label=''):
    if dot is None:
        dot = Digraph()

    # Crear una etiqueta para cada nodo (si es hoja, mostrar símbolo y frecuencia)
    node_label = f'{nodo.simbolo if nodo.simbolo else ""}\n{nodo.frecuencia}'
    dot.node(str(id(nodo)), node_label)

    # Si hay un nodo padre, conectar este nodo con el padre
    if parent is not None:
        dot.edge(str(id(parent)), str(id(nodo)), label=label)

    # Recorrer los hijos (hasta 3) del nodo actual
    for i, hijo in enumerate(nodo.hijos):
        graficar_arbol_huffman(hijo, dot, nodo, label=str(i))

    return dot

# Ejemplo de uso
if __name__ == "__main__":
    # Frecuencias de ejemplo
    frecuencias = {
        'i': 4,
        'l': 4,
        'n': 4,
        'o': 3,
        't': 3,
        'a': 2,
        'á': 2,
        'd': 2,
        'e': 2,
        's': 2,
        'h': 1,
        'i': 1,
        'k': 1,
        'p': 1,
        'u': 1
    }
    
    # Construir el árbol de Huffman ternario
    arbol_huffman_ternario = construir_arbol_ternario(frecuencias)
    
    # Asignar los códigos Huffman a los símbolos
    codigos_huffman = asignar_codigos(arbol_huffman_ternario)
    
    # Mostrar los códigos de cada símbolo
    print("Códigos Huffman ternarios:")
    for simbolo, codigo in codigos_huffman.items():
        print(f"Símbolo: {simbolo}, Código: {codigo}")
    
    # Graficar el árbol de Huffman
    dot = graficar_arbol_huffman(arbol_huffman_ternario)
    dot.render("Arbol de Huffman terniario", format="png", cleanup=False)  # Guardar en archivo PNG

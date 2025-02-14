from typing import List, Optional, Union
import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Клас для представлення вузла дерева
class TreeNode:
    def __init__(self, key):
        self.val = key
        self.id = str(uuid.uuid4())
        self.left: Optional["TreeNode"] = None
        self.right: Optional["TreeNode"] = None

# Функція для побудови дерева з списку значень
# None означає відсутність вузла

def build_tree_from_list(values: List[Union[int, None]]) -> Optional[TreeNode]:
    if not values:
        return None

    nodes: List[Optional[TreeNode]] = [
        TreeNode(val) if val is not None else None for val in values]

    for i in range(len(nodes)):
        node = nodes[i]
        if node is not None:
            left_idx, right_idx = 2 * i + 1, 2 * i + 2

            if left_idx < len(nodes) and nodes[left_idx] is not None:
                node.left = nodes[left_idx]
            if right_idx < len(nodes) and nodes[right_idx] is not None:
                node.right = nodes[right_idx]

    return nodes[0] if nodes else None

# Додавання вузлів та зв'язків між ними до графа

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node:
        graph.add_node(node.id, label=node.val)
        pos[node.id] = (x, y)

        if node.left:
            graph.add_edge(node.id, node.left.id)
            add_edges(graph, node.left, pos, x - 1 /
                      2 ** layer, y - 1, layer + 1)

        if node.right:
            graph.add_edge(node.id, node.right.id)
            add_edges(graph, node.right, pos, x + 1 /
                      2 ** layer, y - 1, layer + 1)

    return graph

# Функція для генерації кольорів для вузлів при обході дерева

def generate_color(index, total):
    if total == 0:
        return "#CCCCCC"
    blue = 240
    red = int(18 + (index / max(total, 1)) * 150)
    green = int(80 + (index / max(total, 1)) * 150)
    return f'#{red:02X}{green:02X}{blue:02X}'

# Функція для візуалізації дерев після обходів DFS та BFS

def draw_dual_trees(graph_dfs, graph_bfs, pos_dfs, pos_bfs, visited_dfs, visited_bfs):
    labels_dfs = {node_id: data.get('label', '') for node_id, data in graph_dfs.nodes(data=True)}
    labels_bfs = {node_id: data.get('label', '') for node_id, data in graph_bfs.nodes(data=True)}

    color_map_dfs = {n: "#CCCCCC" for n in graph_dfs.nodes}
    color_map_bfs = {n: "#CCCCCC" for n in graph_bfs.nodes}

    for i, node_id in enumerate(visited_dfs):
        color_map_dfs[node_id] = generate_color(i, len(visited_dfs))

    for i, node_id in enumerate(visited_bfs):
        color_map_bfs[node_id] = generate_color(i, len(visited_bfs))

    colors_dfs = [color_map_dfs[n] for n in graph_dfs.nodes]
    colors_bfs = [color_map_bfs[n] for n in graph_bfs.nodes]

    plt.figure(figsize=(14, 6))

    plt.subplot(1, 2, 1)
    plt.title("Обхід у глибину (DFS)")
    nx.draw(graph_dfs, pos=pos_dfs, labels=labels_dfs,
            node_color=colors_dfs, arrows=False, node_size=2500)

    plt.subplot(1, 2, 2)
    plt.title("Обхід у ширину (BFS)")
    nx.draw(graph_bfs, pos=pos_bfs, labels=labels_bfs,
            node_color=colors_bfs, arrows=False, node_size=2500)

    plt.show()

# Функція для обходу дерева в глибину (DFS)

def dfs_traversal(root):
    if not root:
        return []

    stack, visited = [root], []
    while stack:
        node = stack.pop()
        visited.append(node.id)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return visited

# Функція для обходу дерева в ширину (BFS)

def bfs_traversal(root):
    if not root:
        return []

    queue = deque([root])
    visited = []

    while queue:
        node = queue.popleft()
        visited.append(node.id)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return visited

# Початковий список значень для побудови дерева
values: List[Union[int, None]] = [10, 8, 9, 7, 6, 5, 4]

# Створення дерева
root = build_tree_from_list(values)

# Створення графів для DFS та BFS
graph_dfs, graph_bfs = nx.DiGraph(), nx.DiGraph()
pos_dfs, pos_bfs = {}, {}

# Додавання зв'язків до графа
graph_dfs = add_edges(graph_dfs, root, pos_dfs, x=0)
graph_bfs = add_edges(graph_bfs, root, pos_bfs, x=0)

# Виконання обходів
visited_dfs = dfs_traversal(root)
visited_bfs = bfs_traversal(root)

# Візуалізація результатів обходу
draw_dual_trees(graph_dfs, graph_bfs, pos_dfs, pos_bfs, visited_dfs, visited_bfs)

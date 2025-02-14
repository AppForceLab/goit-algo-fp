import heapq

def dijkstra(graph, start):
    # Ініціалізація відстаней: безкінечність для всіх, крім стартової вершини
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Пріоритетна черга (бінарна купа) для вибору вершини з найменшою відстанню
    priority_queue = [(0, start)]  # (відстань, вершина)
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Пропускаємо, якщо вже знайшли коротший шлях
        if current_distance > distances[current_node]:
            continue
        
        # Переглядаємо сусідів поточної вершини
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Якщо знайдено коротший шлях до сусіда, оновлюємо його
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Приклад зваженого графа (у вигляді списку суміжності)
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Запуск алгоритму з вершини 'A'
start_node = 'A'
shortest_paths = dijkstra(graph, start_node)
print(shortest_paths)
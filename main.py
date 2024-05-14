import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def dfs_paths(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    result = [vertex]  # Відвідуємо вершину
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            result += dfs_paths(graph, neighbor, visited)
    return result

def bfs_paths(graph, queue, visited=None):
    # Перевіряємо, чи існує множина відвіданих вершин, якщо ні, то ініціалізуємо нову
    if visited is None:
        visited = set()
    result = [] #створюємо пустий список result, де зберігаємо результати обходу графа
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            result.append(vertex)
            visited.add(vertex)
            queue.extend(set(graph.neighbors(vertex)) - visited)
    return result

# Створення графа
G = nx.Graph()

# Додавання вершин (столиці Європи)
capitals = ["Париж", "Лондон", "Рим", "Мадрид", "Берлін", "Амстердам"]

G.add_nodes_from(capitals)

# Додавання ребер (воздушне сполучення) та їх ваг (відстань)
# Приберемо декілька шляхів даби ускладнити прорахування маршрутів :)
# G.add_edge("Париж", "Лондон", weight=344)
G.add_edge("Париж", "Рим", weight=1105)
# G.add_edge("Париж", "Мадрид", weight=1059)
G.add_edge("Париж", "Берлін", weight=878)
G.add_edge("Париж", "Амстердам", weight=431)
# G.add_edge("Лондон", "Рим", weight=1443)
G.add_edge("Лондон", "Мадрид", weight=1269)
G.add_edge("Лондон", "Берлін", weight=933)
G.add_edge("Лондон", "Амстердам", weight=356)
G.add_edge("Рим", "Мадрид", weight=1420)
G.add_edge("Рим", "Берлін", weight=1181)
G.add_edge("Рим", "Амстердам", weight=1371)
G.add_edge("Мадрид", "Берлін", weight=1672)
G.add_edge("Мадрид", "Амстердам", weight=1446)
# G.add_edge("Берлін", "Амстердам", weight=577)

# Візуалізація графа
pos = nx.spring_layout(G)  # Позиціонування вершин
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_weight="bold")
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.title("Воздушне сполучення між столицями Європи")
plt.show()

# Аналіз основних характеристик
print("Кількість вершин:", G.number_of_nodes())
print("Кількість ребер:", G.number_of_edges())

# Ступінь вершин
degree = dict(G.degree())
print("Ступінь вершин:")
for capital, deg in degree.items():
    print(capital, ":", deg)


# Знаходження шляхів за допомогою DFS та BFS
start = "Париж"

# Алгоритм Дейкстри
shortest_paths = nx.single_source_dijkstra_path(G, source=start)
shortest_path_lengths = nx.single_source_dijkstra_path_length(G, source=start)

print(f"Довжини найкоротших шляхів: {shortest_path_lengths}")
print(f"Найкоротші шляхи від Парижа до інших вершин:")
for node, distance in shortest_paths.items():
    print(f"{node}: {distance}")
print("")

dfs_result = dfs_paths(G, start)
print("DFS Result:", dfs_result)

bfs_result = bfs_paths(G, deque([start]))
print("BFS Result:", bfs_result)

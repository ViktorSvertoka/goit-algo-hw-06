import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
stations = ["Депо", "Вишенька", "Яблунька", "Центральна", "Березка", "Гайок"]
G.add_nodes_from(stations)


edges = [
    ("Депо", "Вишенька", 1),
    ("Вишенька", "Яблунька", 2),
    ("Яблунька", "Центральна", 1),
    ("Центральна", "Березка", 3),
    ("Березка", "Гайок", 2),
    ("Гайок", "Депо", 4),
    ("Депо", "Центральна", 5),
]

G.add_weighted_edges_from(edges)

# Запуск алгоритму Дейкстри для всіх пар вершин
shortest_paths = dict(nx.all_pairs_dijkstra_path(G))
shortest_distances = dict(nx.all_pairs_dijkstra_path_length(G))

# Виведення результатів
print("Найкоротші шляхи між усіма парами вершин:")
for source in shortest_paths:
    for target in shortest_paths[source]:
        path = shortest_paths[source][target]
        distance = shortest_distances[source][target]
        print(f"Від {source} до {target}: шлях {path}, відстань {distance}")

# Візуалізація графа
pos = nx.circular_layout(G)
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="lightgreen",
    node_size=2000,
    edge_color="blue",
    font_size=15,
    font_color="darkgreen",
)

# Відображення ваг ребер на графі
edge_labels = {(u, v): f'{d["weight"]}' for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Схема дитячої залізниці з вагами ребер")
plt.show()

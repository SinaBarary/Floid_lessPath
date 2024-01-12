import networkx as nx
import matplotlib.pyplot as plt


def floyd_warshall(graph):
    """
    پیاده‌سازی الگوریتم فلوید وارشال
    :param graph: یک دیکشنری شامل گراف وزن‌دار به صورت:
                  {'node1': {'node2': weight, 'node3': weight, ...}, ...}
    :return: یک دیکشنری شامل کوتاه‌ترین فاصله‌ها بین هر زوج راس
    """
    vertices = graph.keys()
    dist = {v: {w: float('inf') if v != w else 0 for w in vertices} for v in vertices}

    for v in vertices:
        for w, weight in graph[v].items():
            dist[v][w] = weight

    for k in vertices:
        for i in vertices:
            for j in vertices:
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

def input_graph():
    graph = {}
    
    num_nodes = int(input("Enter the number of graph vertices : "))
    for _ in range(num_nodes):
        node = input(f"name of vertice : {len(graph) + 1} : ")
        graph[node] = {}

    while True:
        start_node = input("Start vertex name (enter 'exit' to finish) :")
        if start_node.lower() == 'exit':
            break

        end_node = input("The name of the end : ")
        weight = float(input("Enter the edge weight between these two vertices : "))
        
        if start_node in graph and end_node in graph:
            graph[start_node][end_node] = weight
            graph[end_node][start_node] = weight  # این خط را برای گراف بدون جهت حذف کنید

    return graph

def draw_graph(graph):
    G = nx.Graph()
    
    # اضافه کردن یال‌ها و وزن‌ها به گراف
    for node, edges in graph.items():
        for target, weight in edges.items():
            G.add_edge(node, target, weight=weight)

    pos = nx.spring_layout(G)  # تعیین موقعیت‌های راس‌ها
    labels = nx.get_edge_attributes(G, 'weight')  # دریافت وزن‌های یال‌ها

    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, edge_color='gray', linewidths=1, font_size=15, font_color='black', font_weight='bold', arrows=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.title("Floyd-Warshall Algorithm Visualization")
    plt.show()


# example:
graph_example = {
    'A': {'B': 3, 'C': 8},
    'B': {'A': 3, 'C': 1},
    'C': {'A': 8, 'B': 1},
}

graph_input = input_graph()
draw_graph(graph_input)
print(floyd_warshall(graph_input))

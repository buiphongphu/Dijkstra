from graph import dijkstra  # Import thuật toán Dijkstra từ file graph.py
import networkx as nx  # Import NetworkX để tạo và vẽ đồ thị
import matplotlib.pyplot as plt  # Import Matplotlib để hiển thị đồ thị

# Định nghĩa đồ thị dưới dạng dictionary.
# Mỗi đỉnh (vertex) trong đồ thị được liên kết với một dictionary khác,
# trong đó khóa là các đỉnh lân cận và giá trị là trọng số của cạnh nối giữa hai đỉnh.
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Định nghĩa đỉnh bắt đầu (đỉnh gốc) cho thuật toán Dijkstra
start_vertex = 'A'

# Gọi hàm Dijkstra để tính toán khoảng cách ngắn nhất từ đỉnh bắt đầu đến tất cả các đỉnh khác
distances = dijkstra(graph, start_vertex)


# Hàm để vẽ đồ thị
def draw_graph(graph, title):
    """
    Vẽ đồ thị từ cấu trúc đồ thị được định nghĩa dưới dạng dictionary.

    Parameters:
    - graph: Dictionary chứa thông tin về đồ thị, trong đó các đỉnh là các khóa và
             giá trị là các dictionary chứa các đỉnh lân cận và trọng số của cạnh.
    - title: Tiêu đề của đồ thị để hiển thị trên cửa sổ vẽ đồ thị.
    """
    G = nx.Graph()  # Tạo một đối tượng đồ thị không có hướng từ NetworkX

    # Thêm các cạnh và trọng số vào đồ thị
    for vertex, edges in graph.items():
        for edge, weight in edges.items():
            G.add_edge(vertex, edge, weight=weight)

    pos = nx.spring_layout(G)  # Tạo bố cục cho đồ thị để các đỉnh và cạnh được bố trí hợp lý
    edge_labels = nx.get_edge_attributes(G, 'weight')  # Lấy các trọng số của các cạnh để hiển thị

    plt.figure(figsize=(12, 6))  # Tạo một hình mới với kích thước cụ thể
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)  # Vẽ các nhãn trọng số trên các cạnh
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='cyan')  # Vẽ đồ thị với các đỉnh và cạnh
    plt.title(title)  # Đặt tiêu đề cho đồ thị
    plt.show()  # Hiển thị đồ thị


# Vẽ đồ thị ban đầu
draw_graph(graph, 'Đồ thị ban đầu')


# Hàm để vẽ đồ thị với các đường đi ngắn nhất
def highlight_shortest_paths(graph, distances, start):
    """
    Vẽ đồ thị và làm nổi bật các đường đi ngắn nhất từ đỉnh bắt đầu.

    Parameters:
    - graph: Dictionary chứa thông tin về đồ thị.
    - distances: Dictionary chứa khoảng cách ngắn nhất từ đỉnh bắt đầu đến các đỉnh khác.
    - start: Đỉnh bắt đầu cho thuật toán Dijkstra.
    """
    G = nx.Graph()  # Tạo một đối tượng đồ thị không có hướng từ NetworkX

    # Thêm các cạnh và trọng số vào đồ thị
    for vertex, edges in graph.items():
        for edge, weight in edges.items():
            G.add_edge(vertex, edge, weight=weight)

    # Tạo một dict chứa các đường đi ngắn nhất từ đỉnh bắt đầu
    shortest_paths = {start: 0}
    for vertex, distance in distances.items():
        if vertex != start:
            shortest_paths[vertex] = distance

    # Tạo một danh sách chứa các cạnh ngắn nhất
    shortest_edges = set()
    for vertex in shortest_paths:
        # Tìm các cạnh ngắn nhất từ đỉnh bắt đầu
        for neighbor, weight in graph[vertex].items():
            if vertex in shortest_paths and shortest_paths[vertex] + weight == distances.get(neighbor, float('inf')):
                shortest_edges.add((vertex, neighbor))

    # Vẽ đồ thị với các cạnh ngắn nhất được nổi bật
    pos = nx.spring_layout(G)  # Tạo bố cục cho đồ thị
    edge_labels = nx.get_edge_attributes(G, 'weight')  # Lấy các trọng số của các cạnh để hiển thị

    plt.figure(figsize=(12, 6))  # Tạo một hình mới với kích thước cụ thể
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)  # Vẽ các nhãn trọng số trên các cạnh
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='cyan')  # Vẽ đồ thị với các đỉnh và cạnh
    nx.draw_networkx_edges(G, pos, edgelist=shortest_edges, edge_color='red', width=2)  # Nổi bật các cạnh ngắn nhất
    plt.title('Đồ thị với các đường đi ngắn nhất từ đỉnh ' + start)  # Đặt tiêu đề cho đồ thị
    plt.show()  # Hiển thị đồ thị


# Vẽ đồ thị với các đường đi ngắn nhất
highlight_shortest_paths(graph, distances, start_vertex)

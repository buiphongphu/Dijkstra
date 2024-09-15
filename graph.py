import heapq  # Import heapq để sử dụng hàng đợi ưu tiên (priority queue) cho thuật toán Dijkstra


def dijkstra(graph, start):
    """
    Hàm Dijkstra tìm đường đi ngắn nhất từ đỉnh `start` đến tất cả các đỉnh khác trong đồ thị `graph`.

    Args:
    - graph: Đồ thị được biểu diễn dưới dạng dictionary.
      Mỗi khóa là một đỉnh, giá trị tương ứng là một dictionary khác chứa các đỉnh kề và trọng số của cạnh nối.
    - start: Đỉnh bắt đầu (đỉnh gốc) từ đó cần tính toán khoảng cách ngắn nhất đến các đỉnh khác.

    Returns:
    - distances: Dictionary lưu trữ khoảng cách ngắn nhất từ đỉnh `start` đến mỗi đỉnh khác trong đồ thị.
    """

    # Khởi tạo hàng đợi ưu tiên (priority queue) với khoảng cách từ đỉnh bắt đầu đến chính nó là 0
    queue = [(0, start)]

    # Dictionary để lưu khoảng cách ngắn nhất từ đỉnh bắt đầu đến mỗi đỉnh
    distances = {start: 0}

    # Vòng lặp chính để xử lý từng đỉnh trong hàng đợi
    while queue:
        # Lấy đỉnh có khoảng cách nhỏ nhất từ hàng đợi
        (current_distance, current_vertex) = heapq.heappop(queue)

        # Nếu khoảng cách hiện tại lớn hơn khoảng cách đã lưu, bỏ qua đỉnh này
        if current_distance > distances[current_vertex]:
            continue

        # Kiểm tra các đỉnh kề của đỉnh hiện tại
        for neighbor, weight in graph[current_vertex].items():
            # Tính khoảng cách từ đỉnh bắt đầu đến đỉnh kề qua đỉnh hiện tại
            distance = current_distance + weight

            # Nếu khoảng cách này nhỏ hơn khoảng cách đã biết, cập nhật khoảng cách và thêm vào hàng đợi
            if neighbor not in distances or distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    # Trả về dictionary chứa khoảng cách ngắn nhất từ đỉnh bắt đầu đến mỗi đỉnh khác
    return distances

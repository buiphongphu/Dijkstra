# Dijkstra Algorithm Implementation

## Mô tả

Dự án này cung cấp một triển khai cơ bản của thuật toán Dijkstra, được sử dụng để tìm đường đi ngắn nhất từ một đỉnh đến tất cả các đỉnh khác trong đồ thị có trọng số dương. Đây là một bài toán phổ biến trong lý thuyết đồ thị và có ứng dụng rộng rãi trong các hệ thống định tuyến, tìm kiếm đường đi, và các bài toán tối ưu hóa khác.

## Cấu trúc thư mục
```angular2html
dijkstra/
├── main.py: File chính chạy thuật toán Dijkstra
├── graph.py: Chứa định nghĩa về đồ thị và hàm Dijkstra 
├── requirements.txt: Danh sách các thư viện cần thiết (nếu có)
├── venv/: Môi trường ảo Python (không bắt buộc, nếu đã tạo)
└── README.md: Mô tả về bài toán và cách chạy chương trình
```

## Yêu cầu hệ thống

- **Python:** Phiên bản 3.x
- **Thư viện:** Không yêu cầu thư viện bên ngoài, nếu có thể cài đặt qua `requirements.txt`

## Cài đặt

### Bước 1: Tải và cài đặt Python

Đảm bảo rằng Python đã được cài đặt trên máy tính của bạn. Bạn có thể tải xuống Python từ [trang chính thức của Python](https://www.python.org/downloads/).

### Bước 2: Tạo và kích hoạt môi trường ảo (không bắt buộc)

Môi trường ảo giúp cô lập các thư viện mà bạn cài đặt cho dự án. Để tạo và kích hoạt môi trường ảo:

```bash
# Chạy lệnh này trong thư mục dijkstra/
python -m venv venv

# Kích hoạt môi trường ảo:
venv\Scripts\activate

```

### Bước 3: Cài đặt các thư viện cần thiết
```
pip install -r requirements.txt
```
### Bước 4: Chạy chương trình
``` bash
# Để chạy thuật toán Dijkstra:
python main.py
```
Chương trình sẽ thực thi và in ra kết quả đường đi ngắn nhất từ đỉnh xuất phát đến tất cả các đỉnh khác trong đồ thị.

# Cách hoạt động

- **graph.py**: Chứa định nghĩa về lớp đồ thị (Graph) và hàm dijkstra() để tính toán đường đi ngắn nhất.
- **main.py**: Thiết lập đồ thị, xác định các đỉnh và cạnh, và gọi hàm dijkstra() để thực thi thuật toán và hiển thị kết quả.

## Ví dụ
Giả sử bạn có đồ thị như sau:
- **Các đỉnh**: A, B, C, D
- **Các cạnh**: A-B (1), A-C (3), B-C (1), B-D (2), C-D (4)

Chương trình sẽ tìm đường đi ngắn nhất từ đỉnh A đến tất cả các đỉnh khác:
```
Khoảng cách ngắn nhất từ A: {'A': 0, 'B': 1, 'C': 2, 'D': 3}
```
Ảnh minh họa:

![Dijkstra Algorithm](https://upload.wikimedia.org/wikipedia/commons/5/57/Dijkstra_Animation.gif)


# Giải thuật

**Thuật toán Dijkstra** là một thuật toán tham lam được sử dụng để giải quyết bài toán đường đi ngắn nhất trong đồ thị. Nó hoạt động bằng cách lặp đi lặp lại:

**1.** Khởi tạo khoảng cách của tất cả các đỉnh từ đỉnh xuất phát là vô hạn, ngoại trừ đỉnh xuất phát với khoảng cách là 0.

**2.** Chọn đỉnh chưa được xử lý có khoảng cách nhỏ nhất và cập nhật khoảng cách của các đỉnh lân cận nếu có thể tìm được đường đi ngắn hơn.

**3.** Lặp lại quá trình cho đến khi tất cả các đỉnh đã được xử lý.

**Độ phức tạp thời gian**: O(V^2) với V là số lượng đỉnh. Nếu sử dụng hàng đợi ưu tiên, độ phức tạp có thể giảm xuống O((V + E) log V).
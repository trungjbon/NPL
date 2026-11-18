# 1. Giải thích các bước triển khai
## Phần 1: Khám phá Tensor

- Tạo Tensor:
  - Từ list Python, NumPy array, hoặc tạo ngẫu nhiên bằng torch.ones_like() và torch.rand_like().

- Kiểm tra thuộc tính Tensor:
  - In ra shape, dtype, và device để hiểu nơi lưu trữ dữ liệu.

- Thực hiện các phép toán:
  - Cộng, nhân vô hướng, nhân ma trận (@) thể hiện tính toán vector hóa.

- Indexing và Slicing:
  - Truy cập phần tử bằng cú pháp tensor[i, j] tương tự NumPy.

- Thay đổi hình dạng:
  - Dùng reshape() để thay đổi kích thước tensor mà không thay đổi dữ liệu.
 
## Phần 2: Tự động tính đạo hàm với Autograd
- Khởi tạo tensor với requires_grad=True.

- Thực hiện chuỗi phép toán (y = x + 2, z = y * y * 3).

- Gọi z.backward() để tính đạo hàm tự động.

- Truy cập kết quả qua x.grad
=> Với z = 3(x+2)^2 và x=1, ta có dz/dx = 18.

## Phần 3: Xây dựng mô hình đầu tiên với torch.nn
- Lớp nn.Linear:
  - Thực hiện phép biến đổi tuyến tính y = x(A^T) + b

- Lớp nn.Embedding:
  - Biểu diễn chỉ số từ thành vector đặc trưng có ý nghĩa.

- Xây dựng nn.Module:
  - Định nghĩa lớp MyFirstModel gồm các tầng: Embedding -> Linear -> ReLU -> Linear.
  - Định nghĩa hàm forward() mô tả luồng dữ liệu.
  - Truyền dữ liệu mẫu qua mô hình để kiểm tra kích thước đầu ra.
 
# 2. Hướng dẫn chạy mã
## Cài đặt thư viện cần thiết
```
pip install torch numpy
```
- Chạy chương trình thông qua các code cell để cho ra kết quả

# 3. Phân tích kết quả
- Tensor:	Tạo được các tensor từ nhiều nguồn, thực hiện phép toán, indexing, reshape thành công.
- Autograd: Gradient tính chính xác (dz/dx = 18 với x=1).
- Mô hình nn.Module: Mô hình hoạt động đúng, trả về đầu ra có kích thước hợp lý (1, 4, 2).

- Nhận xét:
  - PyTorch tự động quản lý gradient và đồ thị tính toán, giúp việc huấn luyện mô hình trở nên dễ dàng.
  - Các lớp trong torch.nn hỗ trợ việc xây dựng mô hình theo hướng hướng đối tượng, rất tiện để mở rộng cho các bài toán phức tạp.

# 4. Khó khăn và giải pháp
## Không gọi được z.backward() lần thứ 2
```
z.backward() # Hoạt động bình thường
z.backward() # Graph đã bị xóa, nên không thể lan truyền gradient nữa -> PyTorch ném lỗi
```
- Nếu muốn tính lại đạo hàm nhiều lần, cần giữ lại graph bằng tham số retain_graph=True
```
z.backward(retain_graph=True)
z.backward()  # Gọi lần hai không lỗi
```

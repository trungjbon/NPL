# 1. Masked Language Modeling
- Mô hình đã dự đoán đúng từ "capital" với xác xuất 99%
- Các mô hình Encoder-only như này phù hợp với tác vụ này vì:
  - Được huấn luyện trực tiếp bằng Masked Language Modeling
  - Có self-attention hai chiều (bidirectional) -> tận dụng toàn bộ ngữ cảnh
 
# 2. Next Token Prediction
- Kết quả sinh ra hợp lý
- Các mô hình Decoder-only như này phù hợp với tác vụ này vì:
  - Được huấn luyện bằng causal language modeling
  - Self-attention chỉ nhìn trái, phù hợp cho từ tương lai chưa biết
  - Có cơ chế sinh nội dung auto-regressive

# 3. Sentence Representation
- Kích thước của vector biểu diễn là 768. Con số này tương ứng với tham số hidden_size của mô hình BERT
- Cần sử dụng attention_mask để loại bỏ token padding khi mean pooling để embedding không bị sai lệch

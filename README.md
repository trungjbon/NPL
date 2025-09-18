# NPL

Mô tả công việc

Trong Lab 1 và Lab 2, tôi đã thực hiện các bước sau:

Lab 1:

Cài đặt interface Tokenizer (sử dụng abc.ABC và abstractmethod).

Xây dựng SimpleTokenizer: tách token dựa trên khoảng trắng.

Xây dựng RegexTokenizer: sử dụng regex (\w+|[^\w\s]) để tách token, có thể bắt được dấu chấm câu và ký hiệu đặc biệt tốt hơn.

Lab 2:

Cài đặt interface Vectorizer với các phương thức fit, transform, fit_transform.

Xây dựng CountVectorizer:

Nhận một Tokenizer làm tham số.

Dùng tokenizer để tạo vocabulary (tập từ duy nhất trong corpus).

Biến mỗi document thành một document-term vector (mảng đếm số lần từ xuất hiện).

Test trên corpus nhỏ và dataset UD English EWT.

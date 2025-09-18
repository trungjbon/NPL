# Lab 1 & Lab 2 – Tokenizer và CountVectorizer

## 1. Mô tả công việc
### Lab 1
- Cài đặt interface `Tokenizer` với các phương thức trừu tượng.
- Xây dựng:
  - **SimpleTokenizer**: tách token dựa trên khoảng trắng.
  - **RegexTokenizer**: dùng regex (`\w+|[^\w\s]`) để tách từ, dấu câu, ký hiệu đặc biệt.
- Thử nghiệm trên dữ liệu mẫu và dataset **UD English EWT**.

### Lab 2
- Cài đặt interface `Vectorizer` với các phương thức:
  - `fit(corpus)`
  - `transform(documents)`
  - `fit_transform(corpus)`
- Xây dựng **CountVectorizer**:
  - Nhận `Tokenizer` làm input.
  - Sinh vocabulary từ corpus.
  - Biến đổi document thành vector đếm từ (document-term matrix).
- Test trên corpus nhỏ và dataset **UD English EWT**.

---

## 2. Kết quả chạy code

### Ví dụ corpus nhỏ
```python
corpus = [
    "I love NLP.",
    "I love programming.",
    "NLP is a subfield of AI."
]

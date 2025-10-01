## 1. Mô tả công việc
### Lab 1
1. **Định nghĩa interface `Tokenizer`**
   - Dùng `abc.ABC` và `abstractmethod` để định nghĩa phương thức `tokenize(text: str)`.

2. **Cài đặt `SimpleTokenizer`**
   - Implement class `SimpleTokenizer` kế thừa `Tokenizer`.
   - Token hóa dựa trên hàm `for` để xử lý.

3. **Cài đặt `RegexTokenizer`**
   - Implement class `RegexTokenizer` kế thừa `Tokenizer`.
   - Sử dụng regex `\w+|[^\w\s]` để tách cả từ, dấu câu, ký hiệu đặc biệt.

4. **Test tokenizer**
   - Chạy thử `SimpleTokenizer` và `RegexTokenizer` trên mẫu text ngắn và dataset UD English EWT.


### Lab 2
1. **Định nghĩa interface `Vectorizer`**
   - Định nghĩa class `Vectorizer(ABC)` với các phương thức:
     - `fit(corpus: list[str])`
     - `transform(documents: list[str]) -> list[list[int]]`
     - `fit_transform(corpus: list[str]) -> list[list[int]]`

2. **Cài đặt `CountVectorizer`**
   - Implement class `CountVectorizer` kế thừa `Vectorizer`.
   - Constructor nhận `Tokenizer`.
   - Trong `fit`:
     - Dùng tokenizer để duyệt toàn bộ corpus.
     - Thu thập tất cả token vào một tập hợp (set).
     - Tạo `vocabulary_` (dict từ → index).
   - Trong `transform`:
     - Với mỗi document:
       - Tạo vector toàn 0 có kích thước bằng vocab.
       - Tokenize document.
       - Với mỗi token có trong vocab, tăng giá trị tại vị trí index tương ứng.
   - Trả về document-term matrix (list các vector).
- Xây dựng **CountVectorizer**:
  - Nhận `Tokenizer` làm input.
  - Sinh vocabulary từ corpus.
  - Biến đổi document thành vector đếm từ (document-term matrix).

3. **Test CountVectorizer**
   - Chạy thử trên corpus nhỏ và dataset **UD English EWT**
   - In vocab và document-term matrix.
   
---

## 2. Kết quả chạy code
- Chạy kết quả với các file lab1_test.py và lab2_test.py
  
### Lab 1
```
Sample:  Hello, world! This is a test.
Simple Tokenizer: ['hello', ',', 'world', '!', 'this', 'is', 'a', 'test', '.']
Regex Tokenizer: ['hello', ',', 'world', '!', 'this', 'is', 'a', 'test', '.']

Sample:  NLP is fascinating... isn't it?
Simple Tokenizer: ['nlp', 'is', 'fascinating', '.', '.', '.', 'isn', "'", 't', 'it', '?']
Regex Tokenizer: ['nlp', 'is', 'fascinating', '.', '.', '.', 'isn', "'", 't', 'it', '?']

Sample:  Let's see how it handles 123 numbers and punctuation!
Simple Tokenizer: ['let', "'", 's', 'see', 'how', 'it', 'handles', '123', 'numbers', 'and', 'punctuation', '!']
Regex Tokenizer: ['let', "'", 's', 'see', 'how', 'it', 'handles', '123', 'numbers', 'and', 'punctuation', '!']

--- Tokenizing Sample Text from UD_English-EWT ---
Original Sample: Al-Zaman : American forces killed Shaikh Abdullah al-Ani, the preacher at the
mosque in the town of ...
SimpleTokenizer Output (first 20 tokens): ['al', '-', 'zaman', ':', 'american', 'forces', 'killed', 'shaikh', 'abdullah', 'al', '-', 'ani', ',', 'the', 'preacher', 'at', 'the', 'mosque', 'in', 'the']
RegexTokenizer Output (first 20 tokens): ['al', '-', 'zaman', ':', 'american', 'forces', 'killed', 'shaikh', 'abdullah', 'al', '-', 'ani', ',', 'the', 'preacher', 'at', 'the', 'mosque', 'in', 'the']
```

### Lab 2
```
--- Corpus ---
['I love NLP.', 'I love programming.', 'NLP is a subfield of AI.']

--- Vocabulary ---
{'.': 0, 'a': 1, 'ai': 2, 'i': 3, 'is': 4, 'love': 5, 'nlp': 6, 'of': 7, 'programming': 8, 'subfield': 9}

--- Document-Term Matrix ---
[1, 0, 0, 1, 0, 1, 1, 0, 0, 0]
[1, 0, 0, 1, 0, 1, 0, 0, 1, 0]
[1, 1, 1, 0, 1, 0, 1, 1, 0, 1]

--- Sample Documents ---
Doc 1: Al-Zaman : American forces killed Shaikh Abdullah al-Ani, the preacher at the
Doc 2: mosque in the town of Qaim, near the Syrian border. [This killing of a respected
Doc 3: cleric will be causing us trouble for years to come.] DPA: Iraqi authorities
Doc 4: announced that they had busted up 3 terrorist cells operating in Baghdad. Two of
Doc 5: them were being run by 2 officials of the Ministry of the Interior! The MoI in

--- Vocabulary ---
{'!': 0, ',': 1, '-': 2, '.': 3, '2': 4, '3': 5, ':': 6, '[': 7, ']': 8, 'a': 9, 'abdullah': 10, 'al': 11, 'american': 12, 'ani': 13, 'announced': 14, 'at': 15, 'authorities': 16, 'baghdad': 17, 'be': 18, 'being': 19, 'border': 20, 'busted': 21, 'by': 22, 'causing': 23, 'cells': 24, 'cleric': 25, 'come': 26, 'dpa': 27, 'for': 28, 'forces': 29, 'had': 30, 'in': 31, 'interior': 32, 'iraqi': 33, 'killed': 34, 'killing': 35, 'ministry': 36, 'moi': 37, 'mosque': 38, 'near': 39, 'of': 40, 'officials': 41, 'operating': 42, 'preacher': 43, 'qaim': 44, 'respected': 45, 'run': 46, 'shaikh': 47, 'syrian': 48, 'terrorist': 49, 'that': 50, 'the': 51, 'them': 52, 'they': 53, 'this': 54, 'to': 55, 'town': 56, 'trouble': 57, 'two': 58, 'up': 59, 'us': 60, 'were': 61, 'will': 62, 'years': 63, 'zaman': 64}

--- Document-Term Matrix ---
[0, 1, 2, 0, 0, 0, 1, 0, 0, 0, 1, 2, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
[0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 2, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 2, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0]
[0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0]
[1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 2, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
```

---

## 3. Giải thích kết quả
### SimpleTokenizer và RegexTokenizer
- Kết quả test cho ra giống nhau trên 1 số ví dụ cơ bản và trên dataset UD English EWT
- Nhưng triển khai SimpleTokenizer phức tạp hơn và sẽ khó khăn trong việc mở rộng các tiêu chí tách từ khác so với dùng biểu thức chính quy của RegexTokenizer

### CountVectorizer
- Vocabulary: tập hợp tất cả token duy nhất trong corpus, mỗi token gán một index.
- Document-Term Matrix: mỗi document là một vector, số chiều bằng số token trong vocab.
- Với corpus nhỏ: kết quả dễ đọc, minh họa rõ ràng.
- Với dataset UD EWT: vocab rất lớn, ma trận thưa (sparse), cho thấy hạn chế của CountVectorizer trong thực tế.
  
### Khó khăn & Cách xử lý
- Lỗi ModuleNotFoundError: Giải quyết bằng cách thêm
```
 import sys
 import os
 sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
```

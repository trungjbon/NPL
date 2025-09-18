Tokenizer và CountVectorizer

## 1. Mô tả công việc
### Lab 1
- Cài đặt interface `Tokenizer` với các phương thức trừu tượng.
- Xây dựng:
  - **SimpleTokenizer**: tách token dựa trên khoảng trắng và các ký hiệu đặc biệt dùng vòng lặp for để xử lý.
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

## 3. Giải thích kết quả


import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.preprocessing.regex_tokenizer import RegexTokenizer
from src.representations.count_vectorizer import CountVectorizer

def main():
    # Test 1
    tokenizer = RegexTokenizer()
    vectorizer = CountVectorizer(tokenizer)
    corpus = [
        "I love NLP.",
        "I love programming.",
        "NLP is a subfield of AI."
    ]

    X = vectorizer.fit_transform(corpus)

    print("\n--- Corpus ---")
    print(corpus)

    print("\n--- Vocabulary ---")
    print(vectorizer.vocabulary_)
    print("\n--- Document-Term Matrix ---")
    for row in X:
        print(row)

    # Test 2
    dataset_path = "Lab\\data\\UD_English-EWT\\en_ewt-ud-train.txt"
    raw_text = load_raw_text_data(dataset_path)

    sample_docs = raw_text.split("\n")[:5]
    sample_docs = [doc for doc in sample_docs if doc.strip()]

    print("\n--- Sample Documents ---")
    for i, doc in enumerate(sample_docs):
        print(f"Doc {i+1}: {doc}")

    X = vectorizer.fit_transform(sample_docs)

    print("\n--- Vocabulary ---")
    print(vectorizer.vocabulary_)

    print("\n--- Document-Term Matrix ---")
    for row in X:
        print(row)


if __name__ == "__main__":
    main()



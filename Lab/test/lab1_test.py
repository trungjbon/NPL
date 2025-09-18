import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.core.dataset_loaders import load_raw_text_data
from src.preprocessing.regex_tokenizer import RegexTokenizer
from src.preprocessing.simple_tokenizer import SimpleTokenizer

def main():
    # Test 1
    sample1 = "Hello, world! This is a test."
    sample2 = "NLP is fascinating... isn't it?"
    sample3 = "Let's see how it handles 123 numbers and punctuation!"

    simple_tokenizer = SimpleTokenizer()
    regex_tokenizer = RegexTokenizer()

    print(simple_tokenizer.tokenize(sample1))
    print(regex_tokenizer.tokenize(sample1))

    print(simple_tokenizer.tokenize(sample2))
    print(regex_tokenizer.tokenize(sample2))

    print(simple_tokenizer.tokenize(sample3))
    print(regex_tokenizer.tokenize(sample3))

    # Test 2
    dataset_path = "Lab\\data\\UD_English-EWT\\en_ewt-ud-train.txt"
    raw_text = load_raw_text_data(dataset_path)

    sample_text = raw_text[:500]  
    print("\n--- Tokenizing Sample Text from UD_English-EWT ---")
    print(f"Original Sample: {sample_text[:100]}...")

    simple_tokens = simple_tokenizer.tokenize(sample_text)
    print(f"SimpleTokenizer Output (first 20 tokens): {simple_tokens[:20]}")

    regex_tokens = regex_tokenizer.tokenize(sample_text)
    print(f"RegexTokenizer Output (first 20 tokens): {regex_tokens[:20]}")


if __name__ == "__main__":
    main()
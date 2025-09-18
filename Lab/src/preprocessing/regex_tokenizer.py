import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import re
from core.interfaces import Tokenizer

class RegexTokenizer(Tokenizer):
    def tokenize(self, text: str) -> list[str]:
        text = text.lower()

        tokens = re.findall(r"\w+|[^\w\s]", text)

        return tokens
    
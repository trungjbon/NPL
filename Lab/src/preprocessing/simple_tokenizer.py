import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import string
from core.interfaces import Tokenizer

class SimpleTokenizer(Tokenizer):
    def tokenize(self, text: str) -> list[str]:
        text = text.lower()
        punctuation = string.punctuation

        tokens = []
        curr = ""

        for ch in text:
            if (ch.isspace()):
                if (curr):
                    tokens.append(curr)
                    curr = ""
            elif (ch in punctuation):
                if (curr):
                    tokens.append(curr)
                    curr = ""
                tokens.append(ch)
            else:
                curr += ch

        if (curr):
            tokens.append(curr)

        return tokens

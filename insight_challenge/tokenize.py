import collections
import string

import nltk

_tokenizer = nltk.tokenize.WordPunctTokenizer()


def word_tokenize(text, tokenizer=_tokenizer):
    tokens = tokenizer.tokenize(text)
    words = filter(lambda x: x not in string.punctuation, tokens)
    return map(str.lower, words)

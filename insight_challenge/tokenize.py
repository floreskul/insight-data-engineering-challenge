import collections
import string

import nltk

_tokenizer = nltk.tokenize.WordPunctTokenizer()


def word_tokenize(text, tokenizer=_tokenizer):
    # First remove all hyphens and apostrophes from the text
    # We can do it safely as they aren't used to separate different words
    text = text.replace('-', '')
    text = text.replace('\'', '')

    tokens = tokenizer.tokenize(text)
    words = filter(lambda x: x not in string.punctuation, tokens)
    return map(str.lower, words)

import collections

import nltk

_tokenizer = nltk.tokenize.WordPunctTokenizer()


def word_tokenize(text, tokenizer=_tokenizer):
    '''Split the given text into tokens'''

    # First remove all hyphens and apostrophes from the text
    # We can do it safely as they aren't used to separate different words
    text = text.replace('-', '')
    text = text.replace('\'', '')

    tokens = tokenizer.tokenize(text)
    # Remove tokens that are just punctuation symbols
    words = filter(str.isalnum, tokens)
    return map(str.lower, words)

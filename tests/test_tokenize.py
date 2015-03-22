import unittest

from insight_challenge.tokenize import word_tokenize


class TestTokenize(unittest.TestCase):

    def test_empty(self):
        result = word_tokenize('')
        self.assertEqual(list(result), [])

    def test_single_word(self):
        result = word_tokenize('test')
        self.assertEqual(list(result), ['test'])

    def test_only_punctuation(self):
        result = word_tokenize('.')
        self.assertEqual(list(result), [])

        result = word_tokenize('. ,\t&')
        self.assertEqual(list(result), [])

    def test_task_example(self):
        result = word_tokenize('So call a big meeting,')
        self.assertEqual(list(result), ['so', 'call', 'a', 'big', 'meeting'])

    def test_hyphens(self):
        result = word_tokenize('hi-lite')
        self.assertEqual(list(result), ['hilite'])

    def test_conjunctions(self):
        result = word_tokenize("we're and haven't")
        self.assertEqual(list(result), ['were', 'and', 'havent'])

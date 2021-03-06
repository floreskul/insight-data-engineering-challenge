'''
Calculate and print the counts of words.

The script reads the given files, extracts words from the text
and prints total word counts for words ordered alphabetically.
'''
import sys
import fileinput
import collections

import tokenize


def main():
    # Read the list of files from the command line arguments
    # Make sure they are ordered in alphabetical order
    files = sorted(sys.argv[1:])
    file_input = fileinput.FileInput(files)

    # Count frequencies using a Counter object based on Python's dict
    # For more memory efficient implementation we may use Trie data structure
    word_counter = collections.Counter()
    for line in file_input:
        for word in tokenize.word_tokenize(line):
            word_counter[word] += 1

    for word in sorted(word_counter.keys()):
        print ('%s\t%s' % (word, word_counter[word]))


if __name__ == '__main__':
    main()

import sys
import os
import fileinput
import collections

import tokenize


INPUT_DIRECTORY = '../wc_input'


def get_file_stream(dir_path):
    '''
    Return a line stream from files in the given directory in alphabetic order

    Any subdirectories are ignored
    '''

    files_and_directories = [os.path.join(dir_path, f)
                             for f in os.listdir(dir_path)]
    files = sorted(filter(os.path.isfile, files_and_directories))

    file_input = fileinput.FileInput(files)
    return file_input


def main():
    word_counter = collections.Counter()
    # Count frequencies
    for line in get_file_stream(INPUT_DIRECTORY):
        for word in tokenize.word_tokenize(line):
            word_counter[word] += 1
    # Print the result
    for word in sorted(word_counter.keys()):
        print ('%s\t%s' % (word, word_counter[word]))


if __name__ == '__main__':
    main()

import sys
import fileinput

import tokenize
import median


def main():
    # Read the list of files from the command line arguments
    # and make sure they are ordered in alphabetical order
    files = sorted(sys.argv[1:])
    file_input = fileinput.FileInput(files)

    running_median = median.RunningMedian()
    for line in file_input:
        words = list(tokenize.word_tokenize(line))
        running_median.add(len(words))
        print ('%.1f' % running_median.get_median())


if __name__ == '__main__':
    main()

# insight-data-engineering-challenge
The solution to the [coding challenge](https://github.com/InsightDataScience/cc-example) for the [Insight Data Engineering Program](http://insightdataengineering.com/) implemented in Python 3.

## Task

One of the first problems you’ll encounter in data engineering is Word Count, which takes in a text file or set of text files from a directory and outputs the number of occurrences for each word.  For example, Word Count on a file containing the following passage:

> So call a big meeting,  
Get everyone out out,  
Make every Who holler,  
Make every Who shout shout.  

would return:

	a			1
	big			1  
	call		1  
	every		2  
	everyone	1  
	get			1  
	holler		1  
	make		2  
	meeting		1  
	out			2  
	shout		2  
	so			1  
	who			2  

The first part of the coding challenge is to implement your own version of Word Count that counts all the words from the text files contained in a directory named `wc_input` and outputs the counts (in alphabetical order) to a file named `wc_result.txt`, which is placed in a directory named `wc_output`.

Another common problem is the Running Median - which keeps track of the median for a stream of numbers, updating the median for each new number.  The second part of the coding challenge is to implement a running median for the number of words per line of text.  Consider each line in a text file as a new stream of words, and find the median number of words per line, up to that point (i.e. the median for that line and all the previous lines).  For example, the first line of the passage

> So call a big meeting,  
Get everyone out out,  
Make every Who holler,  
Make every Who shout shout.  

has 5 words so the running median for the first line is simply 5.  Since the second line has 4 words, the running median for the first two lines is the median of {4, 5} = 4.5 (since the median of an even set of numbers is defined as the mean of the middle two elements after sorting).  After three lines, the running median would be the median of {4, 4, 5} = 4, and after all four lines the running median is the median of {4, 4, 5, 5} = 4.5.  Thus, the correct output for the running median program for the above passage is:

	5.0  
	4.5  
	4.0  
	4.5  

We'd like you to implement your own version of this running median that calculates the median number of words per line, for each line of the text files in the `wc_input` directory.  If there are multiple files in that directory, the files should be combined into a single stream and processed by your running median program in alphabetical order, so a file named `hello.txt` should be processed before a file named `world.txt`.  The resulting running median for each line should then be outputted to a text file named `med_result.txt` in the `wc_output` directory.

You may write your solution in any one of the following programming languages: C, C++, Clojure, Java, Python, Ruby, or Scala - then submit a link to a Github repo with your source code.  In addition to the source code, the top-most directory of your repo must include `wc_input` and `wc_output` directories, and a shell script named `run.sh` that compiles and runs the Word Count and Running Median programs.  If your solution requires additional libraries or dependencies, the shell script should load them first so that your programs can be run on any system just by running `run.sh`.  See the figure below for the required structure of the top-most directory in your repo, or simply clone this repo.

As a data engineer, it’s important that you write clean, well-documented code that scales for large amounts of data.  For this reason, it’s important to ensure that your solution works well for small and large text files, rather than just the simple examples above.

**More details are available in the official repository:** https://github.com/InsightDataScience/cc-example


## Word Count

The solution is based on using text tokenization from the [NLTK](http://www.nltk.org/) library with few custom changes to satisfy the requirements from the FAQ section in the official repository. We keep counts of all extracted words by using _collections.Counter_ class from the Python standart library which is a subclass of the built-in _dict_ type. At the end we simply iterate the sorted found words (keys) and print the count for each of them.

## Running Median

The solution is based on using two heaps - a min-heap to store the elements greater or equal than the median and a max-heap to store elements smaller or equal to the median. We maintain the property that the size of any heap is not larger than the other one by more than 1. This gives the opportunity to perform the add operation in _O(log n)_ time and to get median in _O(1)_ time.n


## Run programs

Both _Word Count_ and _Running Median_ programs are launched by running _run.sh_ Bash script:

	./run.sh

The results will be available in the files _wc_output/wc_result.txt_ and _wc_output/med_result.txt_.

To manually run the programs and print the output to STDOUT:

	python3 insight_challenge/word_count.py <file_1> <file_n>
	python3 insight_challenge/running_median.py <file_1> <file_n>


## Tests

Tests are available in the _tests_ directory. To run them:

	cd tests
	python3 -m unittest


## Dependencies

- Python3
- NLTK 3.0

The _run.sh_ script automatically installs all dependencies during the first run on OS X or Debian-based Linux operating systems.


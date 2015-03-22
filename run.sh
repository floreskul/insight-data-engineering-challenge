#!/usr/bin/env bash

# Install dependencies
if [ "$(uname)" == "Darwin" ]; then
    if [! python3 -V > /dev/null 2>&1 ]; then
        # Install Homebrew
        ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
        # Install Python3, versions >= 3.4 include pip3 by default
        brew install python3
    fi
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    if [! python3 -V > /dev/null 2>&1 ]; then
        apt-get install -y python3
    fi
    if [! pip3 -V > /dev/null 2>&1 ]; then
        apt-get install -y python3-pip
    fi
fi
if [! python -c "import nltk" > /dev/null 2>&1 ]; then
    pip3 install nltk
fi

# Run Word Count
python3 insight_challenge/word_count.py wc_input/* > wc_output/wc_result.txt
# Run Running Median
python3 insight_challenge/running_median.py wc_input/* > wc_output/med_result.txt

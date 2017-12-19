#!/usr/bin/env python3
'''
Created on Oct 7, 2017

@author: j_sal

Retrieve and print words from a URL.

Usage:
    
    python3 WordModule.py <URL>
    python WordModule.py <URL>
'''
import sys
from urllib.request import urlopen
# 'http://sixty-north.com/c/t.txt'


def fetch_words(url):
    """Fetch a list of words from a URL.
    
    Args:
        url: The URL of a UTF-8 text document.
        
    Returns:
        A list of strings containing the words from
        the document.
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    """Print items one per line.
    
    Args:
        An iterable series of printable items.
    """
    for item in items:
        print(item)

    
def main(url):
    """Print each word from a text document from a URL.
    
    Args:
        url: The URL of a UTF-8 text document.
    """
    words = fetch_words(url)
    print (words)

    
if __name__ == '__main__':
    main(sys.argv[1])
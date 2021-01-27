"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    
    def __init__(self, path):
        """create dictionary with words from file, count them and return word count
        """
        word_list = open(path)
        self.words = self.parse(word_list)
        print(f"{len(self.words)} words were read")

    def parse(self, word_list):
        """remove all spaces from words"""
        return [w.strip() for w in word_list]
    
    def random(self):
        """Return random word."""
        return random.choice(self.words)

    
wf = WordFinder("words.txt")
"""initialize path to variable"""


class SpecialWordFinder(WordFinder):
    """WordFinder that excludes blank lines/comments."""
    
    def parse(self, word_list):
        """remove all spaces from words; return words without #
        """

        return [w.strip() for w in word_list if w.strip() and not w.startswith("#")]

swf = SpecialWordFinder("words.txt")

"""
In [2]: %run wordfinder.py
235886 words were read

In [3]: wf.random()
Out[3]: 'Phytozoa'

In [4]: wf.random()
Out[4]: 'quadriseptate'
"""
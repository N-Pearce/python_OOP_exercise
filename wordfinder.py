"""Word Finder: finds random words from a dictionary."""
from random import choice

class WordFinder:
    ...
    def __init__(self, file):
        self.file = file
        self.words = []
        self.read_file()
        print(f"{len(self.words)} words read")

    def read_file(self):
        with open(self.file) as f:
            for line in f:
                self.words.append(line)

    def random(self):
        word = choice(self.words)
        return word.removesuffix("\n")

class SpecialWordFinder(WordFinder):
    """Only returns words that aren't commented out

    >>> swf = SpecialWordFinder("complex.txt")
    3 words read
    
    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True
    """

    def read_file(self):
        with open(self.file) as f:
            for line in f:
                if line.strip() and not line.startswith('#'):
                    self.words.append(line)
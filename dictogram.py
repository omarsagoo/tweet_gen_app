#!python

from __future__ import division, print_function  # Python 2 and 3 compatibility
from random import random


class Dictogram(dict):
    """Dictogram is a histogram implemented as a subclass of the dict type."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new dict and count given words."""
        super(Dictogram, self).__init__()  # Initialize this as a new dict
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        # Count words in given list, if any
        if word_list is not None:
            for word in word_list:
                self.add_count(word)

    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        self[word] = self.get(word , 0) + count
        self.tokens += count
        self.types = len(self)

    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        # TODO: Retrieve word frequency count
        
        return self.get(word, 0)

    def sampling(self):
        ran_num = random()
        weight_dict = self.weight_of_all_words_dict()
        prev_weight = 0
    
        for key in weight_dict:
            if prev_weight < ran_num < weight_dict[key]:
                return key
            prev_weight = weight_dict[key]

    def word_weight(self, word):
        if word in self:
            word_wgt = self.frequency(word) / self.tokens
            return word_wgt
        else:
            return 'no word found'
    
    def weight_of_all_words_dict(self):
        weight_dict = {}
        total_weight = 0
        for key in self.keys():
            wgt = self.word_weight(key)
            total_weight += wgt
            weight_dict[key] = weight_dict.get(key, total_weight)

        return weight_dict


def test_sampling_dict(histogram):
    sample_dict = {}
    for _ in range(10000):
        word = histogram.sampling()
        sample_dict[word] = sample_dict.get(word, 0) + 1

    return sample_dict

def print_histogram(word_list):
    print('word list: {}'.format(word_list))
    # Create a dictogram and display its contents
    histogram = Dictogram(word_list)
    print('dictogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()
    print(f'word has a weight of {histogram.word_weight(word_list[0])} ')
    print(histogram.weight_of_all_words_dict())
    print(histogram.sampling())
    print(test_sampling_dict(histogram))


def main():
    import sys
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) >= 1:
        # Test histogram on given arguments
        print_histogram(arguments)
    else:
        # Test histogram on letters in a word
        word = 'abracadabra'
        print_histogram(list(word))
        # Test histogram on words in a classic book title
        fish_text = 'one fish two fish red fish blue fish'
        print_histogram(fish_text.split())
        # Test histogram on words in a long repetitive sentence
        woodchuck_text = ('how much wood would a wood chuck chuck'
                          ' if a wood chuck could chuck wood')
        print_histogram(woodchuck_text.split())


if __name__ == '__main__':
    main()

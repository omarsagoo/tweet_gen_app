#!python

from __future__ import division, print_function  # Python 2 and 3 compatibility


class Listogram(list):
    """Listogram is a histogram implemented as a subclass of the list type."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new list and count given words."""
        
        super().__init__()  # Initialize this as a new list
        if word_list is not None:
            self.setup(word_list)
        # Add properties to track useful word counts for this histogram
        self.types = len(self)  # Count of distinct word types in this histogram
        self.tokens = sum([cell[1] for cell in self])  # Total count of all word tokens in this histogram

        # Count words in given list, if any
        


    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        value = 0
        for cell in self:
            if cell[0] == word:
                cell[1] += count
                self.tokens += count
                break
            value += 1

        
        if value == len(self):
            self.append([word, count])
            self.types += 1
            self.tokens += count
            


    def setup(self, word_list):
        for word in word_list:
            if word not in self:
                cell = [word, word_list.count(word)]
                if cell not in self:
                    self.append(cell)


    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        for cell in self:
            if cell[0] == word:
                return cell[1]
        return 0

    def __contains__(self, word):
        """Return boolean indicating if given word is in this histogram."""
        # TODO: Check if word is in this histogram
        for cell in self:
            if cell[0] == word:
                return True
        return False

    def _index(self, target):
        """Return the index of entry containing given target word if found in
        this histogram, or None if target word is not found."""
        # TODO: Implement linear search to find index of entry with target word
        for cell in self:
            if cell[0] == target:
                return self.index(cell)


def print_histogram(word_list):
    print('word list: {}'.format(word_list))
    # Create a listogram and display its contents
    histogram = Listogram(word_list)
    print('listogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()
    histogram.add_count('tree', 2)


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

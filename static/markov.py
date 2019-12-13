import re
from .dictogram import Dictogram

START = '[START]'
STOP = '[STOP]'

class Markov:

    def __init__(self, words_list, order):
        super().__init__()
        self.states = {}
        self.order = order
        self.words_list = words_list
        self.states[START] = Dictogram()
        
    def histo_of_histos(self):
        '''Returns a nested Histogram of words that follow other words.'''
        word = self.words_list[0]
        self.states[word] = Dictogram()
        self.states[START].add_count(word)

        for next_index in range(1, len(self.words_list)):
            # if the word is not already a Dictogram object, make it one
            if word not in self.states:
                self.states[word] = Dictogram()
                
            #add the count of the word to the individual Dictogram Object
            next_word = self.words_list[next_index]
            self.states[word].add_count(next_word)

            # if there is a period in the word, add a stop token and update start token
            if '.' in word:
                self.states[word].add_count(STOP)
                self.states[START].add_count(next_word)

            # reinitialize word to equal the next word.
            word = next_word


    def markov_sentence(self):
        '''Samples words to create a sentence'''
        word = self.states[START].sampling()
        sentence = []
        while word is not STOP:
            sentence.append(word)
            word = self.states[word].sampling()
        return ' '.join(sentence)

def get_file_clean(file):
    '''accepts the text file and opens the file, then reads through it and changes all the charecters to lowercase,
    then returns a list of all the words'''
    with open(file, 'r') as file:
        open_file = file.read().lower()
        words = re.sub(r'[^a-zA-Z.,\s]', '', open_file)
    return words.split()

def test_sampling_dict(histogram):
    '''Tests the sampling frequency for randomness at 10000 checks'''
    sample_dict = {}
    for _ in range(10000):
        word = histogram.sampling()
        sample_dict[word] = sample_dict.get(word, 0) + 1

    return sample_dict

if __name__ == "__main__":
    # fish_text = 'one fish two fish red fish blue fish'
    # mv = Markov(fish_text.split())
    # # print(mv.markov_sentence(8))
    # print(test_sampling_dict(mv.states['fish']))

    # # for item in mv:
    #     print(item)
    # print(mv.histo_of_histos())
    # print(mv.sampling())
    # dic = Dictogram(fish_text.split())
    # print(dic)

    file = 'diogenes.txt'
    file_list = get_file_clean(file)
    # print(file_list)
    dmv = Markov(file_list, 1)
    dmv.histo_of_histos()
    print(dmv.markov_sentence())
    # print(dmv.histo_of_histos())
    # dmv.log_histogram("diogenes_histo")
    # print(dmv.tokens)
    # print(dmv.types)
    # # print(Dictogram())
    # log_file = open('markov_dio_list.txt', 'w')
    # log_file.write(str(file_list))
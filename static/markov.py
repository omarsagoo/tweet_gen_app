from dictogram import Dictogram
import re
import json


class MarkovDict(Dictogram):

    def __missing__(self, key):
        # if the key is missing from the histogram, immediatly create a key value pair for it.
        self[key] = Dictogram()
        return self[key]

    def histo_of_histos(self):
        '''Returns a nested Histogram of words that follow other words.'''
        nested_histo = Dictogram()
        start_histo = Dictogram()
        stop_histo = Dictogram()
        start_histo.add_count(self.words_list[0])
        i = 0 # Creates a variable that is initializaed at 0
        for word in self.words_list:
            i += 1 # immedietly increment the variable by one
            # the immediate incrementation represents the word that will follow in the word list. 
            if i < len(self.words_list): # checks to make sure i doesnt go out of the list index
                next_word = self.words_list[i]
                # if the word is not already a Dictogram object, make it one
                if word not in nested_histo.keys():
                    nested_histo[word] = Dictogram()
                if '.' in word:
                    stop_histo.add_count(word)
                    start_histo.add_count(next_word)
                #add the count of the word to the individual Dictogram Object
                nested_histo[word].add_count(next_word) 
        # print(stop_histo)
        return nested_histo, start_histo, stop_histo

    


    def markov_sentence(self, length):
        '''Samples words from the histogram, and the nested histogram to create a sentence'''
        nested_histo, start_histo, stop_histo = self.histo_of_histos()        
        word = start_histo.sampling()
        sentence = [word]
        print(nested_histo['plato'].tokens)
        while word not in stop_histo.keys():
            word = nested_histo[word].sampling()
            sentence.append(word)
        return ' '.join(sentence)

def get_file_clean(file):
    '''accepts the text file and opens the file, then reads through it and changes all the charecters to lowercase,
    then returns a list of all the words'''
    with open(file, 'r') as file:
        open_file = file.read().lower()
        words = re.sub(r'[^a-zA-Z.\s]', '', open_file)
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
    # mv = MarkovDict(fish_text.split())
    # print(mv.markov_sentence(8))

    # # for item in mv:
    #     print(item)
    # print(mv.histo_of_histos())
    # print(mv.sampling())
    # dic = Dictogram(fish_text.split())
    # print(dic)

    file = 'diogenes.txt'
    file_list = get_file_clean(file)
    # print(file_list)
    dmv = MarkovDict(file_list)
    print(dmv.markov_sentence(15))
    # print(dmv.histo_of_histos())
    # dmv.log_histogram("diogenes_histo")
    # print(dmv.tokens)
    # print(dmv.types)
    # # print(Dictogram())
    # log_file = open('markov_dio_list.txt', 'w')
    # log_file.write(str(file_list))
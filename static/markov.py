from dictogram import Dictogram
import re
import json


class MarkovDict(Dictogram):

    def __missing__(self, key):
        self[key] = Dictogram()
        return self[key]

    def histo_of_histos(self):
        main_histo = Dictogram()
        nested_histo = Dictogram()
        
        i = 0
        for word in self.words_list:
            i += 1
            
            if i < len(self.words_list):
                nested_histo.add_count(self.words_list[i]) 

                if word not in main_histo.keys():
                    main_histo[word] = nested_histo

                elif self.words_list[i] not in main_histo[word].keys():
                    main_histo[word][self.words_list[i]] = nested_histo[self.words_list[i]]

                elif self.words_list[i] in main_histo[word].keys():
                    main_histo[word].add_count(self.words_list[i]) 

                nested_histo = Dictogram()
        return main_histo

    def markov_sentence(self, length):
        
        word = self.sampling()
        sentence = [word]
        main_histo = self.histo_of_histos()
        for _ in range(length - 1):
            word = main_histo[word].sampling()
            sentence.append(word)

        return ' '.join(sentence)

def get_file_clean(file):
    '''accepts the text file and opens the file, then reads through it and changes all the charecters to lowercase,
    then returns a list of all the words'''
    with open(file, 'r') as file:
        open_file = file.read().lower()
        words = re.sub(r'[^a-zA-Z\s]', '', open_file)
    return words.split()


if __name__ == "__main__":
    # fish_text = 'one fish two fish red fish blue fish'
    # mv = MarkovDict(fish_text.split())
    # for item in mv:
    #     print(item)
    # print(mv.histo_of_histos())
    # print(mv.markov_sentence(4))
    # dic = Dictogram(fish_text.split())
    # print(dic)

    file = 'diogenes.txt'
    file_list = get_file_clean(file)
    dmv = MarkovDict(file_list)
    print(dmv.markov_sentence(15))
    # print(dmv.tokens)
    # print(dmv.types)

from dictogram import Dictogram
import re


class MarkovDict(Dictogram):

    def histo_of_histos(self):
        main_histo = {}
        nested_histo = dict()
        
        i = 0
        for word in self.words_list:
            word_list = []

            i += 1
            # if word not in main_histo.keys():
            if i < len(self.words_list):
                # nested_histo.update({self.words_list[i]: 1})
                # print(nested_histo)
               
                main_histo.get({word: nested_histo.update({self.words_list[i]: 1})})
        return main_histo

    # def word_histogram(self, target_word):
    #     list_word = []
    #     i = 0    
    #     for word in self.words_list:
    #         i += 1 
    #         if word == target_word and i < len(self.words_list):
    #             list_word.append(self.words_list[i])
            
    #     return list_word

    def markov_sentence(self, length):
        sentence = []
    
        for _ in range(length):
            word = self.sampling()
            sentence.append(word)
            other_word = self.histo_of_histos()[word].sampling()
            sentence.append(other_word)
        return ' '.join(sentence)

def get_file_clean(file):
    '''accepts the text file and opens the file, then reads through it and changes all the charecters to lowercase,
    then returns a list of all the words'''
    with open(file, 'r') as file:
        open_file = file.read().lower()
        words = re.sub(r'[^a-zA-Z\s]', '', open_file)
    return words.split()


if __name__ == "__main__":
    fish_text = 'one fish two fish red fish blue fish'
    mv = MarkovDict(fish_text.split())
    print(mv.histo_of_histos())
    # dic = Dictogram(fish_text.split())
    # print(dic)

    # file = 'diogenes.txt'
    # file_list = get_file_clean(file)
    # dmv = MarkovDict(file_list)
    # print(dmv.markov_sentence(5))
    # print(dmv.tokens)
    # print(dmv.types)

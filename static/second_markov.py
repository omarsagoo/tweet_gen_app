from .dictogram import Dictogram
from .word_splitter import split_into_sentences
from .markov import Markov, get_file_clean, START, STOP

# nltk api


class MarkovSecondOrder(Markov):
    '''Class that holds the polymorphic code to create the 2nd order markov chain,
    subclass inherits from the markov class'''
    def create_second_markov(self):
        '''method creates the 2nd order markov chain dict.'''
        state = tuple(self.words_list[0:2])  # stop index depends on order
        self.states[START].add_count(state)

        for next_index in range(2, len(self.words_list)):
            if state not in self.states:
                self.states[state] = Dictogram()

            next_word = self.words_list[next_index]
            self.states[state].add_count(next_word)

            if '.' in state[1]:  # index depends on order
                #
                self.states[state].add_count(STOP)
                #
                next_next_word = self.words_list[next_index + 1]
                start_state = (next_word, next_next_word)
                self.states[START].add_count(start_state)

            state = (state[1], next_word)
        
        # creates a state for the last word pair, then adds STOP
        last_index = len(self.words_list) - 1
        last_state = (self.words_list[last_index - 1], self.words_list[last_index])
        if last_state not in self.states:
            self.states[last_state] = Dictogram([STOP])
        else:
            self.states[last_state].add_count(STOP)

    def create_sentence(self):
        '''Samples words to create a sentence'''
        state = self.states[START].sampling()
        sentence = []
        sentence.extend(state)
        word = state[1]  # index depends on order
        while word != STOP:
            word = self.states[state].sampling()
            if word == STOP:
                break
            sentence.append(word)
            state = (state[1], word)  # index depends on order
        return ' '.join(sentence)

class MarkovNthOrder(Markov):
    '''Class that holds the polymorphic code to create the nth order markov chain,
    subclass inherits from the markov class'''
    def create_nth_markov(self):
        '''method creates the nth order markov chain.'''
        _n = self.order
        state = tuple(self.words_list[0:_n])  # stop index depends on order
        self.states[START].add_count(state)

        for next_index in range(_n, len(self.words_list)):
            if state not in self.states:
                self.states[state] = Dictogram()

            next_word = self.words_list[next_index]
            self.states[state].add_count(next_word)

            # checks to see if there is a period in the last word of the state.
            # if there is, add a start and stop token
            if '.' in state[_n - 1]:  # index depends on order
                # adds the stop token in the state
                self.states[state].add_count(STOP)
                # creates a state tuple to add into the start token state histogram
                # the tuple will hold n words after the next word
                start_state = tuple(self.words_list[next_index:next_index + _n])
                # adds the start state to add into the histogram
                self.states[START].add_count(start_state)

            # create a new list to store all the previous states and the next word
            new_state_word_list = []
            # extend the previous state and the next word into the state
            new_state_word_list.extend(state[1:])
            new_state_word_list.append(next_word)
            # convert the list into a tuple and reinitialize the original state variable
            state = tuple(new_state_word_list)

        # creates a state for the last word pair, then adds STOP
        last_index = len(self.words_list)
        last_state = tuple(self.words_list[last_index-_n:last_index])
        if last_state not in self.states:
            self.states[last_state] = Dictogram([STOP])
        else:
            self.states[last_state].add_count(STOP)

    def create_sentence(self):
        '''Samples words to create a sentence'''
        _n = self.order - 1
        state = self.states[START].sampling()
        sentence = []
        sentence.extend(state)
        word = state[_n]  # index depends on order
        while word != STOP:
            word = self.states[state].sampling()
            if word == STOP:
                break
            sentence.append(word)

            new_state_word_list = []
            new_state_word_list.extend(state[1:])
            new_state_word_list.append(word)
            state = tuple(new_state_word_list)
        return ' '.join(sentence)


if __name__ == "__main__":
    WORDS = 'i like dogs and you like dogs. i like cats but you hate cats.'
    # mv = MarkovSecondOrder(words.split(), 2)
    # mv.create_second_markov()
    # print(mv.create_sentence())
    # pprint(mv.states)


    FILE = 'diogenes.txt'
    FILE_LIST = split_into_sentences(FILE)
    # dmv = MarkovSecondOrder(file_list)
    # dmv.create_second_markov()
    # print(dmv.create_sentence())

    NMV = MarkovNthOrder(FILE_LIST, 3)
    NMV.create_nth_markov()
    # print(nmv.words_list)
    # print(nmv.states)
    print(NMV.create_sentence())

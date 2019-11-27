import random
from sys import argv
from PyDictionary import PyDictionary
from rearrange import anagramizer

def get_file_lines(filename):
    file = open(filename, 'r')

    all_lines = file.readlines()

    all_lines = [line.strip() for line in all_lines]

    file.close()

    return all_lines
    
    
def random_dict_word(dictionary):
    rand_index = random.randint(0, len(dictionary)-1)

    return dictionary[rand_index]

def random_word_game(filename):
    dictionary = get_file_lines(filename)
    dictionary = random_dict_word(dictionary)
    print(dictionary)
    input(f"What does {dictionary} mean?")
    pydictionary = PyDictionary(random_dict_word(dictionary))
    print(dictionary)
    print(pydictionary.printMeanings())
    print(dictionary)


def autocomplete(filename):
    files = get_file_lines(filename)
    letter_input = input('what letter do you want all the words for? ')
    words = list()
    for line in files:
        if letter_input in line[0]:
            words.append(line)
    return words

def better_anagram(filename):
    files = get_file_lines(filename)
    word_input = input('what word do you want all the words for? ')
    words_anagram = anagramizer(word_input)
    words = []
    for line in files:
       if line in words_anagram:
           words.append(line)
    return words

if __name__ == "__main__":
    filename = '/usr/share/dict/words'

    files = get_file_lines(filename)

    number = argv[1:]
    
    words = [random_dict_word(files) for _ in range(int(number[0]))]
    print(words)

    # random_word_game(filename)

    autocomplete = autocomplete(filename)
    print(autocomplete)
    print(len(autocomplete))

    better_anagram = better_anagram(filename)
    print(better_anagram)

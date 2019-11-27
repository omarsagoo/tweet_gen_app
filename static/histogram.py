import re
from random import random, randint
import cProfile
# from rearrange import input_handler

'''Takes a file and turns it into a histogram dictionary, displaying word frequency'''
def create_histogram(file):
    ''' 
    takes file as an argument and creates a histogram dictionary, 
    then iterates over the entire text and stores the words/ checks for repitiotion
    saw this counting method online. 
    '''
    text =  file
   
    histogram = {}
    for word in text:
       histogram[word] = histogram.get(word, 0) + 1

    # returns the histogram
    return histogram


def get_file_clean():
    '''accepts the text file and opens the file, then reads through it and changes all the charecters to lowercase,
    then returns a list of all the words'''
    file = 'diogenes.txt'
    with open(file, 'r') as file:
        open_file = file.read().lower()
        words = re.sub(r'[^a-zA-Z\s]', '', open_file)
    return words.split()


def word_frequency( histo_word, histogram):
    for word in histogram:
        if word == histo_word:
            return histogram[word]

def list_histogram(file):
    text = set(file)
    return [[word, file.count(word)] for word in text]

def tuplegram(file):
    text = set(file)
    return list(zip(text, map(file.count, text)))

def countogram(file):
    histogram = tuplegram(file)
    counts = {}
    for word, count in histogram:
        if count in counts:
            counts[count].append(word)
        else:
            counts[count] = [word]
    return counts

def get_histogram_file(file):
    histo_list = {}
    with open(file, 'r') as file:
        for line in file:
           line_list = line.split()
           line_list[1] = int(line_list[1])
           histo_list[line_list[0]] = histo_list.get(line_list[0], line_list[1])

    file.close()
    return histo_list

def log_histogram(histogram):
    log_file = open("histofile.txt", 'w')
    for key in histogram:
        log_file.write(f'{key} {histogram[key]}\n')
    log_file.close()
    
def sortogram(histogram):
    return dict(sorted(histogram.items(),key = lambda x : x[1], reverse=True))

def unique_words(histogram):
    return len(histogram)

def total_words(histogram):
    token = 0
    for count in histogram.values():
        token += count
    
    return token

def word_weight(word, histogram):
    if word in histogram:
        word_wgt = word_frequency(word, histogram) / total_words(histogram)
        return word_wgt
    else:
        return 'no word found'

def weight_all_words_dict(histogram):
    weight_dict = {}
    total_weight = 0
    for key in histogram.keys():
        wgt = word_weight(key, histogram)
        total_weight += wgt
        weight_dict[key] = weight_dict.get(key, total_weight)

    return weight_dict
    
def weight_all_words_list(histogram):
    ttl_wgt = 0
    weight_list = [0]
    for key in histogram.keys():
        wgt = word_weight(key, histogram)
        ttl_wgt += wgt
        weight_list.append(ttl_wgt)
    return weight_list

def list_of_all_words(histogram):
    word_list = list(histogram)
    return word_list

def sample_by_frequency_list(histogram):
    ran_num = random()

    weight_list = weight_all_words_list(histogram)
    word_list = list_of_all_words(histogram)

    weight_list_index = len(weight_list) - 1
    I = 0
    for x in range(weight_list_index):
        x += 1
        if weight_list[i] <= ran_num <= weight_list[x]:
            return word_list[i]

        I-=-1

def sample_by_frequency_dict(histogram):
    # ran_num = random()
    # weight_dict = weight_all_words_dict(histogram)
    # prev_weight = 0
   
    # for key in weight_dict:
    #     if prev_weight < ran_num < weight_dict[key]:
    #         return key
    #     prev_weight = weight_dict[key]

    tokens = total_words(histogram)
    ran_num = randint(1, tokens)
    curr_range = 0
    for key in histogram:
        
        curr_range += histogram[key]
        if curr_range >= ran_num:
            return key


def word_weight_nested_histo(nested_histogram):
    histo_nested_weight = {}
    for key in nested_histogram:
        histo_nested_weight[key] = weight_all_words_dict(nested_histogram[key])

    return histo_nested_weight

def sample_sentence(nested_histogram, original_histogram):
    sentence = []
   
    for _ in range(5):
        word = sample_by_frequency_dict(original_histogram)
        sentence.append(word)
        other_word = sample_by_frequency_dict(nested_histogram[word])
        sentence.append(other_word)
    return ' '.join(sentence)


def histo_of_histos(word_list):
    main_histo = {}
    for word in word_list:
        if word not in main_histo.keys():
            main_histo[word] = main_histo.get(word, create_histogram(word_histogram(word, word_list)))
    return main_histo

def word_histogram(word, word_list):
    list_word = []    
    for i in range(len(word_list)):
        if word == word_list[i]:
            if len(word_list) - 1 != i:
                list_word.append(word_list[i+1])
            
    return list_word

def test_sampling_list(histogram):
    sample_dict = {}
    for _ in range(100000):
        word = sample_by_frequency_list(histogram)
        sample_dict[word] = sample_dict.get(word, 0) + 1

    return sample_dict

def test_sampling_dict(histogram):
    sample_dict = {}
    for _ in range(100000):
        word = sample_by_frequency_dict(histogram)
        sample_dict[word] = sample_dict.get(word, 0) + 1

    return sample_dict

if __name__ == "__main__":
    # words = get_file_clean()
    # # histofile = 'histogram.txt'
    # histo = create_histogram(words)
    # histo_dict = histo_of_histos(words)
    # sample_sentence(histo_dict, histo)

    # # print(histo)
    # # print(total_words(histo))
    # tokens = total_words(histo)
    # print(word_frequency('diogenes', histo))
    # sample_by_frequency(histo, tokens)
    # wood = 'Alice was beginning to get very tired of sitting by her sister on the bank and of having nothing to do'
    fish_text = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']
    # print(word_histogram('fish', fish_text))
    # print(create_histogram(word_histogram('fish', fish_text)))
    # print(histo_of_histos(wood.split()))
    fishtogram = create_histogram(fish_text)
    # print(fishtogram)

    # print(sample_sentence(histo_of_histos(wood.split()), create_histogram(wood.split()) ))
    # print(histogram(fish_text))
    # print(total_words(fishtogram))
    # print(word_frequency('fish', fishtogram))
    # print(word_weight('one', fishtogram))

    # print(weight_all_words_list(fishtogram))
    # print(list_of_all_words(fishtogram))
    # print(list_histogram(fish_text))
    # print(tuplegram(fish_text))
    # print(countogram(fish_text))
    # print(get_histogram_file(histofile))
    # sample_by_frequency_list(fishtogram)
    # print(test_sampling_dict(fishtogram))
    # print(weight_all_words_dict(fishtogram))
    # print(sample_by_frequency_dict(fishtogram))

    # fishtogram = histogram(fish_text)
    # sorted_histo = sortogram(histo)
    # log_histogram(sorted_histo)
    '''
    benchmarking sampling dict test with 100,000 sample size

    Benchmark test after refactoring code
    
    results:
        3,000,004 function calls, in 1.111 seconds
        999,901 function calls, in .393 seconds

    refactored way is superior by ~3x the speed
    '''
    print(cProfile.run('test_sampling_dict(fishtogram)'))

    '''
    benchmarking sampling list test with 100,000 sample size

    results:
        3,200,004 function calls in 1.369 seconds
    '''
    # print(cProfile.run('test_sampling_list(fishtogram)'))

    '''
    What do these results mean?
        well, this means that it is much faster to sample from a dictionary, than it is to sample from a list. 
        however, lists save memory, the tradeoff is that it takes much longer to iterate through a list, 
        than it does to search through a dictionary
    '''
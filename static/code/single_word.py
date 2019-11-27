import histogram

def single_rand_word(histogram):
    list_histogram = []
    for key in histogram.keys():
        cell = [key, histogram[key]]
        list_histogram.append(cell)
    return list_histogram

if __name__ == "__main__":
    fish_text = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']
    fishtogram = histogram.histogram(fish_text)
    print(fishtogram)
    single_rand_word(fishtogram)
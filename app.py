from flask import Flask
from static.markov import MarkovDict, get_file_clean

app = Flask(__name__)

file = 'static/diogenes.txt'
list_file = get_file_clean(file)
mv = MarkovDict(list_file)

@app.route('/')
def sample_dict():
    
    return mv.markov_sentence(5)

if __name__ == "__main__":
    print(mv.markov_sentence(10))
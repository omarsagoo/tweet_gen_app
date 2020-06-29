from flask import Flask, render_template
from static.markov import get_file_clean
from static.second_markov import MarkovNthOrder

app = Flask(__name__)


# mv = MarkovNthOrder(LIST_FILE, 3)
# mv.create_nth_markov()

FILE = 'static/diogenes.txt'
DIO_FILE =get_file_clean(FILE)
TRUMP_FILE = 'static/trump_txt.txt'
TRUMP_FILE = get_file_clean(TRUMP_FILE)
dmv = MarkovNthOrder(DIO_FILE, 4)
mv = MarkovNthOrder(TRUMP_FILE, 4)
mv.create_nth_markov()
dmv.create_nth_markov()
print(dmv.states)
@app.route('/')
def sample_dict():
    trump_sentence = mv.create_sentence()
    dio_sentence = dmv.create_sentence()
    return render_template('base.html', trump_sentence=trump_sentence, dio_sentence=dio_sentence)
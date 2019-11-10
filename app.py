from flask import Flask
import histogram

app = Flask(__name__)

fish_text = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']
fishtogram = histogram.create_histogram(fish_text)

@app.route('/')
def sample_dict():
    sample_dict = histogram.test_sampling_dict(fishtogram)
    return sample_dict
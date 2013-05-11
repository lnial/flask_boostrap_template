from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

app.debug = True

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        tweet = request.form['eval']
        return  render_template('index.html', tweet = tweet)
    tweet = "Hello world"
    return  render_template('index.html', tweet = tweet)
   

if __name__ == '__main__':
    app.run()

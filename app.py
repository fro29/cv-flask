from flask import Flask, render_template 
from data import Data 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', user_data = Data)

@app.route('/cv/<name>')
def cv(name):
    return name

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

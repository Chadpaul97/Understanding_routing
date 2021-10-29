from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/flask')
def say_Flask():
    return 'Hi Flask!'

@app.route('/say/michael')
def say_Michael():
    return 'Hi Michael!'

@app.route('/say/john')
def say_John():
    return 'Hi John!'



@app.route('/repeat/35/hello')
def hello():
    return ' Hello! '*35

@app.route('/repeat/80/bye')
def bye():
    return ' Bye! '*80

@app.route('/repeat/99/dogs')
def dogs():
    return ' Dogs '*99


if __name__=="__main__":
    app.run(debug=True)
import random
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/ping/<address>')
def ping(address):
    return f'/ping/{address}'

@app.route('/randomnumber')
def randomnumber():
    return str(random.randint(0,1000000000000000000000000000000000000000))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'MEOW!'


@app.route('/cats')
def hello_cats():
    return 'HERE BE CATS!'


if __name__ == '__main__':
    app.run()

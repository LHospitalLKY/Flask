from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/shiyanlou')
def hello_shiyanlou():
    return 'fuck shiyanlou'


if __name__ == '__main__':
    app.debug = False
    app.run(host = '127.0.0.1')
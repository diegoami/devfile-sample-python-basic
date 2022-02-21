from flask import Flask
from waitress import serve
import time

app = Flask(__name__)

@app.route('/')
def hello():
    time.sleep(80)
    return "Hello World!"

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)

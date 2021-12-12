from flask import Flask, request, abort
from urllib.parse import parse_qs, urlparse
from waitress import serve

app = Flask(__name__)


@app.route('/', methods=['POST','GET'])
def home():
    if request.method == 'GET':
        print("************************************")
        print("Response")        
        print("---------------------------------------")
        return 'Hello World!', 200
    else:
        abort(400)


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8081)

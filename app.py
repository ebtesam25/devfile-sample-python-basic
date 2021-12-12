from flask import Flask, request, abort
from urllib.parse import parse_qs, urlparse

app = Flask(__name__)


@app.route('/', methods=['POST','GET'])
def home():
    if request.method == 'GET':
        print("************************************")
        
        print("---------------------------------------")
        return '', 200
    else:
        abort(400)


@app.route('/webhook', methods=['POST','GET'])
def webhook():
    if request.method == 'GET':
        print("************************************")
        print("Response:",request.args['Body'])
        print("From:",request.args['From'])
        
        print("---------------------------------------")
        return '', 200
    else:
        abort(400)


@app.route('/mms', methods=['POST','GET'])
def mms():
    if request.method == 'POST':
        print("************************************")
        # print("Response:",request.args['Body'])
        # print("From:",request.args['From'])
        print("Response",request)
        
        print("---------------------------------------")
        return '', 200
    else:
        abort(400)


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8081)

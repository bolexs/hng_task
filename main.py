from flask import Flask, Response
from json import dumps
from flask_cors import CORS, cross_origin


app = Flask(__name__)

CORS(app)

cors = CORS(app, resources={
    r"/*": {
        "origins": "*"
    } 
})

@app.route('/', methods=['GET'])
@cross_origin( supports_credentials=True)
def index():
     return Response(dumps({
        "slack_username": "bolex",
        "backend": True,
        "age": 21,
        "bio": 'my name is bolu, i love taking challenges and trying to provide soluctions to problems'
    }), mimetype='text/json')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
from pprint import pprint
from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Custom'


pprint(app.config)

if __name__ == '__main__':
    app.run(debug=True)

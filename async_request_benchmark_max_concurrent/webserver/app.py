import sys
from flask import Flask

port = sys.argv[1]

app = Flask(
    'benchmarking',
)

@app.route('/')
def hello_world():
    return 'hello world'

app.run(port=port)

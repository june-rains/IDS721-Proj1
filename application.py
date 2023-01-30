from flask import Flask
from flask import request

application = Flask(__name__)

@application.route('/')
def hello_world():
    return 'Hello, World!'


@application.route('/name', methods=['GET', 'POST'])
def get_name():
    if request.method == 'GET':
        return 'name from GET'
    else:
        return 'name from POST'

@application.route('/fans')
def get_fans():
    return '100000'
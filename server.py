# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask
from flask_restful import Resource, Api, reqparse, abort
import stanfordNER

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('text')
    
def handleException():
    abort(404, message = "Unable to Identify the Entity")

class StanfordNer(Resource):
    def post (self):
        args = parser.parse_args()
        text = args['text']
        try :
            result = stanfordNER.performIdentification(text)
        except:
            handleException()
        return {'data' : result}

api.add_resource(StanfordNer , '/stanfordner')

if __name__ == '__main__':
    app.run(debug=True)
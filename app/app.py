from flask import Flask, request
from flask_restful import Api

from app.resources import ImageResource

app = Flask(__name__)
api = Api(app)

api.add_resource(ImageResource, '/')


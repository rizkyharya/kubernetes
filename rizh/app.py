from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'HELLO': 'RIZH'}

api.add_resource(HELLORIZH, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
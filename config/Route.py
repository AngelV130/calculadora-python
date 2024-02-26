from flask import Flask
from flask_cors import CORS


# Configurar rutas
class Router:

    def __init__(self):
        self._app = Flask(__name__)
        CORS(self._app)

    def run(self):
        self._app.run(debug=True)

    def get(self, url, function, name=''):
        return self._app.add_url_rule(url, name, function, methods=['GET'])

    def post(self, url, function, name=''):
        return self._app.add_url_rule(url, name, function, methods=['POST'])

    def put(self, url, function, name=''):
        return self._app.add_url_rule(url, name, function, methods=['PUT'])

    def delete(self, url, function, name=''):
        return self._app.add_url_rule(url, name, function, methods=['DELETE'])
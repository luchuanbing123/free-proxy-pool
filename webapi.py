from flask import Flask, request
import proxyhelper
import config


def execute():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'Hello, World!'

    @app.route('/get')
    def get(protocol='http', token=None):
        if request.values.get('protocol') in ['http', 'https']:
            protocol = request.values.get('protocol')
        if request.values.get('token'):
            token = request.values.get('token')
        proxy = proxyhelper.next(protocol, token)
        return proxy['proxy_addr']

    app.run(host=config.webapi_host, port=config.webapi_port)

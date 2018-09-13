from flask import Flask, request
import proxyhelper
import config
import threading
import time


def execute():
    threading.Thread(target=_update_proxy_daily).start()
    app = Flask(__name__)

    @app.route('/')
    def index():
        contents = [
            'github:<a href="https://github.com/LuChuanBing/free-proxy-pool">https://github.com/LuChuanBing/free-proxy-pool</a>',
            '作者/Author: bingge',
            '联系方式/contact: 微信公众号:<b>高效工具库(gaoxiaogongjuku)</b>',
            "<img alt='微信公众号:gaoxiaogongjuku'  src='https://github.com/LuChuanBing/free-proxy-pool/blob/master/qrcode.jpg' />",
            '当前共有<b>{}</b>个代理IP'.format(proxyhelper.get_proxy_count()),
            "<a href='https://github.com/LuChuanBing/free-proxy-pool/blob/master/README.md'>说明文档</a>",
            "<a href='https://github.com/LuChuanBing/free-proxy-pool/blob/master/README.en.md'>readme</a>"
        ]
        return '<div style="margin:10px"></div>'.join(contents)

    @app.route('/get')
    def get(protocol='http', token=None):
        if request.values.get('protocol') in ['http', 'https']:
            protocol = request.values.get('protocol')
        if request.values.get('token'):
            token = request.values.get('token')
        proxy = proxyhelper.next(protocol, token)
        return proxy['proxy_addr']

    app.run(host=config.webapi_host, port=config.webapi_port)


def _update_proxy_daily():
    while True:
        proxyhelper.update_proxy()
        time.sleep(24 * 60 * 60)

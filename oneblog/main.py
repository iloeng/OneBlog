# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     main
   Description :
   Author :        Liangz
   Date：          2018/12/7
-------------------------------------------------
   Change Activity:
                   2018/12/7:
-------------------------------------------------
"""
__author__ = 'Liangz'


from flask import Flask
import settings
import urllib
from werkzeug.routing import BaseConverter


app = Flask(__name__)

# 加载配置文件
# app.config.from_object('settings')
app.config.from_object(settings)


@app.route('/')
def index():
    return 'Hello world'


@app.route('/user')
def user():
    return 'Welcome!'


@app.route('/item/<id>')
def item(id):
    return 'Item:{}'.format(id)


# @app.route('/<any(a, b):page_name>/')


class ListCoverter(BaseConverter):

    def __init__(self, url_map, separator='+'):
        super(ListCoverter, self).__init__(url_map)
        self.separator = urllib.unquote(separator)

    def to_python(self, value):
        return value.split(self.separator)

    def to_url(self, values):
        return self.separator.join(BaseConverter.to_url(value) for value in values)

app.url_map.converters['list']=ListCoverter


@app.route('/list1/<list:page_name>')
def list1(page_names):
    return 'Separator:{}{}'.format('+', page_names)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

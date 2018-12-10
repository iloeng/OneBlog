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


from flask import Flask, url_for, request, abort, redirect
import config
# import urllib.request
# from werkzeug.routing import BaseConverter


app = Flask(__name__)

# 加载配置文件
# app.config.from_object('settings')
app.config.from_object(config)


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


# class ListCoverter(BaseConverter):
#
#     def __init__(self, url_map, separator='+'):
#         super(ListCoverter, self).__init__(url_map)
#         self.separator = urllib.request.unquote(separator)
#
#     def to_python(self, value):
#         return value.split(self.separator)
#
#     def to_url(self, values):
#         return self.separator.join(BaseConverter.to_url(value)
#                                    for value in values)
#
#
# app.url_map.converters['list'] = ListCoverter


# @app.route('/list1/<list:page_names>')
# def list1(page_names):
#     return 'Separator:{}{}'.format('+', page_names)
#
#
# @app.route('/list2/<list(separator=u"|"):page_names>')
# def list2(page_names):
#     return 'Separator:{}{}'.format('|', page_names)


@app.route('/projects/')
def projects():
    return "The Project Page"


@app.route('/about')
def about():
    return 'The About Page'

#
# @app.route('/item/1/')
# def item1(id):
#     pass
#
#
# with app.test_request_context():
#     print(url_for('item1', id='1'))
#     print(url_for('item1', id=2, next='/'))
#     # /item/1/?id=1
#     # /item/1/?id=2&next=%2F

@app.route('/people/')
def people():
    name = request.args.get('name')
    if not name:
        return redirect(url_for('login'))
    user_agent = request.headers.get('User-Agent')
    return 'Name:{0}; UA:{1}'.format(name, user_agent)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        return 'User:{} login'.format(user_id)
    else:
        return 'Open Login Page'


@app.route('/secret/')
def secret():
    abort(401)
    print('This is never executed')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

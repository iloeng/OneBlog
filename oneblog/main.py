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


from flask import Flask, url_for, request, abort, redirect, render_template, make_response
import config
from flask_bootstrap import Bootstrap
from flask import jsonify     # Json格式的响应
from werkzeug.wrappers import Response
# import urllib.request
# from werkzeug.routing import BaseConverter
from flask.views import View

app = Flask(__name__, template_folder='./templates')
bootstrap = Bootstrap(app)      # 引入Bootstrap，防止出现模板base.html错误
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


# @app.errorhandler(404)
# def not_found(error):
#     return render_template('404.html'), 404

# 此方式更加灵活，可以设置cookie、头信息等
@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('404.html'), 404)
    return resp


class JSONResponse(Response):
    @classmethod
    def force_type(cls, rv, environ=None):
        if isinstance(rv, dict):
            rv = jsonify(rv)
        return super(JSONResponse, cls).force_type(rv, environ)


app.response_class = JSONResponse


@app.route('/')
def hellow_world():
    return {'message': 'Hello World'}


@app.route('/custom_headers')
def header():
    return {'header': [1, 2, 3]}, 201, [('X-Request-ID', '100')]


class BaseView(View):
    def get_template_name(self):
        raise NotImplementedError

    def render_template(self, context):
        return render_template(self.get_template_name(), **context)

    def dispatch_request(self):
        if request.method != 'GET':
            return 'UNSUPPORTED!'
        context = {'users': self.get_users()}
        return self.render_template(context)


class UserView(BaseView):
    def get_template_name(self):
        return 'users.html'

    def get_users(self):
        return [{
            'username': 'fake',
            'avatar': 'http://lorempixel.com/100/100/nature'
        }]


app.add_url_rule('/users', view_func=UserView.as_view('userview'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

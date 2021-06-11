#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name:     app.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2021.06.11   23:27
-------------------------------------------------------------------------------
   @Change:   2021.06.11
-------------------------------------------------------------------------------
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name:     app.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.07.24   17:51
-------------------------------------------------------------------------------
   @Change:   2020.07.24
-------------------------------------------------------------------------------
"""

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from apps.main.views import main
from flask_admin import Admin, BaseView
from apps.admin.views import AdminHomeView, UserView
from apps.models import User, Post

db = SQLAlchemy()


def create_app():
    application = Flask(__name__)  # , template_folder='apps/templates')
    configure_app(application)
    manage = management(application)
    db.init_app(application)
    application.register_blueprint(main)
    return application


def configure_app(app, config=Config):
    app.config.from_object(config)


def management(app):
    manage = Admin(app, name=u'后台管理系统', template_mode='bootstrap3')
    manage.add_view(UserView(db.session, name='用户管理'))
    manage.add_view(AdminHomeView(Post, db.session, name='test'))
    return manage



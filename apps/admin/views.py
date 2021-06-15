#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name:     views.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.08.09   23:20
-------------------------------------------------------------------------------
   @Change:   2020.08.09
-------------------------------------------------------------------------------
"""
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla.view import ModelView
from apps.models import User


class UserView(ModelView):
    # Disable model creation
    can_create = False

    # Override displayed fields
    column_list = ('user_login', 'user_email', 'user_nicename', 'display_name', 'user_registered')

    def __init__(self, session, **kwargs):
        # You can pass name and other parameters if you want to
        super(UserView, self).__init__(User, session, **kwargs)


class AdminHomeView(ModelView):

    @expose('/')
    def index(self):
        return self.render('admin/base.html')

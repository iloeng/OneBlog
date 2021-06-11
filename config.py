#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name:     config.py
   @Desc:
   @Author:   liangz.org@gmail.com
   @Create:   2021.06.11   21:42
-------------------------------------------------------------------------------
   @Change:   2020.07.31
-------------------------------------------------------------------------------
"""

import os


class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@127.0.0.1:3306/wordpress?charset=utf8mb4"
    DEBUG = os.environ.setdefault('FLASK_DEBUG', 'True')

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_TEARDOWN = True
    SECRET_KEY = os.urandom(24)

    FLASK_POSTS_PER_PAGE = 15

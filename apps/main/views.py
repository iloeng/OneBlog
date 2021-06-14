#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name:     views.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.08.02   12:09
-------------------------------------------------------------------------------
   @Change:   2021.06.14
-------------------------------------------------------------------------------
"""
from flask import render_template, request, current_app
from apps.models import Post, User, Option
from apps.main import main


@main.route('/')
def home():
    header = {}
    page = request.args.get('page', 1, type=int)
    pagination = Post.query.filter_by(post_type='post').order_by(
        Post.post_date.desc()
    ).paginate(
        page,
        per_page=current_app.config['FLASK_POSTS_PER_PAGE'],
        error_out=False
    )

    header['blogname'] = Option.query.filter_by(
        option_name="blogname"
    ).first().option_value

    header['blogdesc'] = Option.query.filter_by(
        option_name="blogdescription"
    ).first().option_value

    posts = pagination.items
    return render_template('index.html', posts=posts, header=header)


@main.route('/<id>')
def article(id):
    article = Post.query.get(id)
    if article:
        return render_template('article-detail.html', article=article)
    else:
        return '404'


@main.route('/sort/<name>')
def sort(name):
    return

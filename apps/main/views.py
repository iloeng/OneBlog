#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name:     views.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.08.02   12:09
-------------------------------------------------------------------------------
   @Change:   2020.08.02
-------------------------------------------------------------------------------
"""
from flask import render_template, request, current_app
from apps.models import Post, User
from apps.main import main


@main.route('/')
def home():
    page = request.args.get('page', 1, type=int)
    pagination = Post.query.filter_by(post_type='post').order_by(
        Post.post_date.desc()
    ).paginate(
        page,
        per_page=current_app.config['FLASK_POSTS_PER_PAGE'],
        error_out=False
    )
    posts = pagination.items
    for i in posts:
        print(i.post_title)
        print(i.post_date)
        print(i.post_thumbnail)
        print(i.article_author)
    return render_template('base.html', posts=posts)


@main.route('/<id>')
def article(id):
    article = Post.query.get(id)
    if article:
        return render_template('article-detail.html', article=article)
    else:
        return '404'

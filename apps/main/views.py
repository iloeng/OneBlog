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
import re

from flask import render_template, request, current_app
from apps.models import Post, User, Option
from apps.main import main
from apps.main import assistant


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
    hot_posts = assistant.host_posts()
    recent_posts = assistant.recent_posts()
    guess_likes = assistant.guess_like()
    hot_tags = assistant.hot_tags()
    all_categories = assistant.all_categories()
    post_statistics = assistant.post_statistics()

    header = assistant.common_info()
    posts = pagination.items
    return render_template(
        'base.html', posts=posts, header=header, hot_posts=hot_posts,
        recent_posts=recent_posts, guess_likes=guess_likes, hot_tags=hot_tags,
        all_categories=all_categories, post_statistics=post_statistics
    )


@main.route('/<id>')
def article(id):
    article = Post.query.get(id)
    header = assistant.common_info()
    hot_posts = assistant.host_posts()
    recent_posts = assistant.recent_posts()
    guess_likes = assistant.guess_like()
    hot_tags = assistant.hot_tags()
    if article:
        return render_template(
            'post-detail.html', article=article, header=header,
            hot_posts=hot_posts, recent_posts=recent_posts,
            guess_likes=guess_likes, hot_tags=hot_tags
        )
    else:
        return '404'


@main.route('/sort/<name>')
def sort(name):
    return

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
    hot_posts = Post.query.filter_by(post_type='post').order_by(
        Post.comment_count.desc()
    ).all()[:6]

    header = common_info()
    posts = pagination.items
    return render_template(
        'base.html', posts=posts, header=header, hot_posts=hot_posts
    )


@main.route('/<id>')
def article(id):
    article = Post.query.get(id)
    header = common_info()
    hot_posts = Post.query.filter_by(post_type='post').order_by(
        Post.comment_count.desc()
    ).all()[:6]
    if article:
        return render_template(
            'post-detail.html', article=article, header=header,
            hot_posts=hot_posts
        )
    else:
        return '404'


@main.route('/sort/<name>')
def sort(name):
    return


def common_info():
    header = dict()
    header['blogname'] = Option.query.filter_by(
        option_name="blogname"
    ).first().option_value

    header['blogdesc'] = Option.query.filter_by(
        option_name="blogdescription"
    ).first().option_value

    header['siteurl'] = Option.query.filter_by(
        option_name="siteurl"
    ).first().option_value

    header['home'] = Option.query.filter_by(
        option_name="home"
    ).first().option_value.rstrip('/')
    return header

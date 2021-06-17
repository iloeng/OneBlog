#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name:     assistant.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2021.06.17   22:35
-------------------------------------------------------------------------------
   @Change:   2021.06.17
-------------------------------------------------------------------------------
"""

from apps.models import Post, User, Option


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


def host_posts():
    return Post.query.filter_by(post_type='post').order_by(
        Post.comment_count.desc()
    ).all()[:6]


def recent_posts():
    return Post.query.filter_by(post_type='post').order_by(
        Post.post_date.desc()
    ).all()[:6]
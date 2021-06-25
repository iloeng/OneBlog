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

import random

from apps.models import (
    Post, User, Option, TermTaxonomy, Term, Comment, TermRelationship
)


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


def hot_posts():
    return Post.query.filter_by(post_type='post').order_by(
        Post.comment_count.desc()
    ).all()[:6]


def recent_posts():
    return Post.query.filter_by(post_type='post').order_by(
        Post.post_date.desc()
    ).all()[:6]


def guess_like():
    """ randomly selected from all the articles """
    all = Post.query.filter_by(post_type='post').all()
    return random.sample(all, 6)


def hot_tags():
    """ get the top 30 tags """
    tags = list()
    tag_ids = TermTaxonomy.query.filter_by(taxonomy='post_tag').order_by(
        TermTaxonomy.count.desc()
    )[:30]
    for i in tag_ids:
        tags.append(Term.query.get(i.term_id))
    return tags


def all_categories():
    """ get all categories """
    all_category = list()
    categories = TermTaxonomy.query.filter_by(taxonomy='category').all()
    for category in categories:
        all_category.append(Term.query.get(category.term_id))
    all_category = sorted(all_category, key=lambda x: x.name, reverse=False)
    return all_category


def post_statistics():
    """ get the data of posts """
    post_statistic = dict()
    post_statistic['total_posts'] = len(Post.query.filter_by(post_type='post').all())
    post_statistic['total_comments'] = len(Comment.query.filter_by(user_id=0).all())
    post_statistic['total_pages'] = len(Post.query.filter_by(post_type='page').all())
    post_statistic['latest'] = Post.query.filter_by(post_type='post').order_by(
        Post.post_date.desc()
    )[0].post_date
    return post_statistic


def site_notifications():
    """ get latest 5 notifications of site """
    res = list()
    term_id = Term.query.filter_by(name='网站公告').first().term_id
    target_posts = TermRelationship.query.filter_by(term_taxonomy_id=term_id).all()
    for target in target_posts:
        res.append(Post.query.get(target.object_id))
    return res[::-1]

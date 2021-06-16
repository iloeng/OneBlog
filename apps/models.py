# coding: utf-8
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class CommentMeta(db.Model):

    __tablename__ = 'wp_commentmeta'

    meta_id = db.Column(db.BigInteger, primary_key=True)

    comment_id = db.Column(
        db.BigInteger,
        nullable=False,
        index=True,
        server_default=db.FetchedValue()
    )

    meta_key = db.Column(db.String(255, 'utf8mb4_unicode_ci'), index=True)

    meta_value = db.Column(db.String(collation='utf8mb4_unicode_ci'))


class Comment(db.Model):

    __tablename__ = 'wp_comments'

    __table_args__ = (
        db.Index(
            'comment_approved_date_gmt',
            'comment_approved',
            'comment_date_gmt'
        ),
    )

    comment_ID = db.Column(db.BigInteger, primary_key=True)

    comment_post_ID = db.Column(
        db.BigInteger,
        nullable=False,
        index=True,
        server_default=db.FetchedValue()
    )

    comment_author = db.Column(
        db.String(collation='utf8mb4_unicode_ci'),
        nullable=False
    )

    comment_author_email = db.Column(
        db.String(100, 'utf8mb4_unicode_ci'),
        nullable=False,
        index=True,
        server_default=db.FetchedValue()
    )

    comment_author_url = db.Column(
        db.String(200, 'utf8mb4_unicode_ci'),
        nullable=False,
        server_default=db.FetchedValue()
    )

    comment_author_IP = db.Column(
        db.String(100, 'utf8mb4_unicode_ci'),
        nullable=False,
        server_default=db.FetchedValue()
    )

    comment_date = db.Column(
        db.DateTime,
        nullable=False,
        server_default=db.FetchedValue()
    )

    comment_date_gmt = db.Column(
        db.DateTime,
        nullable=False,
        index=True,
        server_default=db.FetchedValue()
    )

    comment_content = db.Column(
        db.Text(collation='utf8mb4_unicode_ci'),
        nullable=False
    )

    comment_karma = db.Column(
        db.Integer,
        nullable=False,
        server_default=db.FetchedValue()
    )

    comment_approved = db.Column(
        db.String(20, 'utf8mb4_unicode_ci'),
        nullable=False,
        server_default=db.FetchedValue()
    )

    comment_agent = db.Column(
        db.String(255, 'utf8mb4_unicode_ci'),
        nullable=False,
        server_default=db.FetchedValue()
    )

    comment_type = db.Column(
        db.String(20, 'utf8mb4_unicode_ci'),
        nullable=False,
        server_default=db.FetchedValue()
    )

    comment_parent = db.Column(
        db.BigInteger,
        nullable=False,
        index=True,
        server_default=db.FetchedValue()
    )

    user_id = db.Column(
        db.BigInteger,
        nullable=False,
        server_default=db.FetchedValue()
    )

    comment_mail_notify = db.Column(
        db.Integer,
        nullable=False,
        server_default=db.FetchedValue()
    )


class Link(db.Model):

    __tablename__ = 'wp_links'

    link_id = db.Column(db.BigInteger, primary_key=True)

    link_url = db.Column(
        db.String(255, 'utf8mb4_unicode_ci'),
        nullable=False,
        server_default=db.FetchedValue()
    )

    link_name = db.Column(
        db.String(255, 'utf8mb4_unicode_ci'),
        nullable=False,
        server_default=db.FetchedValue()
    )

    link_image = db.Column(
        db.String(255, 'utf8mb4_unicode_ci'),
        nullable=False,
        server_default=db.FetchedValue()
    )

    link_target = db.Column(
        db.String(25, 'utf8mb4_unicode_ci'),
        nullable=False,
        server_default=db.FetchedValue()
    )

    link_description = db.Column(
        db.String(255, 'utf8mb4_unicode_ci'),
        nullable=False,
        server_default=db.FetchedValue()
    )

    link_visible = db.Column(
        db.String(20, 'utf8mb4_unicode_ci'),
        nullable=False,
        index=True,
        server_default=db.FetchedValue()
    )

    link_owner = db.Column(
        db.BigInteger,
        nullable=False,
        server_default=db.FetchedValue()
    )

    link_rating = db.Column(
        db.Integer,
        nullable=False,
        server_default=db.FetchedValue()
    )

    link_updated = db.Column(
        db.DateTime,
        nullable=False,
        server_default=db.FetchedValue()
    )

    link_rel = db.Column(
        db.String(255, 'utf8mb4_unicode_ci'),
        nullable=False,
        server_default=db.FetchedValue()
    )

    link_notes = db.Column(
        db.String(collation='utf8mb4_unicode_ci'),
        nullable=False
    )

    link_rss = db.Column(
        db.String(255, 'utf8mb4_unicode_ci'),
        nullable=False,
        server_default=db.FetchedValue()
    )


class Option(db.Model):

    __tablename__ = 'wp_options'

    option_id = db.Column(db.BigInteger, primary_key=True)

    option_name = db.Column(
        db.String(191, 'utf8mb4_unicode_ci'),
        nullable=False,
        unique=True,
        server_default=db.FetchedValue()
    )

    option_value = db.Column(
        db.String(collation='utf8mb4_unicode_ci'),
        nullable=False
    )

    autoload = db.Column(
        db.String(20, 'utf8mb4_unicode_ci'),
        nullable=False,
        index=True,
        server_default=db.FetchedValue()
    )


class PostMeta(db.Model):

    __tablename__ = 'wp_postmeta'

    meta_id = db.Column(db.BigInteger, primary_key=True)

    post_id = db.Column(
        db.BigInteger,
        nullable=False,
        index=True,
        server_default=db.FetchedValue()
    )

    meta_key = db.Column(db.String(255, 'utf8mb4_unicode_ci'), index=True)

    meta_value = db.Column(db.String(collation='utf8mb4_unicode_ci'))


class Post(db.Model):

    __tablename__ = 'wp_posts'

    __table_args__ = (
        db.Index(
            'type_status_date', 'post_type', 'post_status', 'post_date', 'ID'
        ),
    )

    ID = db.Column(
        db.BigInteger,
        primary_key=True
    )

    post_author = db.Column(
        db.BigInteger,
        nullable=False,
        index=True,
        server_default=db.FetchedValue()
    )

    post_date = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False,
        server_default=db.FetchedValue()
    )

    post_date_gmt = db.Column(
        db.DateTime,
        nullable=False,
        server_default=db.FetchedValue()
    )

    post_content = db.Column(
        db.String(collation='utf8mb4_unicode_ci'),
        nullable=False
    )

    post_title = db.Column(
        db.Text(collation='utf8mb4_unicode_ci'),
        nullable=False
    )

    post_excerpt = db.Column(
        db.Text(collation='utf8mb4_unicode_ci'),
        nullable=False
    )

    post_status = db.Column(
        db.String(20, 'utf8mb4_unicode_ci'),
        nullable=False,
        server_default=db.FetchedValue()
    )

    comment_status = db.Column(
        db.String(20, 'utf8mb4_unicode_ci'),
        nullable=False,
        server_default=db.FetchedValue()
    )

    ping_status = db.Column(
        db.String(20, 'utf8mb4_unicode_ci'),
        nullable=False,
        server_default=db.FetchedValue()
    )

    post_password = db.Column(
        db.String(255, 'utf8mb4_unicode_ci'),
        nullable=False,
        server_default=db.FetchedValue()
    )

    post_name = db.Column(
        db.String(200, 'utf8mb4_unicode_ci'),
        nullable=False, index=True,
        server_default=db.FetchedValue()
    )

    to_ping = db.Column(
        db.Text(collation='utf8mb4_unicode_ci'),
        nullable=False
    )

    pinged = db.Column(
        db.Text(collation='utf8mb4_unicode_ci'),
        nullable=False
    )

    post_modified = db.Column(
        db.DateTime,
        nullable=False,
        server_default=db.FetchedValue()
    )

    post_modified_gmt = db.Column(
        db.DateTime,
        nullable=False,
        server_default=db.FetchedValue()
    )

    post_content_filtered = db.Column(
        db.String(collation='utf8mb4_unicode_ci'),
        nullable=False
    )

    post_parent = db.Column(
        db.BigInteger,
        nullable=False,
        index=True,
        server_default=db.FetchedValue()
    )

    guid = db.Column(
        db.String(255, 'utf8mb4_unicode_ci'),
        nullable=False,
        server_default=db.FetchedValue()
    )

    menu_order = db.Column(
        db.Integer,
        nullable=False,
        server_default=db.FetchedValue()
    )

    post_type = db.Column(
        db.String(20, 'utf8mb4_unicode_ci'),
        nullable=False,
        server_default=db.FetchedValue()
    )

    post_mime_type = db.Column(
        db.String(100, 'utf8mb4_unicode_ci'),
        nullable=False,
        server_default=db.FetchedValue()
    )

    comment_count = db.Column(
        db.BigInteger,
        nullable=False,
        server_default=db.FetchedValue()
    )

    @property
    def article_category(self):
        """
        :return: return article's categories list
        """
        categories = TermRelationship.query.filter_by(object_id=self.ID).all()
        result = []
        for category in categories:
            term_taxonomy = TermTaxonomy.query.get(category.term_taxonomy_id)
            if term_taxonomy.taxonomy == 'category':
                result.append(Term.query.get(term_taxonomy.term_id).name)
        return result

    @property
    def post_thumbnail(self):
        """ get thumbnail photo's url """
        if self.post_type == 'post' and self.post_status == 'publish':
            _thumbnail_id = PostMeta.query.filter_by(
                post_id=self.ID, meta_key='_thumbnail_id'
            ).first()
            thumbnail = Post.query.filter_by(post_parent=self.ID).order_by(
                Post.post_date.asc()
            ).all()
            if _thumbnail_id:
                return Post.query.get(_thumbnail_id.meta_value).guid
            elif thumbnail:
                print(thumbnail)
                return Post.query.get(thumbnail[0].ID).guid
            else:
                return

    @property
    def post_views(self):
        """ get post's view number """
        if self.post_type == 'post' and self.post_status == 'publish':
            _thumbnail_id = PostMeta.query.filter_by(
                post_id=self.ID, meta_key='views'
            ).first()
            return _thumbnail_id.meta_value

    @property
    def article_author(self):
        """ get post author's display name """
        return User.query.get(self.post_author).display_name

    @property
    def nicename(self):
        """ get post author's real name """
        return User.query.get(self.post_author).user_nicename


class TermRelationship(db.Model):

    __tablename__ = 'wp_term_relationships'

    object_id = db.Column(
        db.BigInteger,
        primary_key=True,
        nullable=False,
        server_default=db.FetchedValue()
    )

    term_taxonomy_id = db.Column(
        db.BigInteger,
        primary_key=True,
        nullable=False,
        index=True,
        server_default=db.FetchedValue()
    )

    term_order = db.Column(
        db.Integer,
        nullable=False,
        server_default=db.FetchedValue()
    )

    @property
    def taxonomy(self):
        """
        :return: return taxonomy: tag or category
        """
        return TermTaxonomy.query.get(self.term_taxonomy_id).taxonomy


class TermTaxonomy(db.Model):

    __tablename__ = 'wp_term_taxonomy'

    __table_args__ = (
        db.Index('term_id_taxonomy', 'term_id', 'taxonomy'),
    )

    term_taxonomy_id = db.Column(db.BigInteger, primary_key=True)

    term_id = db.Column(
        db.BigInteger,
        nullable=False,
        server_default=db.FetchedValue()
    )

    taxonomy = db.Column(
        db.String(32, 'utf8mb4_unicode_ci'),
        nullable=False,
        index=True,
        server_default=db.FetchedValue()
    )

    description = db.Column(
        db.String(collation='utf8mb4_unicode_ci'),
        nullable=False
    )

    parent = db.Column(
        db.BigInteger,
        nullable=False,
        server_default=db.FetchedValue()
    )

    count = db.Column(
        db.BigInteger,
        nullable=False,
        server_default=db.FetchedValue()
    )

    @property
    def get_parent(self):
        """
        :return: return parent's taxonomy and name if has parent
        """
        if self.parent == 0:
            return 'Has no parent!'
        else:
            result = dict()
            parent_obj = TermTaxonomy.query.filter_by(term_id=self.parent).first()
            result['taxonomy'] = parent_obj.taxonomy
            result['name'] = Term.query.get(self.parent).name
            return result


class TermMeta(db.Model):

    __tablename__ = 'wp_termmeta'

    meta_id = db.Column(db.BigInteger, primary_key=True)

    term_id = db.Column(
        db.BigInteger,
        nullable=False,
        index=True,
        server_default=db.FetchedValue()
    )

    meta_key = db.Column(db.String(255, 'utf8mb4_unicode_ci'), index=True)

    meta_value = db.Column(db.String(collation='utf8mb4_unicode_ci'))


class Term(db.Model):

    __tablename__ = 'wp_terms'

    term_id = db.Column(db.BigInteger, primary_key=True)

    name = db.Column(
        db.String(200, 'utf8mb4_unicode_ci'),
        nullable=False,
        index=True,
        server_default=db.FetchedValue()
    )

    slug = db.Column(
        db.String(200, 'utf8mb4_unicode_ci'),
        nullable=False,
        index=True,
        server_default=db.FetchedValue()
    )

    term_group = db.Column(
        db.BigInteger,
        nullable=False,
        server_default=db.FetchedValue()
    )


class UserMeta(db.Model):

    __tablename__ = 'wp_usermeta'

    umeta_id = db.Column(db.BigInteger, primary_key=True)

    user_id = db.Column(
        db.BigInteger,
        nullable=False,
        index=True,
        server_default=db.FetchedValue()
    )

    meta_key = db.Column(db.String(255, 'utf8mb4_unicode_ci'), index=True)

    meta_value = db.Column(db.String(collation='utf8mb4_unicode_ci'))


class User(db.Model):

    __tablename__ = 'wp_users'

    ID = db.Column(db.BigInteger, primary_key=True)

    user_login = db.Column(
        db.String(60, 'utf8mb4_unicode_ci'),
        nullable=False,
        index=True,
        server_default=db.FetchedValue()
    )

    user_pass = db.Column(
        db.String(255, 'utf8mb4_unicode_ci'),
        nullable=False,
        server_default=db.FetchedValue()
    )

    user_nicename = db.Column(
        db.String(50, 'utf8mb4_unicode_ci'),
        nullable=False,
        index=True,
        server_default=db.FetchedValue()
    )

    user_email = db.Column(
        db.String(100, 'utf8mb4_unicode_ci'),
        nullable=False,
        index=True,
        server_default=db.FetchedValue()
    )

    user_url = db.Column(
        db.String(100, 'utf8mb4_unicode_ci'),
        nullable=False,
        server_default=db.FetchedValue()
    )

    user_registered = db.Column(
        db.DateTime,
        nullable=False,
        server_default=db.FetchedValue()
    )

    user_activation_key = db.Column(
        db.String(255, 'utf8mb4_unicode_ci'),
        nullable=False,
        server_default=db.FetchedValue()
    )

    user_status = db.Column(
        db.Integer,
        nullable=False,
        server_default=db.FetchedValue()
    )

    display_name = db.Column(
        db.String(250, 'utf8mb4_unicode_ci'),
        nullable=False,
        server_default=db.FetchedValue()
    )

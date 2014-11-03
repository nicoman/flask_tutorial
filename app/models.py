from app import db
from hashlib import md5


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    # Not a database field (one to many, relationship in one)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime)

    """
    Methods expected by Flask-Login
    """

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python3

    def avatar(self, size):
        """
        Rely on the gravatar service
        Doc: https://gravatar.com/site/implement/images
        """
        return 'http://www.gravatar.com/avatar/%s?d=mm&s=%d' % (
            md5(self.email.encode('utf-8')).hexdigest(),
            size)

    @staticmethod
    def make_unique_nickname(nickname):
        """
        This operation does not apply to any particular instance of the class
        so we coded the method as a static method
        """
        if User.query.filter_by(nickname=nickname).first() is None:
            return nickname
        version = 2
        while True:
            new_nickname = nickname + str(version)
            if User.query.filter_by(nickname=nickname).first() is None:
                break
            version += 1
        return new_nickname

    def __repr__(self):
        return '<User %r>' % (self.nickname)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)
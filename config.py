# -*- coding: utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))

# flask-sqlalchemy extension
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
# sqlalchemy-migrate extension
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
# flask-whooshalchemy extension
WHOOSH_BASE = os.path.join(basedir, 'search.db')

WTF_CSRF_ENABLE = True
SECRET_KEY = 'change-this-in-prod'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

# mail server settings
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
# Get user name and password from environment variables, in linux environments
# use export MAIL_USERNAME=your_username and export MAIL_PASSWORD=your_password
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

# administratir list email
ADMINS = ['nicolasmanso@gmail.com']

# pagination
POSTS_PER_PAGE = 3

# Search
MAX_SEARCH_RESULTS = 50

# available languages
LANGUAGES = {
    'en': 'English',
    'es': 'Español',
}

# microsoft translation service
MS_TRANSLATOR_CLIENT_ID = ''  # enter your MS translator app id here
MS_TRANSLATOR_CLIENT_SECRET = ''  # enter your MS translator app secret here

# DB performance
SQLALCHEMY_RECORD_QUERIES = True

# slow database query threshold (in seconds)
DATABASE_QUERY_TIMEOUT = 0.5
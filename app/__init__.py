import os

from flask import Flask
from flask.json import JSONEncoder
from flask.ext.sqlalchemy import SQLAlchemy

from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir, ADMINS, MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD
from flask.ext.mail import Mail
from flask.ext.babel import Babel, lazy_gettext
from momentjs import momentjs

app = Flask(__name__)

# Add config file
app.config.from_object('config')

# Define db object
db = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)
# Flask-Login needs to know what view logs users in
lm.login_view = 'login'
lm.login_message = lazy_gettext('Please lo in to access this page.')
# Need a path tmp
oid = OpenID(app, os.path.join(basedir, 'tmp'))
# Mail handler
mail = Mail(app)

# Sending errors by email
"""
Setup an email server easy
python -m smtpd -n -c DebuggingServer localhost:25
"""
if not app.debug:
    import logging
    from logging.handlers import SMTPHandler
    credentials = None
    if MAIL_USERNAME or MAIL_PASSWORD:
        credentials = (MAIL_USERNAME, MAIL_PASSWORD)
    mail_handler = SMTPHandler((MAIL_SERVER, MAIL_PORT),
        'no-reply@' + MAIL_SERVER, ADMINS,
        'microblog failure',
        credentials)
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)

# Expose momentsjs wrapper class as a global variable to all templates
app.jinja_env.globals['momentjs'] = momentjs

# Working with multiple languages
babel = Babel(app)

# Loggin file error
if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('tmp/microblog.log', 'a', 1 * 1024 * 1024, 10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('microblog startup')


class CustomJSONEncoder(JSONEncoder):
    """This class adds support for lazy translation texts to Flask's
    JSON encoder. This is necessary when flashing translated texts."""
    def default(self, obj):
        from speaklater import is_lazy_string
        if is_lazy_string(obj):
            try:
                return unicode(obj)  # python2
            except NameError:
                return str(obj)  # python3
        return super(CustomJSONEncoder, self).default(obj)


app.json_encoder = CustomJSONEncoder



from app import views, models
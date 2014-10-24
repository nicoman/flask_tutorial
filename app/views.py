from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

# Route recorators


@app.route('/')
@app.route('/index') #default only GET
def index():
    user = {'nickname': 'Miguel'}
    posts = [{'author': {'nickname': 'John'},
                'body': 'Beautiful day in La Plata!'},
            {'author': {'nickname': 'Susan'},
                'body': 'The Avenger movies was so cool!'}]
    # rendet_template (jinja2 backend)
    return render_template('index.html',
                            title='Home',
                            posts=posts,
                            user=user)


@app.route('/login', methods=['GET', 'POST']) # Accepts GET and POST request
def login():
    form = LoginForm()
    return render_template('login.html',
                            title="Sign In",
                            form=form)
from flask import render_template
from app import app

# Route recorators
@app.route('/')
@app.route('/index')

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

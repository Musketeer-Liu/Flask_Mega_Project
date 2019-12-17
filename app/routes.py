from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': "Musketeer"}
    posts = [
        {
            'author': {'username': 'Musketeer'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Paladin'},
            'body': 'The Avengers movie was cool!'
        }
    ]
    return render_template('index.html', title="Home", user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title="Sign In", form=form)

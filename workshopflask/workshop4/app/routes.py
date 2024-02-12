from app import app
from flask import Flask, render_template
@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'Patrick'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
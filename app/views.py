<<<<<<< HEAD
from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')

def index():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [  # fake array of posts
        {
        	'author': {'nickname': 'Ramesh'},
        	'body' : 'Woof Woof'

        },
        {
        	'author': {'nickname': 'Hansa'},
        	'body' : 'meow'
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)

@app.route('/login', methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for OpenID="%s", remember_me=%s' %
			(form.openid.data, str(form.remember_me.data)))
		return redirect('/index')
	return render_template("login.html", title='Sign In', form=form)
=======
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    return render_template('index.html',
                           title='Home',
                           user=user)
>>>>>>> 1d3453808b40e3d59a26673ebdf283aafbd14959

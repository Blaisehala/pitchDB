from flask import flash, render_template,url_for,redirect
from pitch import app
from pitch.forms import RegistrationForm, LoginForm

from pitch.models import User,Pitch                   







posts =[
  {
  'author': 'John Doe',
   'title': 'pitcher', 
   'content': 'pitchoned', 
   'date_posted':'April 1,2020'
   
   },
{'author': 'Blaise Hala', 'title': 'kode', 'content': 'pitchoned2', 'date_posted':'November 1,2020'}

]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=posts)




@app.route('/about')
def about():
  return render_template('about.html',title="About")


@app.route('/register', methods=['GET', 'POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    # flash message sends one time alert in flask
    user = User(username=form.username.data,email=form.email.data,password=form.password.data)
    db.session.add(user)
    db.session.commit()
    flash(f'Account created for {form.username.data}!','success')
    return redirect(url_for('home'))
  return render_template ('register.html',title='Register',form=form)


@app.route('/login')
def login():
  form = LoginForm()
  return render_template ('login.html',title='Login',form=form)

from . import auth
from flask import render_template,redirect,url_for,flash,request
from . forms import RegistrationForm, LoginForm
from .. import db
from .. models import User
from flask_login import login_user,logout_user,login_required




@auth.route('/register', methods=['GET', 'POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    # flash message sends one time alert in flask
    flash(f'Account created for {form.username.data}!','info')
    return redirect(url_for('home'))
  return render_template ('auth/register.html',title='Register',form=form)


@auth.route('/login',methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    if form.mail.data =='admin@blog.com' and  form.password.data == 'password':
      flash('You have logged in successfully.', 'info')
      return redirect(url_for('home'))
    else:
      flash('Login Unsuccessful.Please check mail or password' 'danger')
      

  return render_template ('auth/login.html',title='Login',form=form)




  
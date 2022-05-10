from crypt import methods
from flask import Flask, flash, render_template, url_for,flash,redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '89d9a808fe229b4cf4e66a3b51e52fdb'


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
    flash(f'Account created for {form.username.data}!','success')
    return redirect(url_for('home'))
  return render_template ('register.html',title='Register',form=form)


@app.route('/login')
def login():
  form = LoginForm()
  return render_template ('login.html',title='Login',form=form)



if __name__ == '__main__':
  app.run(debug=True)
  
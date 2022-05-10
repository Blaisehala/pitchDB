from datetime import  datetime
from flask import Flask, flash, render_template, url_for,flash,redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '89d9a808fe229b4cf4e66a3b51e52fdb'
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///site.db'
# database instance 
db= SQLAlchemy(app) 


class User(db.Model):
  # setting unique identifer
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
  password = db.Column(db.String(60),nullable=False)

  # one to many rlshp
  pitches = db.relationship('Pitch',backref='author', lazy=True)


# How object is printed
  def __repr__(self):
      return f"User('{self.username},'{self.email}','{self.image_file}')"



class Pitch(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable=False)
  date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  content = db.Column(db.Text, nullable=False)
  user_id = db.Column(db.Integer,db.ForeignKey('user.id'), nullable=False)


  # How object is printed
  def __repr__(self):
      return f"Pitch('{self.title},'{self.date_posted}')"









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
    flash(f'Account created for {form.username.data}!','info')
    return redirect(url_for('home'))
  return render_template ('register.html',title='Register',form=form)


@app.route('/login',methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    if form.mail.data =='admin@blog.com' and  form.password.data == 'password':
      flash('You have logged in successfully.', 'info')
      return redirect(url_for('home'))
    else:
      flash('Login Unsuccessful.Please check mail or password' 'danger')
      

  return render_template ('login.html',title='Login',form=form)



if __name__ == '__main__':
  app.run(debug=True)
  
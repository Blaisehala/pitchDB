from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET-KEY'] = '89d9a808fe229b4cf4e66a3b51e52fdb'


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


@app.route('/register')
def register():
  form = RegistrationForm()
  return render_template ('register.html',title='Register',form=form)


@app.route('/login')
def login():
  form = LoginForm()
  return render_template ('login.html',title='Login',form=form)



if __name__ == '__main__':
  app.run(debug=True)
  
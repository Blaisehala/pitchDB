from flask import Flask, render_template
app = Flask(__name__)


posts = [{'author': 'John', 'title': 'pitcher', 'content': 'pitchoned', 'date_posted':'April 1,2020'}]
[{'author': 'Blaise Hala', 'title': 'kode', 'content': 'pitchoned2', 'date_posted':'November 1,2020'}]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=posts)




@app.route('/about')
def about():
  return render_template('about.html')






if __name__ == '__main__':
  app.run(debug=True)
  
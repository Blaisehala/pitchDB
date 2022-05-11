from flask import flash, render_template,url_for,redirect,request,abort
from flask_login import login_user, current_user, logout_user, login_required
from pitch import app,db,bcrypt
from pitch.forms import RegistrationForm, LoginForm, PitchForm



from pitch.models import User,Pitch                   












@app.route('/')
@app.route('/home')
def home():
    posts = Pitch.query.all()
    return render_template('home.html',posts=posts)




@app.route('/about')
def about():
  return render_template('about.html',title="About")


@app.route('/register', methods=['GET', 'POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    # flash message sends one time alert in flask

    hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    user = User(username=form.username.data,email=form.email.data,password=hashed_pass)
    db.session.add(user)
    db.session.commit()
    flash(f'Account created for {form.username.data}!','success')
    return redirect(url_for('home'))
  return render_template ('register.html',title='Register',form=form)


@app.route("/login", methods=['POST','GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user, remember=form.remember.data)
           
            return  redirect(url_for('home'))
        else:
            flash(f'Login unsuccessful check password or email','danger')
    return render_template("login.html", title="Login", form=form)



@app.route("/pitch/new", methods=['POST','GET'])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        pitch = Pitch(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(pitch)
        db.session.commit()
        flash("Pitch was successfully created", "success")
        return redirect(url_for('home'))
    return render_template("create_pitch.html", title="New pitch", form = form, legend="Create a pitch")





@app.route("/pitch/update/<int:pitch_id>", methods=['POST','GET'])
@login_required
def update_pitch(pitch_id):
    pitch = Pitch.query.get_or_404(pitch_id)
    if current_user != pitch.author:
        abort(403)
    form = PitchForm()
    if form.validate_on_submit():
        pitch.title = form.title.data
        pitch.content = form.content.data
        db.session.commit()
        flash('Pitch updated successfully', 'success')
        return redirect(url_for('home'))
    elif request.method == 'GET':
        form.title.data = pitch.title
        form.content.data = pitch.content
    return render_template("create_pitch.html", title="Update pitch", form = form, legend="Update a pitch")


@app.route("/logout")
def logout():
    logout_user()
    return redirect('login')


@app.route("/pitch/delete/<int:pitch_id>", methods=['POST','GET'])
@login_required
def delete_pitch(pitch_id):
    pitch = Pitch.query.get_or_404(pitch_id)
    if current_user != pitch.author:
        abort(403)
    db.session.delete(pitch)
    db.session.commit()
    flash('Pitch was deleted successfully','success')
    return redirect(url_for('home'))
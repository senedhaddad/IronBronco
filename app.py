from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://senedhaddad:PostgresDB1!@localhost/test_coen'
#Change to location of databae.db

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class Users(UserMixin, db.Model):
    name = db.Column(db.String(30))
    email = db.Column(db.String(40), primary_key=True)
    password = db.Column(db.String(80))
    teamid = db.Column(db.String(20))
    bio = db.Column(db.String(200))
    swimming = db.Column(db.Float(3, 2))
    cycling = db.Column(db.Float(5, 2))
    running = db.Column(db.Float(4,2))
    id = db.Column(db.Integer(), primary_key=True)

class Team(UserMixin, db.Model):
    # id = db.Column(db.Integer)
    team = db.Column(db.String(20), primary_key=True)
    player1 = db.Column(db.String(30))
    player2 = db.Column(db.String(30))
    player3 = db.Column(db.String(30))
    swimming = db.Column(db.Float(3, 2))
    cycling = db.Column(db.Float(5, 2))
    running = db.Column(db.Float(4,2))

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Length(min=5, max=40)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('Remember me')

class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), Length(min=2, max=30)])
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=40)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
    bio = StringField('Bio', validators=[InputRequired(), Length(min=1, max=200)])


@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/about')
def about():
    return render_template('about.html')
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('dashboard'))

        return '<h1>Invalid email or password</h1>'
        #return '<h1>' + form.email.data + ' ' + form.password.data + '</h1>'

    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = Users(email=form.email.data, name=form.name.data, password=hashed_password, bio=form.bio.data)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('dashboard'))
        #return '<h1>New user has been created!</h1>'
        #return '<h1>' + form.email.data + ' ' + form.name.data + ' ' + form.password.data + '</h1>'

    return render_template('signup.html', form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.name)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/teamFormation')
def teamFormation():
    return render_template('teamFormation.html')

@app.route('/lookingForTeam')
def lookingForTeam():
    return render_template('lookingForTeam.html')

if __name__ == '__main__':
    app.run(debug=True)

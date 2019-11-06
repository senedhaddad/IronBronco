from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from decimal import Decimal
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////softwareEng/IronBronco/sqlite_example/other.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/peterferguson'

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class Users(UserMixin, db.Model):
    name = db.Column(db.String(30))
    email = db.Column(db.String(40), unique=True)
    password = db.Column(db.String(80))
    teamid = db.Column(db.Integer())
    bio = db.Column(db.String(200))
    lft = db.Column(db.Boolean(False))
    swimming = db.Column(db.Float(3, 2))
    cycling = db.Column(db.Float(5, 2))
    running = db.Column(db.Float(4,2))
    id = db.Column(db.Integer(), primary_key=True)

class Team(UserMixin, db.Model):
    id = db.Column(db.Integer,primary_key=True)
    team = db.Column(db.String(20), unique=True)
    player1 = db.Column(db.String(30))
    player2 = db.Column(db.String(30))
    player3 = db.Column(db.String(30))
    swimming = db.Column(db.Float(3, 2))
    cycling = db.Column(db.Float(5, 2))
    running = db.Column(db.Float(4,2))

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=40)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('Remember me')

class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), Length(min=2, max=30)])
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=40)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
    bio = StringField('Bio', validators=[InputRequired(), Length(min=1, max=200)])

class CreateTeamForm(FlaskForm):
    teamid = StringField('Create Team', validators=[InputRequired(), Length(min=2, max=30)])

class JoinTeamForm(FlaskForm):
    teamid = StringField('Join Team', validators=[InputRequired(), Length(min=2, max=30)])

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
        new_user = Team(team="shit",
                player1="null",
                player2="null",
                player3="null",
                swimming=0.0,
                cycling=0.0,
                running=0.0)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('signup.html', form=form)

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    id = session["user_id"]
    player = db.session.query(Users).get(id)
    # team = db.session.query(Team).get(player.teamid)     
    if request.method == 'POST':
        cycling=request.form['cycling']
        running=request.form['running']
        swimming=request.form['swimming']
        if not swimming:
            swimming=0.0
        if not cycling:
            cycling=0.0
        if not running:
            running=0.0
        try:
            player.cycling+=Decimal(cycling)
            if player.cycling >= 112:
                player.cycling = 112
            player.running+=Decimal(running)
            if player.running >= 26.2:
                player.running = 26.2
            player.swimming+=Decimal(swimming)
            if player.swimming >= 2.4:
                player.swimming = 2.4
            # team.cycling+=cycling
            # team.running+=running
            # team.swimming+=swimming
            db.session.commit()
        except Exception as e:
            return(str(e))

    # return render_template('dashboard.html')
    return render_template('dashboard.html',player=player)
    # return render_template('dashboard.html',player=player,team=team)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/teamFormation', methods=['GET','POST'])
@login_required
def teamFormation():
    id = session["user_id"]
    player = db.session.query(Users).get(id)
    formCT = CreateTeamForm()

    try:
        new_team = Team(team=formCT.teamid.data,
                player1="player",
                player2="null",
                player3="null",
                swimming=0.0,
                cycling=0.0,
                running=0.0)
        player.lft=False
        db.session.add(new_team)
        db.session.commit()
    except Exception as e:
        flash("Team name already in use")
        return redirect(url_for('index'))
        

    
    return render_template('teamFormation.html',formCT=formCT)

@app.route('/lookingForTeam')
def lookingForTeam():
    users = Users.query.all()
    return render_template('lookingForTeam.html',users=users)

if __name__ == '__main__':
    app.run(debug=True)

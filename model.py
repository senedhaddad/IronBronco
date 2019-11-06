from app import db

class Users(UserMixin, db.Model):
    __tablename__ = 'Users'
    name = db.Column(db.String(30))
    email = db.Column(db.String(40),unique=True)
    password = db.Column(db.String(80))
    teamid = db.Column(Integer())
    bio = db.Column(db.String(200))
    lft = db.Column(db.Boolean(False))
    swimming = db.Column(db.Float(3, 2))
    cycling = db.Column(db.Float(5, 2))
    running = db.Column(db.Float(4,2))
    id = db.Column(db.Integer(), primary_key=True)

class Team(UserMixin, db.Model):
    __tablename__ = 'Team'
    id = db.Column(db.Integer(), primary_key=True)
    team = db.Column(db.String(20),unique=True)
    player1 = db.Column(db.String(30))
    player2 = db.Column(db.String(30))
    player3 = db.Column(db.String(30))
    swimming = db.Column(db.Float(3, 2))
    cycling = db.Column(db.Float(5, 2))
    running = db.Column(db.Float(4,2))
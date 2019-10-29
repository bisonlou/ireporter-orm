from api.database import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    firstName = db.Column(db.String, nullable=True)
    lastname = db.Column(db.String, nullable=True)
    othernames = db.Column(db.String, nullable=True)
    phonenumber= db.Column(db.String, nullable=False)
    isadmin = db.Column(db.Boolean, default=False)
    
db.create_all()

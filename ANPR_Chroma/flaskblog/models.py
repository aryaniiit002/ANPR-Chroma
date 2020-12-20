from datetime import datetime
from flaskblog import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return LUser.query.get(int(user_id))


class User(db.Model,UserMixin):
    #__bind_key__ = 'site' default db
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    #password = db.Column(db.String(60), nullable=False)
    licenceplate = db.Column(db.String(10),unique=True, nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.licenceplate}')"

class LUser(db.Model,UserMixin):
    __bind_key__ = 'db2'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"LUser('{self.username}', '{self.email}''{self.image_file}',)"


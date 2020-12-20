from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail, Message

app = Flask(__name__)
mail=Mail(app)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site2.db'
app.config['SQLALCHEMY_BINDS'] = {
   'db2': 'sqlite:////home/aryan2019/Desktop/Flask/ANPR_Chroma/flaskblog/site2.db'
}
db = SQLAlchemy(app)

app.config['MAIL_SERVER'] = 'localhost'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] ='aryanbindal2015@gmail.com'
app.config['MAIL_PASSWORD'] = 'googlearyan'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail=Mail(app)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes
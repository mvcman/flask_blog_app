import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_rbac import RBAC

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database1.db' # connect by using sqlite
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # connect by using sqlite
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://post:password@localhost/post' # i f u connect by using postgres
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://post1:password@localhost/post1'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
rbac = RBAC(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['RBAC_USE_WHITE'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASSWORD')
mail = Mail(app)
from flaskblog import routes

from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flaskblog import db, login_manager, app, rbac
from flask_login import UserMixin
from sqlalchemy import Column, ForeignKey, Integer, String
from flask_rbac import RoleMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


users_roles = db.Table(
    'users_roles',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
)

# class UserRoles(db.Model):
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
#

@rbac.as_user_model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    roles = db.relationship(
        'Role',
        secondary=users_roles,
        backref='roles', lazy=True)


    def add_role(self, role):
        self.roles.append(role)

    def add_roles(self, roles):
        for role in roles:
            self.add_role(role)

    def get_roles(self):
        for role in self.roles:
            yield role

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return "User('{self.username}', '{self.email}', '{self.image_file}')"


# roles_parents = db.Table(
#     'roles_parents',
#     db.Column('role_id', db.Integer, db.ForeignKey('role.id')),
#     db.Column('parent_id', db.Integer, db.ForeignKey('role.id'))
# )
@rbac.as_role_model
class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))


    def __init__(self, name):
        RoleMixin.__init__(self)
        self.name = name

    # def add_parent(self, parent):
    #     # You don't need to add this role to parent's children set,
    #     # relationship between roles would do this work automatically
    #     self.parents.append(parent)
    #
    # def add_parents(self, *parents):
    #     for parent in parents:
    #         self.add_parent(parent)

    @staticmethod
    def get_by_name(name):
        return Role.query.filter_by(name=name).first()


# Define the Role data-model
# class Role(db.Model):
#     id = db.Column(db.Integer(), primary_key=True)
#     name = db.Column(db.String(50), unique=True)
#
# # Define the UserRoles association table
# class UserRoles(db.Model):
#     id = db.Column(db.Integer(), primary_key=True)
#     user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'))
#     role_id = db.Column(db.Integer(), db.ForeignKey('role.id', ondelete='CASCADE'))

# @rbac.as_role_model
# class Role(db.Model):
#     __tablename__ = 'roles'
#     id = db.Column(db.Integer(), primary_key=True)
#     name = db.Column(db.String(50), unique=True)
#
#     @staticmethod
#     def get_by_name(name):
#         return Role.query.filter_by(name=name).first()
#
#
#     # Define the UserRoles association table
# class PostRoles(db.Model):
#     __tablename__ = 'post_roles'
#     id = db.Column(db.Integer(), primary_key=True)
#     post_id = db.Column(db.Integer(), db.ForeignKey('post.id'))
#     role_id = db.Column(db.Integer(), db.ForeignKey('roles.id'))

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return "Post('{self.title}', '{self.date_posted}')"

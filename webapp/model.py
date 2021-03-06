from webapp import db, login
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String, nullable=False)
	text = db.Column(db.Text, nullable=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

	def __repr__(self):
		return f'<Post {self.title} - {self.id}>'

class Comment(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	author = db.Column(db.String, nullable=False)
	text = db.Column(db.Text, nullable=True)

	def __repr__(self):
		return f'<Comment by {self.author}: {self.text}>'
		
class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String, index=True, unique=True, nullable=False)
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))
	posts = db.relationship('Post', backref='author', lazy='dynamic')

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

	def __repr__(self):
		return '<User {} with id={}>'.format(self.username, self.id)

@login.user_loader
def load_user(id):
	return User.query.get(int(id))
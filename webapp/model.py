from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String, nullable=False)
	text = db.Column(db.Text, nullable=True)

	def __repr__(self):
		return f'<Post {self.title} - {self.id}>'

class Comment(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	author = db.Column(db.String, nullable=False)
	text = db.Column(db.Text, nullable=True)

	def __repr__(self):
		return f'<Comment by {self.author}: {self.text}>'
		
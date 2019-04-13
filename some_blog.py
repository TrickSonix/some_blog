from webapp import webapp
from webapp.model import db, User, Post, Comment

@webapp.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Comment': Comment}
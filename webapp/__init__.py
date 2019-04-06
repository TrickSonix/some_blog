from flask import Flask

from webapp.model import db

def create_app():
	app = Flask(__name__)
	app.config.from_pyfile('config.py')
	db.init_app(app)

	@app.route('/')
	def index():
		"""Возвращает страницу с постами и возможностью производить поиск по ним"""
		return "Страница с постами"

	@app.route('/admin')
	def administration():
		"""Если вход не выполнен, то Форма для входа, иначе Страница для создания и редактирования постов."""
		return "Вход и редактирование"

	return app
from webapp import webapp
from flask import render_template, flash, redirect, url_for
from webapp.forms import LoginForm

@webapp.route('/')
@webapp.route('/index')
def index():
    """Возвращает страницу с постами и возможностью производить поиск по ним"""
    return render_template('index.html')

@webapp.route('/admin')
def administration():
    """Если вход не выполнен, то Форма для входа, иначе Страница для создания и редактирования постов."""
    return "Вход и редактирование"

@webapp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Вы вошли как {form.username.data}, запомнить={form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='Войти', form=form)
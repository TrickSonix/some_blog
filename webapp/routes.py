from webapp import webapp, db
from flask import render_template, flash, redirect, url_for, request
from webapp.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user
from webapp.model import User
from werkzeug.urls import url_parse

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
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Войти', form=form)

@webapp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@webapp.route('/registration', methods=['GET', 'POST'])
def registration():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You are now registered user!')
        return redirect(url_for('login'))
    return render_template('registration.html', title='Register', form=form)
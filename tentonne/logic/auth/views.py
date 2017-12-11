from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, login_required

from . import auth
from .forms import LoginForm, RegisterForm
from ..models import User
from ... import db


# from ..user.forms import SearchForm

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        errorLogin = False;
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('user.index'))
        else:
            flash("Invalid password or username")
    return render_template('auth/login.html',
                           title='Авторизация',
                           form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('user.index'))


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    nickname=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        return redirect(url_for('auth.login'))
    return render_template('auth/signup.html',
                           form=form,
                           title='Регистрация')

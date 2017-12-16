from datetime import datetime
from flask import g
from flask_login import login_required, current_user
from flask import render_template, redirect, url_for, request, current_app

from ... import db
#from ..models import Comment, Post, Admin, User
from . import admin
from ..decorators import admin_required
#from ..user.forms import SearchForm
from .forms import NoticeForm

# @admin.before_request
# def before_request():
#     if current_user.is_authenticated:
#         current_user.last_seen = datetime.now()
#         db.session.add(current_user)
#         db.session.commit()
#     g.search_form = SearchForm()

@admin.route('/')
@admin_required
@login_required
def index():
    return render_template('admin/admin.html',
                           title='Панель администратора')


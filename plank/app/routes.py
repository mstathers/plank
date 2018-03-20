import os
from flask import render_template, redirect, flash, url_for, request
from werkzeug.urls import url_parse
from app import app, db, img
from flask_login import current_user, login_user, logout_user, login_required
from app.forms import LoginForm, RegistrationForm, UploadForm
from app.models import User, Post

@app.route("/")
def index():
    posts = Post.query.order_by(Post.timestamp.desc()).limit(5).all()
    return render_template("index.html", posts=posts)

@app.route("/upload", methods=['GET', 'POST'])
@login_required
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        filename = img.save(form.file.data)
        file_url = img.url(filename)
        post = Post(title=form.title.data, body=form.body.data, image=file_url, user_id = current_user.id )
        db.session.add(post)
        db.session.commit()
    else:
        file_url = ''

    return render_template("upload.html", form=form, file_url=file_url)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/login", methods=['GET', 'POST'])
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
    return render_template("login.html", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

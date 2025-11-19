from flask import request, render_template, redirect, url_for, flash, Blueprint
from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from app.extenshions import *
from flask_login import login_user, logout_user

auth = Blueprint("auth", __name__)

@auth.route("/register", methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if User.query.filter_by(email = email).first():
            flash("Email Already Exists", "danger")
            return redirect(url_for('auth.register'))
        
        if password != confirm_password:
            flash("Password Is Not Same", "danger")
            return redirect(url_for("auth.register"))
        
        if not email.endswith("@gmail.com"):
            flash("Email Must Be Ends With @gmail.com", "danger")
            return redirect(url_for("auth.register"))
        
        hashed_password = generate_password_hash(password)
        
        user = User(
            username = username,
            email = email,
            password = hashed_password
        )
        db.session.add(user)
        db.session.commit()
        flash("Account Were Created Successfully", "info")
        return redirect(url_for("auth.login"))
    return render_template('register.html')


@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            flash("You Logged in Successfully", "success")
            return redirect(url_for("main.rooms"))
        else:
            flash("Invalid email or password", "danger")
            return redirect(url_for("auth.login"))

    return render_template('login.html')

@auth.route("/logout")
def logout():
    logout_user()
    flash("You Logout Successfully", "info")
    return redirect(url_for("auth.login"))

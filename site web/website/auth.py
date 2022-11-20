from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user,current_user


auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET','POST'])
def login():
	print('hey')
	if request.method=='POST':
		email=request.form.get('email')
		password=request.form.get('password')
		print(email)	

		user=User.query.filter_by(email=email).first()
		
		if user:
			if check_password_hash(user.password,password):
				flash('Logged in successfully!', category='Success')
				login_user(user, remember=True)
				return redirect(url_for('views.home'))
			else :
				flash('Wrong credentials!', category='Error')


	return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
	if request.method == 'POST':
		email=request.form.get('email')
		firstName=request.form.get('firstName')
		password1=request.form.get('password1')
		password2=request.form.get('password2')

		user=User.query.filter_by(email=email).first()


		if user:
			flash('Email already used!', category='Error')
		elif len(email) <4:
			flash('Email must be greater than 1 characters.', category='Error')
		elif len(firstName) <2:
			flash('First name must be greater than 1 character.', category='Error')
		elif password1!=password2:
			flash('Passwords do not match.', category='Error')
		elif len(password1)>7:
			flash('Password must be less than 8 characters.', category='Error')
		else:
			new_user = User(email=email, firstName=firstName, password=generate_password_hash(password1, method='sha256'))
			db.session.add(new_user)
			db.session.commit()
			login_user(new_user,remember=True)
			flash('Account created!', category='Success')
			return redirect(url_for('views.home'))

	return render_template("sign_up.html", user=current_user)

from flask import render_template, url_for, flash, redirect
from UniHatch import app
from UniHatch.forms import RegistrationForm, LoginForm, searchForm 
from UniHatch.models import User
from flask_login import login_user, current_user, logout_user, login_required 

@app.route("/")
@app.route("/home")
def home():
    form = searchForm 
    if form.validate_on_submit():

    return render_template('home.html')
    #return "<h1>Home Page</h1>"

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.isauhtenticated: 
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bycrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(firstName = form.firstName.data, lastName = form.lastname.data, email = form.email.data, password = hashed_password
                    phoneNumber = form.phoneNumber.data, city = form.city.data, state = form.state.data, zipcode = form.zipcode.data,
                    Birthday = form.Birthday.data)
        db.session.add(user)
        db.session.commit
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)



@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.isauhtenticated: 
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data)
            login_user(user, remmber = form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html', title = 'Account')




from myproject import app, db
from flask import render_template, redirect, request, url_for, flash, abort
from flask_login import login_user, login_required, logout_user
from myproject.models import User, Suggestion, userName
from myproject.forms import LoginForm, RegistrationForm, AddForm, DelForm
from werkzeug.security import generate_password_hash, check_password_hash


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/welcome')
@login_required
def welcome_user():
    return render_template('welcome_user.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You logged out!')
    return redirect(url_for('home'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Grab the user from our User Models table
        user = User.query.filter_by(email=form.email.data).first()

        # Check that the user was supplied and the password is right
        # The verify_password method comes from the User object
        # https://stackoverflow.com/questions/2209755/python-operation-vs-is-not

        if user.check_password(form.password.data) and user is not None:
            # Log in the user

            login_user(user)
            flash('Logged in successfully.')

            # If a user was trying to visit a page that requires a login
            # flask saves that URL as 'next'.
            next = request.args.get('next')

            # So let's now check if that next exists, otherwise we'll go to
            # the welcome page.
            if next == None or not next[0] == '/':
                next = url_for('welcome_user')

            return redirect(next)
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering! Now you can login!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/add', methods=['GET', 'POST'])
def add_sug():

    form = AddForm()

    if form.validate_on_submit():

        name = form.name.data
        user_name = form.user_name.data
        new_sug = Suggestion(name)
        new_user_name = userName(user_name, new_sug.id)
        #db.session.add(new_sug)
        db.session.add_all([new_sug, new_user_name])
        db.session.commit()
        flash('Submitted...........!')
        flash('Thanks for your suggestion, hopefully it will resolve the 3D printing issues.')
        return redirect(url_for('flag_sug'))

    return render_template('add.html', form=form)

@app.route('/list')
def list_sug():

    suggest = Suggestion.query.all()
    username = userName.query.all()
    print(username)
    return render_template('list.html', suggest=suggest, username=username)

@app.route('/flag')
def flag_sug():
    return render_template('flag.html')

@app.route('/flag_remove')
def flag_remove():
    return render_template('flag_remove.html')

@app.route('/delete', methods=['GET', 'POST'])
def del_sug():

    form = DelForm()

    if form.validate_on_submit():

        id = form.id.data
        sug = Suggestion.query.get(id)
        db.session.delete(sug)
        db.session.commit()
        flash('Suggestion Deleted Successfully............!')
        return redirect(url_for('flag_remove'))
    return render_template('delete.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
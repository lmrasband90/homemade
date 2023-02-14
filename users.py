from flask_app import app
from flask import Flask, redirect, render_template, request, session, flash
from flask_app.models.user import User
from flask_app.models.material import Material
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/register-user', methods=['POST'])
def register_new_user():
    if not User.validate_new_user(request.form):
        return redirect('/')
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': request.form['password'],
        'business_name': request.form['business_name'],
        'password': bcrypt.generate_password_hash(request.form['password'])
    }
    print('register user controller')
    user_id = User.save_new_user(data)
    session['logged_in'] = user_id
    return redirect('/dashboard')



@app.route('/login-user', methods=['POST'])
def login_user():
    user = User.get_email(request.form)
    password = User.get_password(request.form)
    print(user)
    if not user:
        flash('******Email not in system******')
        return redirect('/')
    if not bcrypt.check_password_hash(password[0]['password'], request.form['password']):
        flash('******Incorrect password******')
        return redirect('/')
    print(user.id)
    session['logged_in'] = user.id
    return redirect('/dashboard')




@app.route('/dashboard')
def dashboard():
    if 'logged_in' not in session:
        print('You are not logged in')
        return redirect('/')
    user = User.fetch_account_info({'id': session['logged_in']})
    materials = Material.get_all_materials()
    return render_template('dashboard.html', materials = materials, user = user)





@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
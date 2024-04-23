from app import app
from flask import redirect, render_template, request
import users, visits

@app.route('/')
def index():
    visits.add_visit()
    counter = visits.get_counter()
    return render_template('index.html', counter=counter)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

    if not users.login(username, password):
        return render_template('error.html', message='Wrong username or password')

    return redirect('/profile')

@app.route('/logout')
def logout():
    users.logout()
    return redirect('/')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')

    if request.method == 'POST':
        username = request.form['username']
        
        if len(username) < 1 or len(username) > 20:
            return render_template('error.html', message='Username must have 1-20 characters')

        password1 = request.form['password1']
        password2 = request.form['password2']

        if password1 != password2:
            return render_template('error.html', message='Passwords do not match')
        if password1 == '':
            return render_template('error.html', message='Password is empty')

        role = request.form['role']
        if role not in ('1', '2'):
            return render_template('error.html', message='Unknown user role')

        if not users.register(username, password1, role):
            return render_template('error.html', message='Registartion failed, make sure to check username and password')
        
        return redirect('/')
    return render_template('register.html')

@app.route('/profile', methods=['GET'])
def profile():
    return render_template('profile.html')






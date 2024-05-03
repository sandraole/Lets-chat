from app import app
from flask import redirect, render_template, request, flash
import users, visits, messages

@app.route('/')
def index():
    visits.add_visit()
    counter = visits.get_counter()
    return render_template('index.html', counter=counter)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('layout.html')

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

    if not users.login(username, password):
        return render_template('error.html', message='Wrong username, password or no user created')

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
        password1 = request.form['password1']
        password2 = request.form ['password2']
        role = request.form['role']
        
        if len(username) < 1 or len(username) > 25:
            flash('Username must have 1-25 characters')
            return render_template('register.html')

        if password1 != password2:
            flash('Passwords do not match')
            return render_template('register.html')
        if password1 == '':
            flash('Password is empty')
            return render_template('register.html')

        if role not in ('1', '2'):
            flash('Unknown user role')
            return render_template('register.html')

        if not users.register(username, password1, role):
            flash('Registration failed, make sure to check username and password')
            return render_template('register.html')
        
        flash('User registration successful. You may now proceed to login.', 'success')
        return redirect('/')
    return render_template('register.html')

@app.route('/profile', methods=['GET'])
def profile():
    list = messages.get_list()
    return render_template('profile.html', count=len(list), messages=list)

@app.route('/send', methods=['POST'])
def send():
    content = request.form['content']
    if messages.send(content):
        return redirect('/profile')
    else:
        return render_template('error.html', message='Message failed to send.')
    

@app.route('/new')
def new():
    return render_template('new.html')

@app.route('/rules')
def rules():
    return render_template('rules.html')



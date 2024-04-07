from app import app
from flask import redirect, render_template, request, session
import users

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

    if not users.login(username, password):
        return render_template('error.html', message='Wrong username or password')
    
    return redirect('/login')

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
        return redirect('/register')
    return render_template('register.html')

# Add new course
@app.route('/add_course', methods=['POST'])
def add_course():
    pass


# Add new lesson
@app.route('/add_lesson', methods=['POST'])
def add_lesson():
    pass

# Sign up for the course
@app.route('/enroll_course', methods=['POST'])
def enroll_course():
    pass





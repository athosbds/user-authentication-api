from flask import Flask, render_template, redirect, url_for, request, session
from flask_bcrypt import Bcrypt
from models import create_database, create_table, search_user, connect_database, insert_user
create_database()
create_table()
app = Flask(__name__)
bycrpt = Bcrypt()
app.secret_key = 'MySecretKey1234'
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        name = request.form['nome']
        email = request.form['email']
        password = request.form['senha']
        if search_user(email):
            error = 'Email Existente'
        else:
            pass_hash = bycrpt.generate_password_hash(password).decode('utf-8')
            insert_user(name, email, pass_hash)
            return redirect(url_for('login'))
    return render_template('register.html', error=error)
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['senha']
        user = search_user(email)
        if user:
            name, hashed = user
            if hashed and bycrpt.check_password_hash(hashed, password):
                session['email'] = email
                session['name'] = name
                return redirect('/dashboard')
            else:
                error = 'Login incorreto: e-mail ou senha inválidos.'
        else:
            error = 'Login Incorreto: e-mail não encontrado.'
    return render_template('login.html', error=error)
if __name__ == '__main__':
    app.run(debug=True)
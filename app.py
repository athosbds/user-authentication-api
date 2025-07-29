from flask import Flask, render_template, redirect, url_for, request
from flask_bcrypt import Bcrypt
from models import create_database, create_table, search_user
create_table()
create_table()
app = Flask(__name__)
bycrpt = Bcrypt()
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['senha']
        hashed = search_user(email)
        if hashed == bycrpt.check_password_hash(password, hashed):
            return 'Logado Com Sucesso'
        else:
            return 'Login Incorreto'
    return render_template('login.html')
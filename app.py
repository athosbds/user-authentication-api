from flask import Flask, render_template, redirect, url_for, request
from flask_bcrypt import Bcrypt
from models import create_database, create_table, search_user
create_database()
create_table()
app = Flask(__name__)
bycrpt = Bcrypt()
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/cadastro', methods=['GET', 'POST'])
def register():
    # init logic register
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['senha']
        hashed = search_user(email)
        if hashed and bycrpt.check_password_hash(hashed, password):
            return 'Logado Com Sucesso'
        else:
            error = '❌ Login incorreto: e-mail ou senha inválidos'
    return render_template('login.html', error=error)
if __name__ == '__main__':
    app.run(debug=True)
from flask import render_template, redirect, session, request, flash
from flask_app import app

#Importación del modelo
from flask_app.models.users import User
from flask_app.models.citas import appointment

#Importación BCrypt
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registrate', methods=['POST'])
def registrate():
    #Validar la información ingresada
    if not User.valida_usuario(request.form):
        return redirect('/')

    pwd = bcrypt.generate_password_hash(request.form['password'])
    formulario = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": pwd
    }

  
    id = User.save(formulario) #Recibo el identificador de mi nuevo usuario

    session['user_id'] = id

    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():
  
    user = User.get_by_email(request.form) 

    if not user:
        flash('E-mail no encontrado', 'login')
        return redirect('/')

    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Password incorrecto', 'login')
        return redirect('/')

    session['user_id'] = user.id

    return redirect('/dashboard')



@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }

    user = User.get_by_id(formulario)

    citas = appointment.get_all()

    return render_template('dashboard.html', user=user, citas=citas)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
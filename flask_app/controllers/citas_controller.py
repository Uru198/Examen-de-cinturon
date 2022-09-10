from flask import render_template, redirect, session, request, flash
from flask_app import app

#Importación del modelo
from flask_app.models.users import User
from flask_app.models.citas import appointment

@app.route('/new/cita')
def new_cita():
    if 'user_id' not in session: 
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }

    user = User.get_by_id(formulario) 

    return render_template('new_cita.html', user=user)


@app.route('/create/cita', methods=['POST'])
def create_cita():
    if 'user_id' not in session: 
        return redirect('/')

    if not appointment.valida_cita(request.form): 
        return redirect('/new/cita')

    appointment.save(request.form)

    return redirect('/dashboard')


@app.route('/edit/cita/<int:id>') 
def edit_cita(id):
    if 'user_id' not in session: 
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }

    user = User.get_by_id(formulario) 
  
    formulario_cita = {"id": id}
    cita = appointment.get_by_id(formulario_cita)

   

    return render_template('edit_cita.html', user=user, cita=cita)

@app.route('/update/cita', methods=['POST'])
def update_cita():
    if 'user_id' not in session: 
        return redirect('/')
    
    if not appointment.valida_cita(request.form): 
        return redirect('/edit/cita/'+request.form['id'])
    
    if not appointment.valida_cita1(request.form): 
        return redirect('/edit/cita/'+request.form['id'])
    
    
    appointment.update(request.form)
    return redirect('/dashboard')

@app.route('/view/cita/<int:id>') 
def show_cita(id):
    if 'user_id' not in session: 
        return redirect('/')

    formulario = {
        "id": session['user_id']
    }

    user = User.get_by_id(formulario)


    formulario_cita = { "id": id }
    
    cita = appointment.get_by_id(formulario_cita)

    return render_template('show_cita.html', user=user, cita=cita)

@app.route('/delete/cita/<int:id>')
def delete_cita(id):
    if 'user_id' not in session: 
        return redirect('/')
    
    formulario = {"id": id}
    appointment.delete(formulario)

    return redirect('/dashboard')
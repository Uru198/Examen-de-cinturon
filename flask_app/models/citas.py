from flask_app.config.mysqlconnection import  connectToMySQL

from flask import flash

import re
import datetime

class appointment:

    def __init__(self, data):
        self.id = data['id']
        self.tasks = data['tasks']
        self.date_made = data['date_made']
        self.status = data['status']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

        #LEFT JOIN
        self.first_name = data['first_name']

    @staticmethod
    def valida_cita(formulario):
        es_valido = True

        if len(formulario['tasks']) < 3:
            flash('El nombre de la cita debe tener al menos 3 caracteres', 'cita')
            es_valido = False
        
        if formulario['date_made'] == "":
            flash('Ingrese una fecha', 'cita')
            es_valido = False
            
        if len(formulario['tasks']) < 3:
            flash('El nombre de la cita debe tener al menos 3 caracteres', 'cita1')
            es_valido = False
        
        if formulario['date_made'] == "":
            flash('Ingrese una fecha', 'cita1')
            es_valido = False
            
        
        
        #Consultar si ya existe ese correo electrónico
            

        return es_valido
    
    @staticmethod
    def valida_cita1(formulario):
        
     
        es_valido = True
        
        if len(formulario['tasks']) < 3:
            flash('El nombre de la cita debe tener al menos 3 caracteres', 'cita')
            es_valido = False
        
        if len(formulario['tasks']) < 3:
            flash('El nombre de la cita debe tener al menos 3 caracteres', 'cita1')
            es_valido = False
        
        if formulario['date_made'] == "":
            flash('Ingrese una fecha', 'cita')
            es_valido = False
            
        else:
            
            aut = formulario['date_made'].split('-')
            #["2020","06","11"]
        
            d1 = datetime.datetime(int.aut[0], int.aut[1], int.aut[2])
            d2 = datetime.datetime.now()
            if d2 < d1:
                flash('Ingrese una fecha futura', 'cita1')
                es_valido = False
            
      
        return es_valido
        
            


    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO appointment (tasks, date_made, status, user_id) VALUES (%(tasks)s, %(date_made)s, %(status)s, %(user_id)s) "
        result = connectToMySQL('citas').query_db(query, formulario)
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT appointment.*, first_name  FROM appointment LEFT JOIN users ON users.id = appointment.user_id;"
        results = connectToMySQL('citas').query_db(query) 
        appointments = []
        for appointment in results:
            
            appointments.append(cls(appointment)) 
        return appointments

    @classmethod
    def get_by_id(cls, formulario): 
        query = "SELECT appointment.*, first_name  FROM appointment LEFT JOIN users ON users.id = appointment.user_id WHERE appointment.id = %(id)s"
        result = connectToMySQL('citas').query_db(query, formulario) 
        appointment = cls(result[0])
        return appointment
    

    @classmethod
    def update(cls, formulario):
        query = "UPDATE appointment SET tasks=%(tasks)s, date_made=%(date_made)s, status=%(status)s, user_id=%(user_id)s WHERE id = %(id)s"
        result = connectToMySQL('citas').query_db(query, formulario)
        return result
    
   

    @classmethod
    def delete(cls, formulario): 
        query = "DELETE FROM appointment WHERE id = %(id)s"
        result = connectToMySQL('citas').query_db(query, formulario)
        return result
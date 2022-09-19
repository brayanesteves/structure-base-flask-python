from flask import Blueprint, request, render_template, redirect, url_for, flash
from config.mysql.config import mysql
from datetime import datetime

personas = Blueprint('personas', __name__, template_folder='app/templates')


@personas.route('/')
def index():    
    return "Hola"

@personas.route('/personas')
def personasMain():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM 0_Personas')
    data = cur.fetchall()
    cur.close()
    return render_template('personas/index.html', personas=data)


@personas.route('/add-personas', methods=['POST'])
def add_persona():
    if request.method == 'POST':
        cedula = request.form['cedula']
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        birthday = datetime.strptime(str(request.form['fechaDeNacimiento']), "%Y-%m-%d")
        try:
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO 0_Personas (cedula, nombres, apellidos, fechaDeNacimiento) VALUES (%s, %s, %s, %s)", (cedula, nombres, apellidos, birthday))
            mysql.connection.commit()
            #flash('Personas Added successfully')
            return redirect(url_for('personas.personasMain'))
        except Exception as e:
            flash(e.args[1])
            return redirect(url_for('personas.personasMain'))


@personas.route('/edit/<id>', methods=['POST', 'GET'])
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM 0_Personas WHERE Rfrnc = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('personas/edit-personas.html', persona=data[0])


@personas.route('/update/<id>', methods=['POST'])
def update_persona(id):
    if request.method == 'POST':
        cedula = request.form['cedula']
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        birthday = datetime.strptime(str(request.form['fechaDeNacimiento']), "%Y-%m-%d")
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE 0_Personas
            SET cedula = %s,
                nombres = %s,
                apellidos = %s,
                fechaDeNacimiento = %s
            WHERE Rfrnc = %s
        """, (cedula, nombres, apellidos, birthday, Rfrnc))
        #flash('Persona Updated Successfully')
        mysql.connection.commit()
        return redirect(url_for('personas.personasMain'))


@personas.route('/delete/<string:id>', methods=['POST', 'GET'])
def delete_persona(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM 0_Personas WHERE Rfrnc = {0}'.format(id))
    mysql.connection.commit()
    #flash('Personas Removed Successfully')
    return redirect(url_for('personas.personasMain'))
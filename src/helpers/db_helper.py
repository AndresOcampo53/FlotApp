import bdb

from flask import jsonify
from flask_sqlalchemy import *
from sqlalchemy import *
from src.db.db_models import *
from src.app import db
from src.db_schemas.schemas import *


def crear_usuario(request_data):
    # instanciamos variables con los datos que vienen en el request desde el controller
    nombre_usuario = request_data["nombre_usuario"]
    apellido_usuario = request_data["apellido_usuario"]
    cedula_usuario = request_data["cedula_usuario"]
    rol_usuario = request_data["rol_usuario"]

    try:
        new_usuario = usuarios(nombre_usuario, apellido_usuario, cedula_usuario, rol_usuario)
        db.session.add(new_usuario)
        db.session.commit()
        mensaje = {"mensaje": "OK"}
        return mensaje
    except Exception as e:
        mensaje = {"mensaje": "no se pudo hacer comit por estas razones: " + str(e)}
        return mensaje

def crear_log_usuario(request_data):
    # instanciamos variables con los datos que vienen en el request desde el controller
    fecha_login = request_data["fecha_login"]
    usuarios_id = request_data["usuarios_id"]

    try:
        new_log_usuario = logs_usuarios(fecha_login,usuarios_id)
        db.session.add(new_log_usuario)
        db.session.commit()
        mensaje = {"mensaje": "OK"}
        return mensaje
    except Exception as e:
        mensaje = {"mensaje": "no se pudo hacer comit por estas razones: " + str(e)}
        return mensaje


def crear_division(request_data):
    # instanciamos variables con los datos que vienen en el request desde el controller
    nombre_division = request_data["nombre_division"]

    try:
        new_division = division(nombre_division)
        db.session.add(new_division)
        db.session.commit()
        mensaje = {"mensaje": "OK"}
        return mensaje
    except Exception as e:
        mensaje = {"mensaje": "no se pudo hacer comit por estas razones: " + str(e)}
        return mensaje

def crear_centro_de_operaciones(request_data):
    # instanciamos variables con los datos que vienen en el request desde el controller
    nombre_centro_de_operaciones = request_data["nombre_centro_de_operaciones"]
    division_id = request_data["division_id"]

    try:
        new_centro_de_operaciones = centro_de_operaciones(nombre_centro_de_operaciones,division_id)
        db.session.add(new_centro_de_operaciones)
        db.session.commit()
        mensaje = {"mensaje": "OK"}
        return mensaje
    except Exception as e:
        mensaje = {"mensaje": "no se pudo hacer comit por estas razones: " + str(e)}
        return mensaje

def crear_vehiculo(request_data):
    # instanciamos variables con los datos que vienen en el request desde el controller
    placa = request_data["placa"]
    modelo = request_data["modelo"]
    capacidad = request_data["capacidad"]
    centro_de_operaciones_id = request_data["centro_de_operaciones_id"]

    try:
        new_vehiculo = vehiculo(placa, modelo, capacidad, centro_de_operaciones_id)
        db.session.add(new_vehiculo)
        db.session.commit()
        mensaje = {"mensaje": "OK"}
        return mensaje
    except Exception as e:
        mensaje = {"mensaje": "no se pudo hacer comit por estas razones: " + str(e)}
        return mensaje

def crear_formato_preoperacional(request_data):
    # instanciamos variables con los datos que vienen en el request desde el controller
    fecha = request_data["fecha"]
    formulario = request_data["formulario"]
    vehiculo_id =  request_data["vehiculo_id"]

    try:
        new_formato_preoperacional = formato_preoperacional(fecha, formulario, vehiculo_id)
        db.session.add(new_formato_preoperacional)
        db.session.commit()
        mensaje = {"mensaje": "OK"}
        return mensaje
    except Exception as e:
        mensaje = {"mensaje": "no se pudo hacer comit por estas razones: " + str(e)}
        return mensaje

def crear_llantas(request_data):
    # instanciamos variables con los datos que vienen en el request desde el controller
    vehiculo_id = request_data ["vehiculo_id"]
    marca = request_data ["marca"]
    posicion = request_data ["posicion"]
    profundidad = request_data ["profundidad"]
    kilometraje_instalacion = request_data ["kilometraje_instalacion"]
    fecha_instalacion = request_data["fecha_instalacion"]
    kilometraje_descarte = request_data ["kilometraje_descarte"]
    fecha_descarte = request_data ["fecha_descarte"]
    motivo_descarte = request_data ["motivo_descarte"]

    try:
        new_llantas = llantas(vehiculo_id, marca, posicion, profundidad, kilometraje_instalacion, fecha_instalacion,
                 kilometraje_descarte, fecha_descarte, motivo_descarte)
        db.session.add(new_llantas)
        db.session.commit()
        mensaje = {"mensaje": "OK"}
        return mensaje
    except Exception as e:
        mensaje = {"mensaje": "no se pudo hacer comit por estas razones: " + str(e)}
        return mensaje

def crear_tanqueada(request_data):
    # instanciamos variables con los datos que vienen en el request desde el controller
    vehiculo_id = request_data ["vehiculo_id"]
    tanqueada_litros = request_data ["tanqueada_litros"]
    fecha_tanqueada = request_data ["fecha_tanqueada"]
    costo_tanqueada = request_data ["costo_tanqueada"]
    kilometraje_tanqueada = request_data ["kilometraje_tanqueada"]
    combustible = request_data ["combustible"]

    try:
        new_tanqueada = tanqueada(vehiculo_id,tanqueada_litros,fecha_tanqueada, costo_tanqueada,kilometraje_tanqueada,combustible)
        db.session.add(new_tanqueada)
        db.session.commit()
        mensaje = {"mensaje": "OK"}
        return mensaje
    except Exception as e:
        mensaje = {"mensaje": "no se pudo hacer comit por estas razones: " + str(e)}
        return mensaje


def consultar_usuario(cedula):
    #hacemos las consultas
    try:
        query = db.session.query(usuarios).filter(usuarios.cedula_usuario == cedula).first()
        nombre = query.nombre_usuario
        apellido = query.apellido_usuario
        resultado = {"nombre":nombre,
                     "apellido":apellido}

        #result = usuarios_schema().dump(resultado)
        resultado = jsonify(resultado)
    except Exception as e:
        mensaje = {"mensaje":"se produjo el siguiente error: "+str(e)}
        resultado = mensaje,500
    return  resultado


def consultar_un_vehiculo(placa_a_buscar):
    #def __init__(self, placa, modelo, capacidad, centro_de_operaciones_id):
    try:
        query = db.session.query(vehiculo).filter(vehiculo.placa == placa_a_buscar).first()
        placa = query.placa
        modelo = query.modelo
        capacidad = query.capacidad
        centro_de_operaciones_id = query.centro_de_operaciones_id
        query_centro_operaciones = db.session.query(centro_de_operaciones).filter(centro_de_operaciones.id ==centro_de_operaciones_id).first()
        resultado = {"placa": placa,
                     "modelo": modelo,
                     "capacidad":capacidad,
                     "centro de operaciones":query_centro_operaciones.nombre_centro_de_operaciones}

        resultado = jsonify(resultado)
    except Exception as e:
        mensaje = {"mensaje":"se produjo el siguiente error: "+str(e)}
        resultado = mensaje, 500
    return resultado

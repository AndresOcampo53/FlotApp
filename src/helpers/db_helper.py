import bdb

from flask_sqlalchemy import *
from sqlalchemy import *
from src.db.db_models import *
from src.app import db


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
        mensaje = {"mensaje": "se pudo crear el usuario y hacer un commit()"}
        return mensaje
    except Exception as e:
        mensaje = {"mensaje": "no se pudo hacer comito por:" + str(e)}
        return mensaje

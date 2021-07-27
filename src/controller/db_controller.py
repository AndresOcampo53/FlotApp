from flask import Flask, request, Response
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from src.app import app
from src.helpers import db_helper
from src.helpers.db_helper import crear_usuario
from src.helpers.db_helper import crear_division
from src.helpers.db_helper import crear_centro_de_operaciones
from src.helpers.db_helper import crear_vehiculo
from src.helpers.db_helper import crear_formato_preoperacional
from src.helpers.db_helper import crear_llantas
from src.helpers.db_helper import crear_tanqueada

@app.route('/crear_usuario', methods=['POST'])
def crear_usuario_controller():
    # mandamos a un metodo helper el request completo
    json_data = request.json
    response_crear_usuario = crear_usuario(json_data)
    if response_crear_usuario["mensaje"] == "OK":
        response = Response(response=response_crear_usuario["mensaje"], status=200)
    else:
        response = Response(response=response_crear_usuario["mensaje"], status=500)
    return response

@app.route('/crear_log_usuario', methods=['POST'])
def crear_log_usuario():
    # mandamos a un metodo helper el request completo
    json_data = request.json
    response_crear_log_usuario = crear_log_usuario(json_data)
    if response_crear_log_usuario["mensaje"] == "OK":
        response = Response(response=response_crear_log_usuario["mensaje"], status=200)
    else:
        response = Response(response=response_crear_log_usuario["mensaje"], status=500)
    return response

@app.route('/crear_division', methods=['POST'])
def crear_division_controller():
    # mandamos a un metodo helper el request completo
    json_data = request.json
    response_crear_division = crear_division(json_data)
    if response_crear_division["mensaje"] == "OK":
        response = Response(response=response_crear_division["mensaje"], status=200)
    else:
        response = Response(response=response_crear_division["mensaje"], status=500)
    return response

@app.route('/crear_centro_de_operaciones', methods=['POST'])
def crear_centro_de_operaciones_controller():
    # mandamos a un metodo helper el request completo
    json_data = request.json
    response_crear_centro_de_operaciones = crear_centro_de_operaciones(json_data)
    if response_crear_centro_de_operaciones["mensaje"] == "OK":
        response = Response(response=response_crear_centro_de_operaciones["mensaje"], status=200)
    else:
        response = Response(response=response_crear_centro_de_operaciones["mensaje"], status=500)
    return response

@app.route('/crear_vehiculo', methods=['POST'])
def crear_vehiculo_controller():
    # mandamos a un metodo helper el request completo
    json_data = request.json
    response_crear_vehiculo = crear_vehiculo(json_data)
    if response_crear_vehiculo["mensaje"] == "OK":
        response = Response(response=response_crear_vehiculo["mensaje"], status=200)
    else:
        response = Response(response=response_crear_vehiculo["mensaje"], status=500)
    return response

@app.route('/crear_formato_preoperacional', methods=['POST'])
def crear_formato_preoperacional_controller():
    # mandamos a un metodo helper el request completo
    json_data = request.json
    response_formato_preoperacional = crear_formato_preoperacional(json_data)
    if response_formato_preoperacional["mensaje"] == "OK":
        response = Response(response=response_formato_preoperacional["mensaje"], status=200)
    else:
        response = Response(response=response_formato_preoperacional["mensaje"], status=500)
    return response

@app.route('/crear_llantas', methods=['POST'])
def crear_llantas_controller():
    # mandamos a un metodo helper el request completo
    json_data = request.json
    response_crear_llantas = crear_llantas(json_data)
    if response_crear_llantas["mensaje"] == "OK":
        response = Response(response=response_crear_llantas["mensaje"], status=200)
    else:
        response = Response(response=response_crear_llantas["mensaje"], status=500)
    return response

@app.route('/crear_tanqueada', methods=['POST'])
def crear_tanqueada_controller():
    # mandamos a un metodo helper el request completo
    json_data = request.json
    response_crear_tanqueada = crear_tanqueada(json_data)
    if response_crear_tanqueada["mensaje"] == "OK":
        response = Response(response=response_crear_tanqueada["mensaje"], status=200)
    else:
        response = Response(response=response_crear_tanqueada["mensaje"], status=500)
    return response
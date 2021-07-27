from flask import Flask, request, Response
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from src.app import app
from src.helpers import db_helper
from src.helpers.db_helper import crear_usuario


@app.route('/crear_usuario', methods=['POST'])
def crear_usuario_controller():
    # mandamos a un metodo helper el rquest completo
    json_data = request.json
    response_crear_usuario = crear_usuario(json_data)
    if response_crear_usuario["mensaje"] == "OK":
        response = Response(response=response_crear_usuario["mensaje"], status=200)
    else:
        response = Response(response=response_crear_usuario["mensaje"], status=500)
    return response


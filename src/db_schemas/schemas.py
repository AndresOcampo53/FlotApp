from src.db.db_models import *
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field, fields


class logs_usuario_schema(SQLAlchemySchema):
    class Meta:
        model = logs_usuarios

    id = auto_field()
    fecha_login = auto_field()
    usuarios_id = auto_field()

class usuarios_schema(SQLAlchemySchema):
    class Meta:
        model = usuarios

    id = auto_field()
    nombre_usuario = auto_field()
    apellido_usuario = auto_field()
    cedula_usuario = auto_field()
    rol_usuario = auto_field()
    logs_usuarios = fields.Nested(logs_usuario_schema)

class division_schema(SQLAlchemySchema):
    class Meta:
        model = division

    id = auto_field()
    nombre_division = auto_field()
    centro_de_operaciones = fields.Nested(centro_de_operaciones)

class centro_de_operaciones_schema(SQLAlchemySchema):
    class Meta:
        model = centro_de_operaciones

    id = auto_field()
    nombre_centro_de_operaciones = auto_field()
    division_id = auto_field()
    division = fields.Nested(division)
    vehiculo = fields.Nested(vehiculo)

class vehiculo_schema(SQLAlchemySchema):
    class Meta:
        model = vehiculo

    id = auto_field()
    placa = auto_field()
    modelo = auto_field()
    capacidad = auto_field()
    centro_de_operaciones_id = auto_field()
    centro_de_operaciones = fields.Nested(centro_de_operaciones)
    formato_preoperacional = fields.Nested(formato_preoperacional)
    llantas = fields.Nested(llantas)
    tanqueada = fields.Nested(tanqueada)

class formato_preoperacional_schema(SQLAlchemySchema):
    class Meta:
        model = formato_preoperacional

    id = auto_field()
    fecha = auto_field()
    formulario = auto_field()
    vehiculo_id = auto_field()
    vehiculo = fields.Nested(vehiculo)

class llantas_schema(SQLAlchemySchema):
    class Meta:
        model = llantas

    id = auto_field()
    vehiculo_id = auto_field()
    vehiculo = fields.Nested(vehiculo)
    marca = auto_field()
    posicion = auto_field()
    profundidad = auto_field()
    kilometraje_instalacion = auto_field()
    fecha_instalacion = auto_field()
    kilometraje_descarte = auto_field()
    fecha_descarte =auto_field()
    motivo_descarte = auto_field()

class tanqueada_schema(SQLAlchemySchema):
    class Meta:
        model = tanqueada

    id = auto_field()
    vehiculo_id = auto_field()
    vehiculo = fields.Nested(vehiculo)
    tanqueada_litros = auto_field()
    fecha_tanqueada = auto_field()
    costo_tanqueada = auto_field()
    kilometraje_tanqueada = auto_field()
    combustible = auto_field()
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




from marshmallow import schema, fields


class usuarios_schema(schema):
    id = fields.Integer()
    nombre_usuario = fields.String()
    apellido_usuario = fields.String()
    cedula_usuario = fields.String()
    rol_usuario = fields.String()


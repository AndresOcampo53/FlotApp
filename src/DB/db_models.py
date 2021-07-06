from src.app import db
from sqlalchemy.orm import relationship
from sqlalchemy import DateTime, Column, Integer, \
    String, ForeignKey, JSON, Float

"""------Definicion de tablas------"""


class usuarios(db.Model):
    __tablename__ = 'usuarios'
    id = Column(Integer(), primary_key=True)
    nombre_usuario = Column(String(30), nullable=False)
    apellido_usuario = Column(String(30), nullable=False)
    cedula_usuario = Column(String(30), nullable=False, unique=True)
    rol_usuario = Column(String(20), nullable=False)
    logsUsuarios = relationship("logs_usuarios", back_populates="usuarios")

    def __init__(self, nombre_usuario, apellido_usuario, cedula_usuario, rol_usuario):
        self.nombre_usuario = nombre_usuario
        self.apellido_usuario = apellido_usuario
        self.cedula_usuario = cedula_usuario
        self.rol_usuario = rol_usuario


class logs_usuarios(db.Model):
    __tablename__ = 'logs_usuarios'
    id = Column(Integer(), primary_key=True)
    fecha_login = Column(DateTime, nullable=False)
    usuarios_id = Column(Integer, ForeignKey('usuarios.id'))
    usuarios = relationship("usuarios", back_populates="logs_usuarios")

    def __init__(self, fecha_login, usuarios_id):
        self.fecha_login = fecha_login
        self.usuarios_id = usuarios_id


class centro_de_operaciones(db.Model):
    __tablename__ = 'centro_de_operaciones'
    id = Column(Integer(), primary_key=True)
    nombre_centro_de_operaciones = Column(String(50), nullable=False)
    division_id = Column(Integer, ForeignKey('division.id'))
    division = relationship("division", back_populates="centro_de_operaciones")
    vehiculo = relationship("vehiculo", back_populates="centro_de_operaciones")

    def __init__(self, nombre_centro_de_operaciones, division_id):
        self.nombre_centro_de_operaciones = nombre_centro_de_operaciones
        self.division_id = division_id


class division(db.Model):
    __tablename__ = 'division'
    id = Column(Integer(), primary_key=True)
    nombre_division = Column(String(50), nullable=False)
    centro_de_operaciones = relationship("centro_de_operaciones", back_populates="division")

    def __init__(self, nombre_division):
        self.nombre_division = nombre_division


class vehiculo(db.Model):
    __tablename__ = 'vehiculo'
    id = Column(Integer, primary_key=True)
    placa = Column(String(10), nullable=False, unique=True)
    modelo = Column(DateTime, nullable=False)
    capacidad = Column(Float, nullable=False)
    centro_de_operaciones_id = Column(Integer, ForeignKey("centro_de_operaciones.id"))
    centro_de_operaciones = relationship("centro_de_operaciones", back_populates="vehiculo")
    formato_preoperacional = relationship("formato_preoperacional", back_populates="vehiculo")
    llantas = relationship("llantas", back_populates="vehiculo")
    tanqueada = relationship("tanqueada", back_populates="vehiculo")

    def __init__(self, placa, modelo, capacidad, centro_de_operaciones_id):
        self.placa = placa
        self.modelo = modelo
        self.capacidad = capacidad
        self.centro_de_operaciones_id = centro_de_operaciones_id


class formato_preoperacional(db.Model):
    __tablename__ = 'formato_preoperacional'
    id = Column(Integer, primary_key=True)
    fecha = Column(DateTime, nullable=False)
    formulario = Column(JSON, nullable=False)
    vehiculo_id = Column(Integer, ForeignKey("vehiculo.id"))
    vehiculo = relationship("vehiculo", back_populates="formato_preoperacional")

    def __init__(self, fecha, formulario, vehiculo_id):
        self.fecha = fecha
        self.formulario = formulario
        self.vehiculo_id = vehiculo_id


class llantas(db.Model):
    __tablename__ = 'llantas'
    id = Column(Integer, primary_key=True)
    vehiculo_id = Column(Integer, ForeignKey("vehiculo.id"))
    vehiculo = relationship("vehiculo", back_populates="llantas")
    marca = Column(String, nullable=False)
    posicion = Column(Integer, nullable=False)
    profundidad = Column(Float, nullable=False)
    kilometraje_instalacion = Column(Integer, nullable=False)
    fecha_instalacion = Column(DateTime, nullable=False)
    kilometraje_descarte = Column(Integer, nullable=True)
    fecha_descarte = Column(DateTime, nullable=True)
    motivo_descarte = Column(String, nullable=True)

    def __init__(self, vehiculo_id, marca, posicion, profundidad, kilometraje_instalacion, fecha_instalacion,
                 kilometraje_descarte, fecha_descarte, motivo_descarte):
        self.vehiculo_id = vehiculo_id
        self.marca = marca
        self.posicion = posicion
        self.profundidad = profundidad
        self.kilometraje_instalacion = kilometraje_instalacion
        self.kilometraje_descarte = kilometraje_descarte
        self.fecha_descarte = fecha_descarte
        self.motivo_descarte = motivo_descarte


class tanqueada(db.Model):
    __tablename__ = 'tanqueada'
    id = Column(Integer, primary_key=True)
    vehiculo_id = Column(Integer, ForeignKey("vehiculo.id"))
    vehiculo = relationship("vehiculo", back_populates="tanqueada")
    tanqueada_litros = Column(Float, nullable=False)
    fecha_tanqueada = Column(DateTime, nullable=False)
    costo_tanqueada = Column(Float, nullable=False)
    kilometraje_tanqueada = Column(Integer, nullable=False)
    combustible = Column(String, nullable=False)

    def __init__(self, vehiculo_id,tanqueada_litros,fecha_tanqueada, costo_tanqueada,kilometraje_tanqueada,combustible):
        self.vehiculo_id = vehiculo_id
        self.tanqueada_litros = tanqueada_litros
        self.fecha_tanqueada = fecha_tanqueada
        self.costo_tanqueada = costo_tanqueada
        self.kilometraje_tanqueada = kilometraje_tanqueada
        self.combustible = combustible


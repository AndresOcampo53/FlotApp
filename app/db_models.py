import enum
import uuid

from db import Base
from flask_security import UserMixin, RoleMixin
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Boolean, DateTime, Column, Integer, \
    String, ForeignKey, JSON, Float, TypeDecorator
from sqlalchemy.dialects.postgresql import UUID

"""------Definicion de tablas------"""


class usuarios(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer(), primary_key=True)
    nombre_usuario = Column(String(30), nullable=False)
    apellido_usuario = Column(String(30), nullable=False)
    cedula_usuario = Column(String(30), nullable=False, unique=True)
    rol_usuario = Column(String(20), nullable=False)
    logsUsuarios = relationship("logsusuarios", back_populates="usuarios")

    def __init__(self, nombre_usuario, apellido_usuario, cedula_usuario, rol_usuario):
        self.nombre_usuario = nombre_usuario
        self.apellido_usuario = apellido_usuario
        self.cedula_usuario = cedula_usuario
        self.rol_usuario = rol_usuario


class logsUsuarios(Base):
    __tablename__ = 'logsUsuarios'
    id = Column(Integer(), primary_key=True)
    fecha_login = Column(DateTime, nullable=False)
    usuarios_id = Column(Integer, ForeignKey('usuarios.id'))
    usuarios = relationship("usuarios", back_populates="logsUsuarios")

    def __init__(self, fecha_login, usuarios_id):
        self.fecha_login = fecha_login
        self.usuarios_id = usuarios_id


class CentroDeOperaciones(Base):
    __tablename__ = 'CentroDeOperaciones'
    id = Column(Integer(), primary_key=True)
    nombre_centro_de_operaciones = Column(String(50), nullable=False)
    division_id = (Integer, ForeignKey('Division.id'))
    Division = relationship("Division", back_populates="CentroDeOperaciones")
    Vehiculo = relationship("Vehiculo", back_populates = "CentroDeOperaciones")

    def __init__(self, nombre_centro_de_operaciones, division_id):
        self.nombre_centro_de_operaciones = nombre_centro_de_operaciones
        self.division_id = division_id


class Division(Base):
    __tablename__ = 'Division'
    id = Column(Integer(), primary_key=True)
    nombre_division = Column(String(50), nullable=False)
    CentroDeOperaciones = relationship("CentroDeOperaciones", back_populates="Division")

    def __init__(self, nombre_division):
        self.nombre_division = nombre_division


class Vehiculo(Base):
    __tablena__ = 'Vehiculo'
    id = Column(Integer, primary_key=True)
    placa = Column(String(10), nullable=False, unique=True)
    modelo = Column(DateTime, nullable=False)
    capacidad = Column(Float, nullable=False)
    centro_de_operaciones_id = Column(Integer, ForeignKey("CentroDeOperaciones.id"))
    CentroDeOperaciones = relationship("Vehiculo", back_populates= "CentroDeOperaciones")

    def __init__(self,placa,modelo,capacidad,centro_de_operaciones_id):
        self.placa = placa
        self.modelo = modelo
        self.capacidad = capacidad
        self.centro_de_operaciones_id = centro_de_operaciones_id






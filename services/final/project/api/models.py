# services/users/project/api/models.py
from sqlalchemy.sql import func
from project import db


class P01(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)
    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'stock': self.stock,
            'price': self.price,
            'active': self.active
        }

    def __init__(self, name, stock, price):
        self.name = name
        self.stock = stock
        self.price = price

class P02(db.Model):
    __tablename__ = 'proveedores'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    address = db.Column(db.String(128), nullable=False)
    ruc = db.Column(db.Integer, nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)
    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'ruc': self.ruc,
            'active': self.active
        }

    def __init__(self, name, address, ruc):
        self.name = name
        self.address = address
        self.ruc = ruc

class T01(db.Model):
    __tablename__ = 'trabajadores'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    position = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)
    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'position': self.position,
            'active': self.active
        }

    def __init__(self, name, position):
        self.name = name
        self.position = position

class S01(db.Model):
    __tablename__ = 'sucursales'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    country = db.Column(db.String(128), nullable=False)
    city = db.Column(db.String(128), nullable=False)
    floor = db.Column(db.Integer, nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)
    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'country': self.country,
            'city': self.city,
            'floor': self.floor,
            'active': self.active
        }

    def __init__(self, country, city, floor):
        self.country = country
        self.city = city
        self.floor = floor

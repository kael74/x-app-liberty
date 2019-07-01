# services/store/project/api/store.py

from flask import Blueprint, jsonify, request, render_template, redirect
from project.api.models import P01, P02, T01, S01
from project import db
from sqlalchemy import exc


store_blueprint = Blueprint('store', __name__, template_folder='./templates')


@store_blueprint.route('/store/ping', methods=['GET'])
def ping_pong():
    return jsonify({
       'status': 'success',
       'message': 'pong!'
    })


@store_blueprint.route('/store', methods=['POST'])
def add_user():
    post_data = request.get_json()
    response_object = {
        'status': 'fail',
        'message': 'Invalid payload.'
    }
    if not post_data:
        return jsonify(response_object), 400
    username = post_data.get('username')
    email = post_data.get('email')
    try:
        user = User.query.filter_by(email=email).first()
        if not user:
            db.session.add(User(username=username, email=email))
            db.session.commit()
            response_object['status'] = 'success'
            response_object['message'] = f'{email} ha sido agregado!'
            return jsonify(response_object), 201
        else:
            response_object['message'] = 'Disculpe. Este email ya existe.'
            return jsonify(response_object), 400
    except exc.IntegrityError:
        db.session.rollback()
        return jsonify(response_object), 400


@store_blueprint.route('/store/p01/<p01_id>', methods=['GET'])
def get_single_products(p01_id):
    """Obtener detalles de ususario unico"""
    response_object = {
        'status': 'fail',
        'message': 'el producto no existe'
    }
    try:
        producto = P01.query.filter_by(id=int(p01_id)).first()
        if not user:
            return jsonify(response_object), 404
        else:
            response_object = {
                'status': 'success',
                'data': {
                    'id': producto.id,
                    'name': producto.name,
                    'stock': producto.stock,
                    'price': producto.price,
                    'active': producto.active
                    }
            }
        return jsonify(response_object), 200
    except ValueError:
        return jsonify(response_object), 404


@store_blueprint.route('/store', methods=['GET'])
def get_all():
    """Obteniendo todos los productos"""
    response_object = {
        'status': 'success',
        'data': {
            'products': [producto.to_json() for producto in P01.query.all()],
            'providers': [proveedor.to_json() for proveedor in P02.query.all()],
            'workers': [trabajador.to_json() for trabajador in T01.query.all()],
            'subsidiary': [sucursal.to_json() for sucursal in S01.query.all()]
        }
    }
    return jsonify(response_object), 200

@store_blueprint.route('/delp01/<p01_id>', methods=['POST', 'GET'])
def delete_products(p01_id):
    producto = P01.query.filter_by(id=int(p01_id)).first()
    db.session.delete(producto)
    db.session.commit()
    return redirect("/")

@store_blueprint.route('/delp02/<p02_id>', methods=['POST', 'GET'])
def delete_providers(p02_id):
    proveedor = P02.query.filter_by(id=int(p02_id)).first()
    db.session.delete(proveedor)
    db.session.commit()
    return redirect("/")

@store_blueprint.route('/delt03/<t01_id>', methods=['POST', 'GET'])
def delete_workers(t01_id):
    trabajador = T01.query.filter_by(id=int(t01_id)).first()
    db.session.delete(trabajador)
    db.session.commit()
    return redirect("/")

@store_blueprint.route('/dels01/<s01_id>', methods=['POST', 'GET'])
def delete_subsidiary(s01_id):
    sucursal = S01.query.filter_by(id=int(s01_id)).first()
    db.session.delete(sucursal)
    db.session.commit()
    return redirect("/")

@store_blueprint.route('/p01', methods=['GET', 'POST'])
def add_products():
    if request.method == 'POST':
        name = request.form['name']
        stock = request.form['stock']
        price = request.form['price']
        db.session.add(P01(name=name, stock=stock, price=price))
        db.session.commit()
        return redirect("/")

@store_blueprint.route('/p02', methods=['GET', 'POST'])
def add_providers():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        ruc = request.form['ruc']
        db.session.add(P02(name=name, address=address, ruc=ruc))
        db.session.commit()
        return redirect("/")

@store_blueprint.route('/t01', methods=['GET', 'POST'])
def add_workers():
    if request.method == 'POST':
        name = request.form['name']
        position = request.form['position']
        db.session.add(T01(name=name, position=position))
        db.session.commit()
        return redirect("/")

@store_blueprint.route('/s01', methods=['GET', 'POST'])
def add_subsidiary():
    if request.method == 'POST':
        country = request.form['country']
        city = request.form['city']
        floor = request.form['floor']
        db.session.add(S01(country=country, city=city, floor=floor))
        db.session.commit()
        return redirect("/")

@store_blueprint.route('/formp01/<id>', methods=['GET'])
def show_form(id):
    p01_id= P01.query.filter_by(id=int(id)).first()
    return render_template('upp01.html', products=p01_id)


@store_blueprint.route('/upp01/<id>', methods=['POST', 'GET'])
def update_product(id):
    producto = P01.query.filter_by(id=int(id)).first()
    name = request.form['name']
    stock = request.form['stock']
    price = request.form['price']

    producto.name = name
    producto.stock = stock
    producto.price = price

    db.session.commit()
    return redirect("/")


@store_blueprint.route('/', methods=['GET', 'POST'])
def index():

    products = P01.query.all()
    providers = P02.query.all()
    workers = T01.query.all()
    subsidiary = S01.query.all()
    return render_template('index.html', products=products, providers=providers, workers=workers, subsidiary=subsidiary)

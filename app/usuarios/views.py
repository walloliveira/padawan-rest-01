from flask import Blueprint, jsonify

usuarios_routes = Blueprint('app.usuarios', __name__)


@usuarios_routes.route('/usuarios')
def get():
    return jsonify([
        {'id': ''}
    ])

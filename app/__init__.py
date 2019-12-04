from flask import Flask
from app.usuarios.views import usuarios_routes

app = Flask(__name__)
app.register_blueprint(usuarios_routes)

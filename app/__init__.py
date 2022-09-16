from csv import excel
from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect

from .models.ModeloLibro import ModeloLibro
from .models.ModeloUsuario import ModeloUsuario

from .models.entities.Usuario import Usuario

app = Flask(__name__)

csrf = CSRFProtect()
db = MySQL(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():

    if request.method == 'POST':

        usuario = Usuario(
            None, request.form['usuario'], request.form['password'], None)
        usuario_logeado = ModeloUsuario.login(db, usuario)
        if usuario_logeado != None:
            return redirect(url_for('index'))
        else:
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')
# request.form['usuario'] == 'admin1' and request.form['password'] == '123456':


@app.route('/libros')
def listar_libros():
    try:
        libros = ModeloLibro.listar_libros(db)
        data = {
            'libros': libros
        }
        return render_template('listado_libros.html', data=data)
    except Exception as ex:
        print(ex)


def pagina_no_encontrada(error):
    return render_template('errores/404.html'), 404


def inicializar_app(config):
    app.config.from_object(config)
    csrf.init_app(app)
    app.register_error_handler(404, pagina_no_encontrada)
    return app

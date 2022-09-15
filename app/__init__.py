from csv import excel
from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)

csrf = CSRFProtect()
db = MySQL(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    """
    print(request.method)
    print(request.form['usuario'])
    print(request.form['password'])
    """

    if request.method == 'POST':
        # print(request.form['usuario'])
        # print(request.form['password'])
        if request.form['usuario'] == 'admin1' and request.form['password'] == '123456':
            return redirect(url_for('index'))
        else:
            return 'intente nuevamente'
    else:
        return render_template('auth/login.html')


@app.route('/libros')
def listar_libros():
    try:
        cursor = db.connection.cursor()
        sql = """SELECT isbn, titulo, anoedicion, precio, apellidos, nombres
        FROM libro join autor ON autor_id = id 
        ORDER BY titulo ASC"""
        cursor.execute(sql)
        data = cursor.fetchall()
        print(data)
        data={
            "libros":data
        }
        
        # return "Okasa. Número de libros: {0}".format(len(data))
        return render_template('listado_libros.html', data=data)
    except Exception as ex:
        raise Exception(ex)


def pagina_no_encontrada(error):
    return render_template('errores/404.html'), 404


def inicializar_app(config):
    app.config.from_object(config)
    csrf.init_app(app)
    app.register_error_handler(404, pagina_no_encontrada)
    return app

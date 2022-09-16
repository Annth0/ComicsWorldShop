from distutils.util import check_environ
from lib2to3.pgen2.pgen import generate_grammar
from werkzeug.security import generate_password_hash, check_password_hash


class Usuario():

    def __init__(self, id, usuario, password, tipousuario):
        self.id = id
        self.Usuario = usuario
        self.password = password
        self.tipousuario = tipousuario

    def encriptar_password(password):
        encriptado = generate_password_hash(password)
        coincide = check_password_hash(encriptado, password)
        return coincide

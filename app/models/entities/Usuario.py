from distutils.util import check_environ
from lib2to3.pgen2.pgen import generate_grammar
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Usuario(UserMixin):

    def __init__(self, id, usuario, password, tipousuario):
        self.id = id
        self.usuario = usuario
        self.password = password
        self.tipousuario = tipousuario
        
    @classmethod
    def verifictar_password(self, encriptado,password):
        coincide = check_password_hash(encriptado, password)
        return coincide

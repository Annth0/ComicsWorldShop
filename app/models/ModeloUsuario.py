from werkzeug.security import check_password_hash

from app.models.entities.Usuario import Usuario


class ModeloUsuario():
    @classmethod
    def login(self, db, usuario):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT id, usuario, password FROM usuario WHERE usuario = '{0}'".format(
                usuario.usuario)
            cursor.execute(sql)
            data = cursor.fetchone()
            coincide = check_password_hash(data[2], usuario.password)
            if coincide:
                usuario_logeado = Usuario(data[0], data[1], None, None)
                return usuario_logeado
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

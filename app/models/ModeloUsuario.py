from werkzeug.security import check_password_hash 

class ModeloUsuario():
    @classmethod
    def login(self, db, usuario):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT id, usuario, password FROM usuario WHERE usuario = '{0}'".format(
                usuario.usuario)
            cursor.execute(sql)
            data = cursor.fetchone()
            #print(data)
            coincide=check_password_hash(data[2],usuario.password)
            return coincide
        except Exception as ex:
            raise Exception(ex)

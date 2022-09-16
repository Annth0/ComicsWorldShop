from .entities.Autor import Autor
from .entities.Libro import Libro

class ModeloLibro():
    
    @classmethod
    def listar_libros(self, db):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT isbn, titulo, anoedicion, precio, apellidos, nombres
                    FROM libro join autor ON autor_id = id 
                    ORDER BY titulo ASC"""
            cursor.execute(sql)
            data = cursor.fetchall()
            libros=[]
            for row in data:
                aut=Autor(0, row[4], row[5])
                lib=Libro(row[0], row[1], aut,row[2], row[3])
                libros.append(lib)
            return libros
        except Exception as ex:
            raise Exception(ex)

from datetime import datetime


import datetime

class Compra():
    def __init__(self, uuid, libro, usuario, fecha=None):
        self.uuid = uuid
        self.libro = libro
        self.usuario = usuario
        self.fecha = fecha
        
    def formatted_date(self):
        return datetime.datetime.strftime(self.fecha, '%Y-%m-%d - %H:%M:%S')
from pymysql import *

class UsuarioDB:
    def __init__(self):
        self.conector = connect(
            host="localhost",
            user='root',
            password='',
            db='d_iei'
        )
        self.cursor = self.conector.cursor()
        print("Conexión exitosa a la base de datos")

    def verUusarios(self):
        sql = "SELECT usuario.id, usuario.name, usuario.age FROM usuario ORDER BY usuario.age ASC"
        try:
            self.cursor.execute(sql)
            usuarios = self.cursor.fetchall()
            if len(usuarios) > 0:
                for obj in usuarios:
                    print("ID : " + obj[0])
                    print("Nombre : " + obj[1])
                    print("Edad : " + str(obj[2])+"\n")
            else:
                print("No hay usuarios registrados")


        except Exception as ex:
            print("Error : " + str(ex.args))

    def verUsuario(self, id):
        sql = "SELECT usuario.id, usuario.name, usuario.age FROM usuario WHERE usuario.id = '" +id+"'"
        try:
            self.cursor.execute(sql)
            usuario = self.cursor.fetchone()
            if usuario != None:
                print("ID : " + usuario[0])
                print("Nombre : " + usuario[1])
                print("Edad : " + str(usuario[2])+"\n")
            else:
                print("No hay usuarios registrados")


        except Exception as ex:
            print("Error : " + str(ex.args))

#bd = usuarioDB() - Funciona!
#bd.verUusarios()

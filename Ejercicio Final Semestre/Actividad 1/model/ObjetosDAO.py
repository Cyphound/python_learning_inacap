## Bayron Gómez ##

from pymysql import *

class DataBase:
    def __init__(self):
        self.conector = connect(
            host='localhost',
            user='root',
            password='',
            db='act_pais')
        self.cursor = self.conector.cursor()
        print("Conectado!!")

class BdDao (DataBase):
    def __init__(self):
        super().__init__()

    def verPaises(self):
        sql = "SELECT pais.pais_id, pais.pais_nombre, pais.pais_habitantes, pais.pais_superficie FROM pais"
        try:
            self.cursor.execute(sql)
            resultado = self.cursor.fetchall()
            if len (resultado) == 0:
                print("No hay paises")
            else:
                for obj in resultado:
                    print("    Id               : ",obj[0])
                    print("    Nombre           : ",obj[1])
                    print("    Nº Habitantes    : ",obj[2])
                    print("    Superficie       : ",obj[3])
                    print("")
        except Exception as e:
            print("Error: ",str(e.args))

    def verCiudades(self):
        sql = "SELECT ciudad.ciudad_id, ciudad.ciudad_nombre, ciudad.ciudad_postal, ciudad.pais_id FROM ciudad"
        try:
            self.cursor.execute(sql)
            resultado = self.cursor.fetchall()
            if len (resultado) == 0:
                print("No hay ciudades")
            else:
                for obj in resultado:
                    print("    Id               : ",obj[0])
                    print("    Nombre           : ",obj[1])
                    print("    Codigo Postal    : ",obj[2])
                    print("    Codigo Pais      : ",obj[3])
                    print("")
        except Exception as e:
            print("Error: ",str(e.args))

    def verPais(self, id):
        sql = "SELECT pais.pais_id, pais.pais_nombre, pais.pais_habitantes, pais.pais_superficie FROM pais WHERE pais.pais_id = '"+id+"'"
        try:
            self.cursor.execute(sql)
            resultado = self.cursor.fetchone()
            if resultado != None:
                print("    Id               : ",resultado[0])
                print("    Nombre           : ",resultado[1])
                print("    Nº Habitantes    : ",resultado[2])
                print("    Superficie       : ",resultado[3])
                print("")
            else:
                print("Pais no existente en los registros")
        except Exception as e:
            print("Error: ",str(e.args))

    def verCiudad(self, id):
        sql = "SELECT ciudad.ciudad_id, ciudad.ciudad_nombre, ciudad.ciudad_postal, ciudad.pais_id FROM ciudad WHERE ciudad.ciudad_id = '"+id+"'"
        try:
            self.cursor.execute(sql)
            resultado = self.cursor.fetchone()
            if resultado != None:
                print("    Id               : ",resultado[0])
                print("    Nombre           : ",resultado[1])
                print("    Codigo Postal    : ",resultado[2])
                print("    Codigo Pais      : ",resultado[3])
                print("")
            else:
                print("Ciudad no existente en los registros")
        except Exception as e:
            print("Error: ",str(e.args))

    def agregarPais(self, pais):
        sql = "INSERT INTO pais (pais_id, pais_nombre, pais_habitantes, pais_superficie) VALUES ('"+pais.getId()+"','"+pais.getNombre()+"','"+str(pais.getNHabitantes())+"','"+str(pais.getSuperficie())+"')"
        msg = "Pais agregado"
        try:
            self.cursor.execute(sql)
            self.conector.commit()
        except Exception as e:
            msg = "Error: ",str(e.args)
        
        return msg
    
    def agregarCiudad(self, ciudad):
        sql = "INSERT INTO ciudad (ciudad_id, ciudad_nombre, ciudad_postal, pais_id) VALUES ('"+ciudad.getId()+"','"+ciudad.getNombre()+"','"+str(ciudad.getPostal())+"','"+ciudad.getPais()+"')"
        msg = "Ciudad agregada"
        try:
            self.cursor.execute(sql)
            self.conector.commit()
        except Exception as e:
            msg = "Error: ",str(e.args)
        
        return msg
    
    def actualizarPais(self, id, nombre, habitantes, superficie):
        sqlCheck = "SELECT * FROM pais WHERE pais_id = '"+id+"'"
        self.cursor.execute(sqlCheck)
        resultado = self.cursor.fetchone()

        if resultado == None:
            msg = "Pais no existente en los registros"
        else:
            sql = "UPDATE pais SET pais_nombre = '"+nombre+"', pais_habitantes = '"+str(habitantes)+"', pais_superficie = '"+str(superficie)+"' WHERE pais_id = '"+id+"'"
            msg = "Pais actualizado"
            try:
                self.cursor.execute(sql)
                self.conector.commit()
            except Exception as e:
                msg = "Error: ",str(e.args)

        return msg
    
    def actualizarCiudad(self, id, nombre, postal, pais):
        sqlCheck = "SELECT * FROM ciudad WHERE ciudad_id = '"+id+"'"
        self.cursor.execute(sqlCheck)
        resultado = self.cursor.fetchone()

        if resultado == None:
            msg = "Ciudad no existente en los registros"
        else:
            sql = "UPDATE ciudad SET ciudad_nombre = '"+nombre+"', ciudad_postal = '"+str(postal)+"', pais_id = '"+pais+"' WHERE ciudad_id = '"+id+"'"
            msg = "Ciudad actualizada"
            try:
                self.cursor.execute(sql)
                self.conector.commit()
            except Exception as e:
                msg = "Error: ",str(e.args)

        return msg
    
    def eliminarPais(self, id):
        sqlCheck = "SELECT * FROM pais WHERE pais_id = '"+id+"'"
        self.cursor.execute(sqlCheck)
        resultado = self.cursor.fetchone()

        if resultado == None:
            msg = "Pais no existente en los registros"
        else:
            sql = "DELETE FROM pais WHERE pais_id = '"+id+"'"
            msg = "Pais eliminado"
            try:
                self.cursor.execute(sql)
                self.conector.commit()
            except Exception as e:
                msg = "Error: ",str(e.args)

        return msg
    
    def eliminarCiudad(self, id):
        sqlCheck = "SELECT * FROM ciudad WHERE ciudad_id = '"+id+"'"
        self.cursor.execute(sqlCheck)
        resultado = self.cursor.fetchone()

        if resultado == None:
            msg = "Ciudad no existente en los registros"
        else:
            sql = "DELETE FROM ciudad WHERE ciudad_id = '"+id+"'"
            msg = "Ciudad eliminada"
            try:
                self.cursor.execute(sql)
                self.conector.commit()
            except Exception as e:
                msg = "Error: ",str(e.args)

        return msg
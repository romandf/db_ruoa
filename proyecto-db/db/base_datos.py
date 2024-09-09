from mysql import connector
from os.path import dirname, join
import subprocess
from datetime import datetime
import getpass

#--> Rutas
carpeta_principal = dirname(__file__)
#print(carpeta_principal)
carpeta_respaldo = join(carpeta_principal, "respaldo")
#print(carpeta_respaldo)

#conexion a la base de datos
db_access = {
    "host":"localhost",
    "user":"root",
    "password":"D3l1b3s.Fl0r3s"
    #"auth_plugin":'mysql_native_password'
}

class DataBase:
    #en el init agregaremos todo lo que necesitamos en la clase, tal como la conexion y el cursor y las decoradoras (globales)
    def __init__(self, **kwargs):
        self.connector = connector.connect(**kwargs)
        self.cursor = self.connector.cursor()
        self.password = kwargs["password"]
    
    #Decorador para el reporte de bases de datos en el servidor para evitar la repeticion de funciones o metodos
    def reporte_db(funcion_parametro):
        def fun_interna(self, name_db):
            funcion_parametro(self,name_db)
            print("Estas son las bases de datos que tiene el servidor:")
            DataBase.show_db(self) #se referencia a la clase porque esta dentro de un metodo
        return fun_interna
    
    #metodo para cualesquiera consultas desde la base de datos
    def consult(self, sql):
        result = self.cursor.execute(sql)
        return result
    
    #metodo para mostrar las bases de datos
    def show_db(self):
        self.cursor.execute("SHOW DATABASES")
        for db in self.cursor:
            print(db)

    #metodo para borrar las bases de datos
    @reporte_db #uso de la funcion decoradora
    def drop_db(self, name_db):
        try:
            self.cursor.execute(f"DROP DATABASE {name_db}")
            print(f'La base de datos "{name_db}" se elimino correctamente..')
        except:
            print(f'No existe la base de datos.. "{name_db}"')
    @reporte_db

    #metodo para crear bases de datos
    def create_db(self, name_db):
        try:
            self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {name_db}")
            print(f'Se creo la base de datos"{name_db}" o ya habia sido creada')
        except:
            print(f'Ocurrio un error al intentar crear la base de datos "{name_db}"')

    #Crear Backups de bases de datos
    def copia_db(self, name_db):
        fecha_hora = datetime.now().strftime("%Y-%m-%d %H-%M")
        with open(f"{carpeta_respaldo}/{name_db}_{fecha_hora}.sql","w") as out:
            subprocess.Popen(f'mysqldump --user=root --password={self.password} --databases {name_db}', shell=True, stdout=out)
    
    #Crear Tablas
    def create_table(self, name_db, name_table, columns):
        #String para guardar el string con las columnas y tipos de datos
        columns_string =""
        #Se itera la lista que se le pasa como argumento (cada diccionario)
        for column in columns:
            #formamos el string con el nombre, tipo y longitud
            columns_string += f"{column['name']} {column['type']} ({column['length']})"
            #Si es la clave primaria, auto
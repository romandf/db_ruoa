from mysql import connector
from os.path import dirname, join
import subprocess
from datetime import datetime
#import getpass

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
        self.conector = connector.connect(**kwargs)
        self.cursor = self.conector.cursor()
        self.host = kwargs["host"]
        self.user = kwargs["user"]
        self.password = kwargs["password"]
        self.conexion_cerrada = False
        #avisa de que se abrio la conexion con el servidor
        print("Se abrio la conexion con el servidor.")
    
    #Decorador para el reporte de bases de datos en el servidor para evitar la repeticion de funciones o metodos
    def reporte_db(funcion_parametro):
        def fun_interna(self, name_db):
            funcion_parametro(self,name_db)
            DataBase.show_db(self) #se referencia a la clase porque esta dentro de un metodo
        return fun_interna
    
    #Decorador para el cierre del cursor y la base de datos
    def conexion(funcion_parametro):
        def interno(self, *args, **kwargs):
            try:
                if self.conexion_cerrada:
                    self.conector = connector.connect(
                        host = self.host,
                        user = self.user,
                        password = self.password
                    )
                    self.cursor = self.conector.cursor()
                    self.conexion_cerrada = False
                    print("Se abrio la conexion con el servidor..")
                #se llama a la funcion externa
                funcion_parametro(self, *args, **kwargs)
            except:
                #Se informa de un error en la llamada
                print("Ocurrio un error con la llamada")
            finally:
                if self.conexion_cerrada:
                    pass
                else:
                #cerrar el cursor y la base de datos.
                    self.cursor.close()
                    self.conector.close()
                    print("Se cerro la conexion en el servidor..")
                    self.conexion_cerrada = True
        return interno
    #metodo para cualesquiera consultas desde la base de datos
    @conexion
    def consult(self, sql):
        try:
            self.cursor.execute(sql)
            print("Salida de la instruccion introducida..")
            print(self.cursor.fetchall())
        except:
            print("Ocurrio un error. revisa la instruccion SQL.")
    #metodo para mostrar las bases de datos
    @conexion
    def show_db(self):
        try:
            #Se informa de que se estan obteniendo las bases de datos
            print("\nListado de las bases de datos alojadas en el servidor:\n")
            #Realiza la consulta para mostrar las bases de datos
            self.cursor.execute("SHOW DATABASES")
            result = self.cursor.fetchall()
            for db in result:
                print(f"--{db[0]}")
        except:
            #Si ocurre una excepcion, se avisa en la consola
            print("No se pudieron obtener las bases de datos. COmprueba la conexion con el servidor..")
    #metodo para borrar las bases de datos
    @conexion #Cuando se usan varios decoradores el primero que se llama es el ultimo en ejecutarse
    @reporte_db #uso de la funcion decoradora
    def drop_db(self, name_db):
        try:
            self.cursor.execute(f"DROP DATABASE {name_db}")
            print(f'La base de datos "{name_db}" se elimino correctamente..')
        except:
            print(f'No existe la base de datos.. "{name_db}"')
    @conexion
    @reporte_db
    #metodo para crear bases de datos
    def create_db(self, name_db):
        try:
            self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {name_db}")
            print(f'Se creo la base de datos"{name_db}" o ya habia sido creada')
        except:
            print(f'Ocurrio un error al intentar crear la base de datos "{name_db}"')

    #Crear Backups de bases de datos
    @conexion
    def copia_db(self, name_db):
        #Verifica si la base de datos existe en el servidor
        sql = f"SHOW DATABASES LIKE '{name_db}'"
        self.cursor.execute(sql)
        result = self.cursor.fetchone()

        #Si la base de datos no existe, muestra un mensaje de error y termina el metodo
        if not result:
            print(f"La base de datos {name_db} no existe.")
            return #aparte de regresar valores. termina las funciones
        #obtiene la hora y la fecha actuales
        self.fecha_hora = datetime.now().strftime("%Y-%m-%d %H-%M")

        #Se crea la copia de seguridad
        with open(f"{carpeta_respaldo}/{name_db}_{self.fecha_hora}.sql","w") as out:
            subprocess.Popen(f'mysqldump --user=root --password={self.password} --databases {name_db}', shell=True, stdout=out)
        print("La copia se creo correctamente..")
    
    #Crear Tablas
    @conexion
    def create_table(self, name_db, name_table, columns):
        try:
            columns_string =""
            #Se itera la lista que se le pasa como argumento (cada diccionario)
            for column in columns:
                #formamos el string con el nombre, tipo y longitud
                columns_string += f"{column['name']} {column['type']}({column['length']})"
                #Si es la clave primaria, auto_increment o no adminte valors nulos, lo agrega al string
                if column['primary_key']:
                    columns_string += " PRIMARY KEY"
                if column['auto_increment']:
                    columns_string += " AUTO_INCREMENT"
                if column['not_null']:
                    columns_string += " NOT NULL"
                #Hace un salto de linea despues de cada diccionario
                columns_string += ",\n"
                    
                #elimina al final del string el salto de la linea y la coma
            columns_string = columns_string[:-2]
            self.cursor.execute(f"USE {name_db}")
            #Se crea la tabla juntando la instruccion SQL con el string generado
            sql = f"CREATE TABLE {name_table} ({columns_string});"
            #Se ejecuta la instruccion
            self.cursor.execute(sql)
            #Se hace efectiva
            self.conector.commit()
            print(f"la tabla {name_table} se ha creado correctamente en la base de datos {name_db}")
        except:
            print(f"ocurrio un error al crear la tabla {name_table}")
    
    #Borrar tablas desde la base de datos
    @conexion
    def drop_table(self, name_db,name_table):
        #selecccionamos la base de datos
        self.cursor.execute(f" USE {name_db}")
        #Instruccion sql para  eliminar la tabla si es que existe
        sql = f"DROP TABLE IF EXISTS {name_table}"
        self.cursor.execute(sql)
        #hace efectiva
        self.conector.commit()
        self.conector.close()

    @conexion
    def show_tables(self, name_db):
        try:
            #Primero se verifica si la base de datos existe
            sql = f"SHOW DATABASES LIKE '{name_db}'"
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            #Si la base de datos no existe, muestra un mensaje de error y termina la funcion
            if not result:
                print(f"La base de datso {name_db} no existe.")
                return
            #selecciona la base de datos 
            self.cursor.execute(f"USE {name_db};")
            #Se informa de que se estan obteniendo las tablas
            print(f"Listado de las tablas existentes en la base de datos {name_db}")
            #Realiza la consulta para mostrar las tablas de la base de datos actual
            self.cursor.execute("SHOW TABLES")
            result = self.cursor.fetchall()
            #recorre los resultados y los muestra por pantalla
            for tabla in result:
                print(f"--{tabla[0]} ")
        except:
            print("Ocurrio un error. No existe la tabla en la base de datos")
    @conexion
    def show_columns(self, name_db, name_table):
        #Primero se verifica si la base de datos existe
        sql = f"SHOW DATABASES LIKE '{name_db}'"
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        #Si la base de datos no existe, muestra un mensaje de error y termina la funcion
        if not result:
            print(f"La base de datso {name_db} no existe.")
            return
        
        #Establece la base de datos actual
        self.cursor.execute(f"USE {name_db}")
        try:
            #Realiza la consulta para mostrar las columnas de la tabla
            self.cursor.execute(f"SHOW COLUMNS FROM {name_table}")
            result = self.cursor.fetchall()

            #Se informa de que se estan obteniendo las columnas
            print(f"Listado de las columnas de la tabla {name_table}")
            #Recorre el resultado y lo muestra en pantalla
            for columna in result:
                print(f"--{columna[0]}")
        except:
            print("Ocurrio un error. Compruebe el nombre de la tabla.")
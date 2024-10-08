import db.base_datos as sqldb
import db.tablas as tbl
from db.Data.estaciones import records 
import interfaz.interfaz_grafica as gui

data_base = sqldb.DataBase(**sqldb.db_access)

ventana_login =gui.Login()

#createdb = data_base.create_db("CREATE DATABASE ruoa_stations;")
#data_base.consult("SHOW DATABASESSWDD;")
#data_base.show_db()
#data_base.create_db("ruoa")
#data_base.copia_db("pruebas")
#data_base.create_table("ruoa","stations",tbl.columnas)
#data_base.drop_table("ruoa","stations")
#data_base.drop_db("pruebas2")
#data_base.show_tables("pruebas2")
#data_base.show_tables("ruoa")
#data_base.show_columns("ruoa", "stations")
#for record in records:
#	data_base.insert_record("ruoa","stations",record)
#data_base.delete_record("ruoa","stations","name = 'sine'")
#data_base.delete_all_record("ruoa","stations")
#data_base.update_data("ruoa","stations","responsable = 'Delibes Flores'", "name = 'UNAM'")
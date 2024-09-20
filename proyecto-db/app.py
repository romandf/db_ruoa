import db.base_datos as sqldb
import db.tablas as tbl

data_base = sqldb.DataBase(**sqldb.db_access)

#createdb = data_base.create_db("CREATE DATABASE ruoa_stations;")
#data_base.consult("SHOW DATABASESSWDD;")
#data_base.show_db()
#data_base.create_db("pruebas")
#data_base.copia_db("pruebas")
#data_base.create_table("pruebas","stations",tbl.columnas)
#data_base.drop_table("pruebas","stations")
#data_base.drop_db("pruebas")
#data_base.show_tables("pruebas")
data_base.show_columns("pruebas", "stations")
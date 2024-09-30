import db.base_datos as sqldb
import db.tablas as tbl

data_base = sqldb.DataBase(**sqldb.db_access)
record = [{
    "name" : "UNAM",
    "sitio" : "Universidad Nacional Autonoma de Mexico",
    "direccion" : "Ciudad Universitaria s/n, Coyoacan CDMX",
    "telefono" : "555555555",
    "responsable" : "personal RUOA",
    "latitud" : "19.000 N",
    "longitud" : "180.000 W",
    "altitud" : "2400 msnm"}]

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
data_base.insert_record("ruoa","stations",record)
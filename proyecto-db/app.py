import db.base_datos as sqldb

data_base = sqldb.DataBase(**sqldb.db_access)

#createdb = data_base.create_db("CREATE DATABASE ruoa_stations;")
#consulta_1 = data_base.show_db()
#consulta_1 = data_base.drop_db("pruebas")
#consulta_1 = data_base.create_db("pruebas") 
data_base.copia_db("pruebas")
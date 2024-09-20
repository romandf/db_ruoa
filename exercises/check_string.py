
columnas = [
        {
            "name": "id",
            "type": "INT",
            "length": 10,
            "primary_key": True,
            "auto_increment": True,
            "not_null": True
        },

        {
            "name":"nombre",
            "type":"VARCHAR",
            "length": 32,
            "primary_key": False,
            "auto_increment": False,
            "not_null": True

        },

        {
            "name": "direccion",
            "type": "VARCHAR",
            "length": 128,
            "primary_key": False,
            "auto_increment": False,
            "not_null": True
        },
        
        {
            "name": "responsable",
            "type": "VARCHAR",
            "length": 64,
            "primary_key": False,
            "auto_increment": False,
            "not_null": True
        },
        {
            "name": "meteoro",
            "type": "VARCHAR",
            "length": 64,
            "primary_key": False,
            "auto_increment": False,
            "not_null": True
        },
        {
            "name": "caire",
            "type": "VARCHAR",
            "length": 64,
            "primary_key": False,
            "auto_increment": False,
            "not_null": True
        },
        {
            "name": "carbono",
            "type": "VARCHAR",
            "length": 64,
            "primary_key": False,
            "auto_increment": False,
            "not_null": True
        },
        {
            "name": "gases_ei",
            "type": "VARCHAR",
            "length": 64,
            "primary_key": False,
            "auto_increment": False,
            "not_null": True
        },
        {
            "name": "d_electricas",
            "type": "VARCHAR",
            "length": 64,
            "primary_key": False,
            "auto_increment": False,
            "not_null": True
        }

]
def create_table(columns):
        #String para guardar el string con las columnas y tipos de datos
        columns_string =""
        #Se itera la lista que se le pasa como argumento (cada diccionario)
        for column in columns:
            #formamos el string con el nombre, tipo y longitud
            columns_string += f"{column['name']} {column['type']}({column['length']})"# {column['primary_key']} {column['auto_increment']} {column['not_null']}"
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
        print(columns_string)

def main():
     create_table(columnas)
if __name__ == '__main__':
     main()
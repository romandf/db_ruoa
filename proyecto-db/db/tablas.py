columnas = [
        {
                'name': 'id',
                'type': 'INT',
                'length': 10,
                'primary_key': True,
                'auto_increment': True,
                'not_null': True
        },

        {
                'name':'name',
                'type':'VARCHAR',
                'length': 8,
                'primary_key': False,
                'auto_increment': False,
                'not_null': True
        },

        {
                'name':'sitio',
                'type':'VARCHAR',
                'length': 128,
                'primary_key': False,
                'auto_increment': False,
                'not_null': True
        },

        {
                'name': 'direccion',
                'type': 'VARCHAR',
                'length': 254,
                'primary_key': False,
                'auto_increment': False,
                'not_null': True
        },
        {
                'name': 'responsable',
                'type': 'VARCHAR',
                'length': 64,
                'primary_key': False,
                'auto_increment': False,
                'not_null': True
        },

        {
                'name':'latitud',
                'type':'VARCHAR',
                'length': 32,
                'primary_key': False,
                'auto_increment': False,
                'not_null': True
        },

        {
                'name':'longitud',
                'type':'VARCHAR',
                'length': 32,
                'primary_key': False,
                'auto_increment': False,
                'not_null': True
        },

        {
                'name':'altitud',
                'type':'VARCHAR',
                'length': 32,
                'primary_key': False,
                'auto_increment': False,
                'not_null': True
        }]
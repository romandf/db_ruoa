persons =[
    [{
        "nombre":"Delibes",
        "apellidos":"Flores Roman",
        "edad":57,
        "phone":"123456789"
    }],
    [{
        "nombre":"Erika",
        "apellidos":"Flores Ramirez",
        "edad":3,
        "phone":"123456789"
    }],
    [{
        "nombre":"Frida Sofia",
        "apellidos":"Flores Ramirez",
        "edad":8,
        "phone":"123456789"
    }],
    [{
        "nombre":"Alan Alejandro",
        "apellidos":"Flores Aviles",
        "edad":25,
        "phone":"123456789"
    }],
    [{
        "nombre":"Eduardo",
        "apellidos":"Flores Aviles",
        "edad":23,
        "phone":"123456789"
    }]
]

def persons_info(records):
    data_key = []
    data_value = []
    for record in records:
        data_key.extend(record.keys())
        data_value.extend(record.values())
    key_string = ""
    value_string = ""
    for key in data_key:
        key_string += f"{key}, "
    key_string = key_string[:-2]
    for value in data_value:
        value_string += f"{value}, "
    value_string = value_string[:-2]
    print(key_string)
    print(value_string)

def main():
    for person in persons:
        persons_info(person)

if __name__ == '__main__':
    main()
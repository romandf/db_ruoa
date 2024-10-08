persons =[
    {
        "nombre":"Delibes",
        "apellidos":"Flores Roman",
        "edad":57,
        "phone":"123456789"
    },
    {
        "nombre":"Erika",
        "apellidos":"Flores Ramirez",
        "edad":3,
        "phone":"123456789"
    },
    {
        "nombre":"Frida Sofia",
        "apellidos":"Flores Ramirez",
        "edad":8,
        "phone":"123456789"
    },
    {
        "nombre":"Alan Alejandro",
        "apellidos":"Flores Aviles",
        "edad":25,
        "phone":"123456789"
    },
    {
        "nombre":"Eduardo",
        "apellidos":"Flores Aviles",
        "edad":23,
        "phone":"123456789"
    }
]

def personas_info(**kwargs):
    keys_string =""
    values_string =""
    for key in kwargs.keys():
        keys_string += f"{key}, "
    keys_string = keys_string[:-2]
    for value in kwargs.values():
        values_string += f"{value}, "
    values_string = values_string[:-2]
    print(keys_string)
    print(values_string)

def main():
    for person in persons:    
        personas_info(**person)

if __name__ == '__main__':
    main()
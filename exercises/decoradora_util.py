def decoradora(funcion_parametro):
    def funcion_interna(a,b): #esta funcion interna nos sirve para que no se llame la funcion automaticamente
        #codigo
        print("El resultado de la operacion es: ")
        funcion_parametro(a,b)
        print("Operacion realizada con exito.")
    return funcion_interna

@decoradora
def sumar(a,b):
    print(a + b)

sumar(10,10)
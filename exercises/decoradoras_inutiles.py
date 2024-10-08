def decoradora(funcion_parametro):
    print("El resultado de la operacion es: ")
    funcion_parametro()
    print("Operacion realizada con exito. ")

@decoradora
def sumar():
    print(10 + 10)

@decoradora
def restar():
    print(10 - 20)
@decoradora
def multiplicar():
    print(45 * 2)
@decoradora
def dividir():
    print(4 /10)

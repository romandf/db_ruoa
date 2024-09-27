import math

edades = [2,12,35,47,80,36,78,2,1]

suma = lambda x,y: x+y
# print(suma(3,2))
# print(suma(80,20))

# MenorEdad = list(filter(lambda edad: edad<18,edades))
# MayorEdad = list(filter(lambda edad: edad >=18, edades))

# # print(f"En la lista hay  {len(MenorEdad)} menores de edad {MenorEdad}" )
# # print(f"En la lista hay {len(MayorEdad)}  mayores de edad {MayorEdad}")

# sumar = list(map(lambda edad: edad + 50, edades))
# Cuadrado =  list(map(lambda edad: math.pow(edad,2),edades))
# Cubo = list(map(lambda edad: math.pow(edad,3), edades))

# print(f"Sumar a la lista de edades 50 {sumar}")
# print(f"cuadrado a la lista de edades  {Cuadrado}")
# print(f"Cubo a la lista de edades 50 {Cubo}")

emails = ["delibes@gmail.com",
         "amparo@gmail.com",
         "alan@hotmail.com",
         "dady",
         "elefante.com"
        ]

mailtrue =list(filter(lambda email: "@" in email, emails))
print(f"son emails {mailtrue}")
    
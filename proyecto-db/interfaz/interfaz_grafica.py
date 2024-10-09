from os import path
import customtkinter as ctk
from PIL import Image
from db.base_datos import db_access

ctk.set_appearance_mode("dark") #Modes: system (default), light, dark
ctk.set_default_color_theme("blue") #Themes: blue (default), dark-blue, green

carpeta_principal = path.dirname(__file__)
#Carpeta de imagenes
carpeta_imagenes = path.join(carpeta_principal, "carpeta_imagenes")


class Login:
    def __init__(self):
        #creacion de la ventana principal
        self.root = ctk.CTk() #instancia
        self.root.title("Bases de datos RUOA-ICAyCC-UNAM")#titulo
        #self.root.iconbitmap(os.path.join(carpeta_imagenes,"logo.ico"))#icono
        self.root.geometry("400x500")#tamanio de la ventana
        self.root.resizable(False,False)#Bloqueo de redimension de ventana alto y ancho

        #contenido de la ventana principal
        #logo
        logo = ctk.CTkImage(
            light_image=Image.open((path.join(carpeta_imagenes, "RUOA_logo.png"))), #Imagen modo claro
            dark_image=Image.open((path.join(carpeta_imagenes, "RUOA_logo.png"))), #Imagen modo Obscuro
        )

        #Etiqueta para mostrar la imagen
        etiqueta = ctk.CTkLabel(master=self.root,
                            image=logo,
                            text="")
        etiqueta.pack(pady =15)

        #Campos de texto
        #Usuario
        ctk.CTkLabel(self.root, text="Usuario").pack()
        self.usuario = ctk.CTkEntry(self.root)
        self.usuario.insert(0, "Nombre")
        self.usuario.bind("<Button-1>", lambda e: self.usuario.delete(0, 'end'))
        self.usuario.pack()

        #password
        ctk.CTkLabel(self.root, text="Password").pack()
        self.password = ctk.CTkEntry(self.root)
        self.password.insert(0,"********")
        self.password.bind("<Button-1>", lambda e: self.password.delete(0, 'end'))
        self.password.pack()

        #Boton enviar
        ctk.CTkButton(self.root, text="Entrar", command=self.validar).pack(pady =10)

        #Bucle de ejecucion
        self.root.mainloop()
# Funcion para validar el login
    def validar(self):
        obtener_usuario = self.usuario.get()
        obtener_password = self.password.get()
        ##Una vez terminado el programa cambiar la validacion de obtener usuario == por !=
        if obtener_usuario != db_access["user"] or obtener_password != db_access["password"]:
        #if obtener_usuario == db_access["user"] or obtener_password == db_access["password"]:
            #En caso de tener ya un elemento "info_login" (etiqueta creado) lo borra
            if hasattr(self, "info_login"):
                self.info_login.destroy()
            #Crea esta etiqueta  siempre que el login sea incorrecto
            self.info_login = ctk.CTkLabel(self.root, text="Usuario o password incorrectos.")
            self.info_login.pack()
        else:
            #En caso de tener ya un elemento "info_login" (etiqueta) creado, lo borrara
            if hasattr(self, "info_login"):
                self.info_login.destroy()
                #Crea esta etiqueta siempre que el login sea correcto
                self.info_login = ctk.CTkLabel(self.root, text=f"Hola, {obtener_usuario}. Espere unos instantes..")
                self.info_login.pack()

                #Se destruye la ventana login
                self.root.destroy()
                #para que no termine el programa
                #se instancia la ventana de opciones del programa
                ventana_opciones = VentanaOpciones()
class VentanaOpciones:
    #Lista de texto para los botones
    botones = ['Consulta SQL', 'Mostrar Bases de Datos', 'Eliminar Bases de Datos','Crear Bases de Datos',
               'Crear Respaldos', 'Crear Tablas', 'Elimiar Tablas', 'Mostrar Tablas','Mostrar Columnas',
                'Insertar Registros','Eliminar Registros','Vaciar Tablas','Actualizar Registros']
    def __init__(self):
        self.root =ctk.CTk()
        self.root.title("Opciones para trabajar con bases de datos.")

        #Contador para la posicion de los botones
        contador = 0
        #Elementos por fila
        elementos_fila = 3

        #Crea los botones y establece su texto
        for texto_boton in self.botones:
            button = ctk.CTkButton(
                master=self.root,
                text=texto_boton,
                height=25,
                width=200
            ) 
            button.grid(row=contador//elementos_fila, column=contador%elementos_fila, padx=5, pady=5)

            #incrementa el contador
            contador +=1
        self.root.mainloop()
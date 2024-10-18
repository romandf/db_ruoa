from os import path
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import tkinter  as tk
from PIL import Image
import db.base_datos as sqldb

ctk.set_appearance_mode("dark") #Modes: system (default), light, dark
ctk.set_default_color_theme("blue") #Themes: blue (default), dark-blue, green

carpeta_principal = path.dirname(__file__)
#Carpeta de imagenes
carpeta_imagenes = path.join(carpeta_principal, "carpeta_imagenes")

#Objeto para manejar bases de datos MySQL
base_datos = sqldb.DataBase(**sqldb.db_access)

#Fuentes del programa
fuente_widgets = ('Raleway', 16, tk.font.BOLD)
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
        ctk.CTkLabel(self.root, text="User").pack()
        self.usuario = ctk.CTkEntry(self.root)
        self.usuario.insert(0, "user")
        self.usuario.bind("<Button-1>", lambda e: self.usuario.delete(0,'end'))
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
        #if obtener_usuario != sqldb.db_access["user"] or obtener_password != sqldb.db_access["password"]:
        if obtener_usuario == sqldb.db_access["user"] or obtener_password == sqldb.db_access["password"]:
            #En caso de tener ya un elemento "info_login" (etiqueta creado) lo borra
            if hasattr(self, "info_login"):
                self.info_login.configure("Usuario o password Incorrectos")
            
            else:
                #Crea esta etiqueta  si el login sea incorrecto
                self.info_login = ctk.CTkLabel(self.root, text="Usuario o password incorrectos.")
                self.info_login.pack()
        else:
            #En caso de tener ya un elemento "info_login" (etiqueta) creado, lo borrara
            if hasattr(self, "info_login"):
                self.info_login.configure(text=f"Hola, {obtener_usuario}. Espere unos instantes..")
                #Crea esta etiqueta siempre el login sea correcto
            else:
                self.info_login = ctk.CTkLabel(self.root, text=f"Hola, {obtener_usuario}. Espere unos instantes..")
                self.info_login.pack()
                self.root.destroy()
            #para que no termine el programa
            #se instancia la ventana de opciones del programa
            ventana_opciones = VentanaOpciones()

class FuncionesProgramas:
    def ventana_consultas(self):
        #Crea la ventana
        ventana = ctk.CTkToplevel()
        #Le da un titulo
        ventana.title("Ventana de consultas SQL")
        #Pone el foco en la ventana
        #ventana.grab_set()

        #crea el frame y se agrega a la ventana
        marco = ctk.CTkFrame(ventana)
        marco.pack(padx=10, pady=10)

        #Crea el entry y establece su tamanio a 300px de ancho
        self.entrada = ctk.CTkEntry(marco, width=300)
        #establece un valor personalizado de la fuente
        self.entrada.configure(font=fuente_widgets)
        #Posiciona el elemento en la grid
        self.entrada.grid(row=0, column=0, pady=10)

        #metodo para utilizar la logica del metodo consulat de base_datos.py
        def procesar_datos():
            try:
                #Borra el contenido de la caja de resultados
                self.texto.delete('0.1', 'end')
                #obtiene el contenido de entry
                datos = self.entrada.get()
                #llama al metodo base_datos.consulta() con los datos argumento
                resultado = base_datos.consult(datos)
                for registro in resultado:
                    self.texto.insert('end', registro)
                    self.texto.insert('end', '\n')
        
                #Actualiza el contador de registros devueltos
                numero_registros = len(resultado)
                self.contador_registros.configure(text=f"Registros devueltos: {numero_registros}")
            except Exception:
                self.contador_registros.configure(text=f"Hay un error en tu consulta SQL.Por favor, revisala")
                CTkMessagebox(title="Error", message="Hay un error en tu consulta SQL!. Revisela por favor..", icon="cancel")
        #Crea el boton de envio 
        boton_envio = ctk.CTkButton(marco, text="Enviar", command=lambda: procesar_datos())
        #Posiciona el boton a la derecha del Entry()
        boton_envio.grid(row=0, column=1)

        #Crea el boton de borrado
        boton_borrar = ctk.CTkButton(marco, text="Borrar", command=self.limpiar_texto)
        #Posiciona el boton a la derecha del boton de envio
        boton_borrar.grid(row=0, column=2)

        #Crea el widget de texto
        self.texto = ctk.CTkTextbox(marco, width=610, height=300)
        #Coloca el widget texto debajo del entry y el boton usando grid
        #el columnspan es para que ocupe el grid las colunas 0,1,2
        self.texto.grid(row=1, column=0, columnspan=3, padx=10, pady=10) 

        #Agrega un nuevo widget Label para mostrar el numero de registros devueltos
        self.contador_registros = ctk.CTkLabel(marco,text="Esperando una instruccion.")
        self.contador_registros.grid(row=2, column=0, columnspan=3, padx=10, pady=10)


    def limpiar_texto(self):
        #Borra todo el contenido del widget Text
        self.texto.delete('1.0', 'end') #Borra desde la linea 0, columna 1 hasta el final del widget - texto

    def ventana_mostrar_bases_datos(self):
        # Se crea la ventana
        ventana = ctk.CTkToplevel()
        # Se le da un titulo
        ventana.title("Ventana para mostrar bases de datos  del servidor")
        #Se le da un tamanio
        ventana.geometry("400x565")
        # Se evita una redimension
        ventana.resizable(0,0) #Se puede poner False, False

        #Se crea un marco
        marco = ctk.CTkFrame(ventana)
        marco.pack(padx=10, pady=10)

        #Se crea una etiquete informativa para la ventana
        ctk.CTkLabel(marco, text="Listado de las bases de datos en el servidor",font=fuente_widgets).pack(padx=10, pady=10)

        #Agregar un campo de entrada para la busqueda
        self.busqueda_control = tk.StringVar()

        # Se crea la entrada de texto para busquedas
        ctk.CTkEntry(marco,
                     font=fuente_widgets,
                     textvariable=self.busqueda_control,
                     width=300).pack(padx=10)
        
        self.texto = ctk.CTkTextbox(marco,
                                    font=fuente_widgets,
                                    width=300,
                                    height=300)
        self.texto.pack(padx=10, pady=10)

        #Se crea una etiqueta para mostrar el numero de resultados de la consylta show databases
        self.resultados_label = ctk.CTkLabel(marco,
                                             text="",
                                             font=fuente_widgets)
        self.resultados_label.pack(padx=10, pady=10)
       
        # Funcion interna de actualizacion SHOW DATABASES
        def actualizar():
            # Se establece el valor de la variable de control a string vacio (reset)
            self.busqueda_control.set('')
            # Elimina el contenido de la busqueda de resultados
            self.texto.delete('1.0', 'end')
            # Se realiza la llamada al metodo mostrar_db (SHOW DATABASES) y se guarda en resultado
            resultado = base_datos.show_db()
            #Se itera el resultado y se presenta linea a linea en la caja de texto
            for db in resultado:
                self.texto.insert('end', f"--{db[0]}\n")

            #Actualizar la etiquete con el numero de resultados
            numero_resultados = len(resultado)
            self.resultados_label.configure(text=f"Se encontraron {numero_resultados} resultado/s.")
        
        #Funcion interna de busqueda
        def buscar():
            # Se elimina el contenido de la caja de resultados
            self.texto.delete('1.0', 'end')
            #realiza la llamada al metodo mostrar_db (SHOW DATABASES) y muestra el resultado
            resultado = base_datos.show_db()
            # Se obtiene el valor string de la variable de control (lo que se le agrego en entry())
            busqueda = self.busqueda_control.get().lower()
            # Se crea una lista vacia donde almacenar los resulados filtrados
        
            resultado_filtrado = []
            # Se itera la tupla fetchall.
            for db in resultado:
                #Si lo que tiene la StringVar esta en cada lista de la tupla
                if busqueda in db[0]:
                    resultado_filtrado.append(db)
            # Se itera la lista ya filtrada, con lo que se insertan en caja de resultados
            for db in resultado_filtrado:
                self.texto.insert('end', f"-{db[0]}\n")
            
            # Se actualiza la etiqueta con el nuumero de resultados
            numero_resultados = len(resultado_filtrado)
            self.resultados_label.configure(text=f"Se encontraron {numero_resultados} resultado/s.")

            #Se crea un boton para buscar bases de datos
        boton_buscar = ctk.CTkButton(marco,
                                    text="Buscar",
                                    command=buscar)
        boton_buscar.pack(pady=10)

        #Se crea un boton para actualizar los resultados de la caja de texto
        boton_actualizar = ctk.CTkButton(marco,
                                        text="Actualizar",
                                        command=actualizar)
        boton_actualizar.pack(pady=10)

        actualizar()

    def ventana_eliminar_bases_datos(self):
        ventana = ctk.CTkToplevel()
        ventana.title("Ventana de eliminar bases de datos")
    

    def ventana_crear_bases_datos(self):
        ventana = ctk.CTkToplevel()
        ventana.title("Ventana de crear bases de datos")

    def ventana_crear_respaldos(self):
        ventana = ctk.CTkToplevel()
        ventana.title("Ventana de crear respaldos")

    def ventana_crear_tablas(self):
        ventana = ctk.CTkToplevel()
        ventana.title("Ventana de crear tablas")

    def ventana_eliminar_tablas(self):
        ventana = ctk.CTkToplevel()
        ventana.title("Ventana de elimiar tablas")

    def ventana_mostrar_tablas(self):
        ventana = ctk.CTkToplevel()
        ventana.title("Ventana de mostrar tablas")

    def ventana_mostrar_columnas(self):
        ventana = ctk.CTkToplevel()
        ventana.title("Ventana de mostrar columnas")

    def ventana_insertar_registros(self):
        ventana = ctk.CTkToplevel()
        ventana.title("Ventana de insertar registros")

    def ventana_eliminar_registros(self):
        ventana = ctk.CTkToplevel()
        ventana.title("Ventana de eliminar registros")

    def ventana_vaciar_tablas(self):
        ventana = ctk.CTkToplevel()
        ventana.title("Ventana de vaciar tablas")

    def ventana_actualizar_tablas(self):
        ventana = ctk.CTkToplevel()
        ventana.title("Ventana de actualizar tablas")

objeto_funciones = FuncionesProgramas()
class VentanaOpciones:
    #Lista de texto para los botones
    botones = {'Consulta SQL': objeto_funciones.ventana_consultas,
                'Mostrar Bases de Datos': objeto_funciones.ventana_mostrar_bases_datos,
                'Eliminar Bases de Datos': objeto_funciones.ventana_eliminar_bases_datos,
                'Crear Bases de Datos': objeto_funciones.ventana_crear_bases_datos,
                'Crear Respaldos': objeto_funciones.ventana_crear_respaldos,
                'Crear Tablas': objeto_funciones.ventana_crear_tablas,
                'Elimiar Tablas': objeto_funciones.ventana_eliminar_tablas,
                'Mostrar Tablas': objeto_funciones.ventana_mostrar_tablas,
                'Mostrar Columnas': objeto_funciones.ventana_mostrar_columnas,
                'Insertar Registros': objeto_funciones.ventana_insertar_registros,
                'Eliminar Registros': objeto_funciones.ventana_eliminar_registros,
                'Vaciar Tablas': objeto_funciones.ventana_vaciar_tablas,
                'Actualizar Registros': objeto_funciones.ventana_actualizar_tablas
                }
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
                width=200,
                command=self.botones[texto_boton]
            ) 
            button.grid(row=contador//elementos_fila, column=contador%elementos_fila, padx=5, pady=5)

            #incrementa el contador
            contador +=1
        self.root.mainloop()
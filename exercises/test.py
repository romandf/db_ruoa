import customtkinter as ctk

ctk.set_appearance_mode("dark") #Modes: system (default), light, dark
ctk.set_default_color_theme("blue") #Themes: blue (default), dark-blue, green
#ventana principal
principal = ctk.CTk()
principal.title("Primera ventana")
principal.geometry("300x100")

#segunda ventana
ventana2 = ctk.CTkToplevel()
ventana2.title("Segunda ventana")
ventana2.geometry("300x100")
#tercera ventana
ventana2 = ctk.CTkToplevel()
ventana2.title("tercera ventana")
ventana2.geometry("300x100")
#cuarta ventana
ventana2 = ctk.CTkToplevel()
ventana2.title("Cuarta ventana")
ventana2.geometry("300x100")

principal.mainloop()
import sqlite3 
from tkinter import *
from tkinter import ttk, messagebox
from container import Container
import tkinter as tk
from PIL import Image, ImageTk 


class Login(tk.Frame):
    db_name = "database.db"
    
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.pack()
        self.place(x=0, y=0 , width=1100 , height=650)
        self.controlador = controlador
        self.widgets()

    def validacion(self, user , pas):
        return len(user) > 0 and len(pas) > 0
    
    def login(self):
        user = self.username.get()
        pas = self.password.get()

        if self.validacion(user, pas):
            consulta = "SELECT * FROM usuarios WHERE username=? AND password = ?"
            parametros = (user, pas)

            try:
                with sqlite3.connect(self.db_name) as conn:
                    cursor = conn.cursor()
                    cursor.execute(consulta, parametros)
                    result = cursor.fetchall()
                    print("Resultado del login:", result)


                    if result:
                        self.control1()
                    else:
                        self.username.delete(0,'end')
                        self.password.delete(0,'end')
                        messagebox.showerror(title="Error", message="Usuario y/o contraseña incorrecta")
            except sqlite3.Error as e:
                messagebox.showerror(title="Error", message="no se conecto a la base de datos: {}".format(e))

        else:
            messagebox.showerror(title="Error", message="Llene todas las casillas")

    def control1(self):
        self.controlador.show_frame(Container)

    def control2(self):
        self.controlador.show_frame(Registro)



    def widgets(self):
        fondo = tk.Frame(self, bg="#C6D9E3")
        fondo.pack()
        fondo.place(x=0, y=0, width=1100, height=650)


        self.bg_image = Image.open("imagenes\supermarke.jpg")
        self.bg_image = self.bg_image.resize((1100, 650))
        self.bg_image = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = ttk.Label(fondo, image=self.bg_image)
        self.bg_label.place(x=0 , y=0 , width=1100, height=650)

        frame1 = tk.Frame(self, bg="#FFFFFF", highlightbackground="black",highlightthickness=1)
        frame1.place(x=350,y=10,width=400,height=630)

        user = ttk.Label(frame1, text="Nombre de usuario", font="arial 16 bold", background="#FFFFFF")
        user.place(x=100,y=250)
        self.username = ttk.Entry(frame1, font="arial 16 bold")
        self.username.place(x=80, y=290, width=240, height=40)

        pas = ttk.Label(frame1, text="Contraseña", font="arial 16 bold", background="#FFFFFF")
        pas.place(x=100,y=340)
        self.password = ttk.Entry(frame1, show="*", font="arial 16 bold")
        self.password.place(x=80,y=380, width=240, height=40)
    
        btn1 = tk.Button(frame1, text="Iniciar", font="arial 16 bold", command=self.login)
        btn1.place(x=80, y=440 , width=240, height=40)
        
        btn2 = tk.Button(frame1, text="Registrar", font="arial 16 bold", command=self.control2)
        btn2.place(x=80, y=500 , width=240, height=40)
      

class Registro(tk.Frame):

    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.pack()
        self.place(x=0, y=0 , width=1100 , height=650)
        self.controlador = controlador
        self.widgets()


    def widgets(self):
        fondo = tk.Frame(self, bg="#C6D9E3")
        fondo.pack()
        fondo.place(x=0, y=0, width=1100, height=650)


        self.bg_image = Image.open("imagenes\supermarke.jpg")
        self.bg_image = self.bg_image.resize((1100, 650))
        self.bg_image = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = ttk.Label(fondo, image=self.bg_image)
        self.bg_label.place(x=0 , y=0 , width=1100, height=650)

        frame1 = tk.Frame(self, bg="#FFFFFF", highlightbackground="black",highlightthickness=1)
        frame1.place(x=350,y=10,width=400,height=630)

        user = ttk.Label(frame1, text="Nombre de usuario", font="arial 16 bold", background="#FFFFFF")
        user.place(x=100,y=250)
        self.username = ttk.Entry(frame1, font="arial 16 bold")
        self.username.place(x=80, y=290, width=240, height=40)

        pas = ttk.Label(frame1, text="Contraseña", font="arial 16 bold", background="#FFFFFF")
        pas.place(x=100,y=340)
        self.password = ttk.Entry(frame1, show="*", font="arial 16 bold")
        self.password.place(x=80,y=380, width=240, height=40)
        
        key = ttk.Label(frame1, text="Codigo de registro", font="arial 16 bold", background="#FFFFFF")
        key.place(x=100, y=430)
        self.key = ttk.Entry(frame1, show="*", font="arial 16 bold")
        self.key.place(x=80,y=470, width=240, height=40)

        btn3 = tk.Button(frame1, text="Registrarse", font="arial 16 bold")
        btn3.place(x=80, y=520 , width=240, height=40)
        
        btn4 = tk.Button(frame1, text="Regresar", font="arial 16 bold")
        btn4.place(x=80, y=570 , width=240, height=40)
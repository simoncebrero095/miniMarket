from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk

import sys
import os

class Inventario(tk.Frame):
    def __init__(self, padre):
        super().__init__(padre)
        self.widgets()

        self.image_folder = "fotos"
        if not os.path.exists(self.image_folder):
            os.makedirs(self.image_folder)



    def widgets(self):
        #================================================================================================
        canvas_articulos = tk.LabelFrame(self, text="Articulos", font="ariald 14 bold", bg="#C6D9E3")
        canvas_articulos.place(x=300, y=10, width=780, height=580)


        self.canvas = tk.Canvas(canvas_articulos, bg="#C6D9E3")
        self.scrollbar = tk.Scrollbar(canvas_articulos, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="#C6D9E3")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0,0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
    #======================================================================================================
        lblframe_buscar = LabelFrame(self, text="Buscar", font="arial 14 bold", bg="#C6D9E3")
        lblframe_buscar.place(x=10, y=10, width=280, height=80)

        self.comboboxbuscar = ttk.Combobox(lblframe_buscar,font="arial 12")
        self.comboboxbuscar.place(x=5, y=5, width=260, height=40)

    #===================== =================================================================================
        lblframe_seleccion = LabelFrame(self, text="Selección", font="arial 14 bold", bg="#C6D9E3")
        lblframe_seleccion.place(x=10,y=95,width=280, height=190)

        self.label1 = tk.Label(lblframe_seleccion, text="Articulo: ", font="Arial 14 bold", bg="#C6D9E3", wraplength=300)
        self.label1.place(x=5,y=5)

        self.label2 = tk.Label(lblframe_seleccion, text="Precio: ", font="Arial 14 bold", bg="#C6D9E3")
        self.label2.place(x=5,y=40)

        self.label3 = tk.Label(lblframe_seleccion, text="Costo: ", font="Arial 14 bold", bg="#C6D9E3")
        self.label3.place(x=5,y=70)

        self.label4 = tk.Label(lblframe_seleccion, text="Stock: ", font="Arial 14 bold", bg="#C6D9E3")
        self.label4.place(x=5,y=100)

        self.label5 = tk.Label(lblframe_seleccion, text="Estado: ", font="Arial 14 bold", bg="#C6D9E3")
        self.label5.place(x=5,y=130)
    #===================== =================================================================================
        lblframe_botones = LabelFrame(self, bg="#C6D9E3", text="Opciones", font="arial 14 bold")
        lblframe_botones.place(x=10, y=290, width=280, height=300)

        btn1 = tk.Button(lblframe_botones, text="Agregar", font="Arial 14 bold",command=self.agregar_articulo)
        btn1.place(x=20, y=20, width=180, height=40)

        
        btn2 = tk.Button(lblframe_botones, text="Editar", font="Arial 14 bold")
        btn2.place(x=20, y=80, width=180, height=40)


    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            image = Image.open(file_path)
            image = image.resize((200, 200)), Image.LANCZOS
            image_name = os.path.basename(file_path)
            image_save_path = os.path.join(self.imagen_folder,image_name)
            image.save(image_save_path)


            self.image_tk = ImageTk.PhotoImage(image)

            self.product_image = self.image_tk
            self.image_path = image_save_path

            img_label = tk.Label(self.frameimg,image = self.image_tk)
            img_label.place(x=0, y=0, width=200, height=200)
    
    def agregar_articulo(self):
        top = tk.Toplevel(self)
        top.title("Agregar Articulo")
        top.geometry("700x400+200+50")
        top.config(bg="#C6D9E3")
        top.resizable(False,False)

        top.transient(self.master)
        top.grab_set()
        top.focus_set()
        top.lift()

        tk.Label(top, text="Articulos", font="arial 12 bold", bg="#C6D9E3").place(x=20, y=80, height=25)
        


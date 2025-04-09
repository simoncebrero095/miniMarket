from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox, filedialog


class Inventario(tk.Frame):
    def __init__(self, padre):
        super().__init__(padre)
        self.widgets()


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

    #======================================================================================================




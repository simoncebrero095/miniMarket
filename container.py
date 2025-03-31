from tkinter import *
import tkinter as tk
import sys
import os

class Container(tk.Frame):
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.controlador = controlador
        self.pack()
        self.place(x=0, y=0, width=1100, height=650)
        self.widgets()
        self.frames = {}
        self.buttons = []
        for i in (Ventas, Inventario, Clientes, Pedidos, Proveedor, Informacion):
            frame = i(self)
            self.frames[i] = frame
            frame.pack()
            frame.config(bg="#C6D9E3",highlightbackground= "gray", highlightthickness=1)
            frame.placer(x=0, y=40, width= 1100, height= 610)
        self.show_frames


    



    def widgets(self):
        pass
    




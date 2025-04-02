from tkinter import *
import tkinter as tk
from ventas import Ventas
from inventario import Inventario
from clientes import Clientes
from pedidos import Pedidos
from proveedor import Proveedor
from informacion import Informacion 
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
            frame.place(x=0, y=40, width= 1100, height= 610)
        self.show_frames(Ventas)


    def show_frames(self, container):
        frame = self.frames[container]
        frame.tkraise()

    def ventas(self):
        self.show_frames(Ventas)
    
    def inventario(self):
        self.show_frames(Inventario)
    
    def clientes(self):
        self.show_frames(Clientes)
    
    def pedidos(self):
        self.show_frames(Pedidos) 
    
    def proveedor(self):
        self.show_frames(Proveedor)

    def informacion(self):
        self.show_frames(Informacion)
    
    def widgets(self):
        frame2 = tk.Frame(self)
        frame2.place(x=0, y=0, width=1100, height=40)

        self.bnt_ventas = Button(frame2, fg="black", text="Venta", font="sans 16 bold",command=self.ventas)
        self.bnt_ventas.place(x=0,y=0, width=184, height=40)

        self.bnt_inventario = Button(frame2, fg="black", text="Inventario", font="sans 16 bold",command=self.inventario)
        self.bnt_inventario.place(x=184,y=0, width=184, height=40)
        
        self.bnt_clientes = Button(frame2, fg="black", text="Clientes", font="sans 16 bold",command=self.clientes)
        self.bnt_clientes.place(x=369,y=0, width=184, height=40)

        self.bnt_pedidos = Button(frame2, fg="black", text="Pedidos", font="sans 16 bold",command=self.pedidos)
        self.bnt_pedidos.place(x=554,y=0, width=184, height=40)

        self.bnt_proveedor = Button(frame2, fg="black", text="Proveedor", font="sans 16 bold",command=self.proveedor)
        self.bnt_proveedor.place(x=739,y=0, width=184, height=40)

        self.bnt_informacion = Button(frame2, fg="black", text="Informacion", font="sans 16 bold",command=self.informacion)
        self.bnt_informacion.place(x=923,y=0, width=184, height=40)

        self.buttons = [self.bnt_ventas,self.bnt_inventario,self.bnt_clientes,self.bnt_pedidos,self.bnt_proveedor,self.bnt_informacion]
    




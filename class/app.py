from laptapGaming import laptopGaming
from laptapBusiness import laptapBusiness
import tkinter as tk 
from tkinter import ttk
from PIL import Image,ImageTk
import random 

class App:
    def __init__(self,root):
        self.root=root
        self.laptops=[]
        self.laptopsbiniues=[]
        self.imagenes=["C:\\Users\\USER\\OneDrive\\Documentos\\Modulo4\\Python\\class\\imagenes\\lp1.jpeg","C:\\Users\\USER\\OneDrive\\Documentos\\Modulo4\\Python\\class\\imagenes\\lp2.jpg","C:\\Users\\USER\\OneDrive\\Documentos\\Modulo4\\Python\\class\\imagenes\\lp3.png","C:\\Users\\USER\\OneDrive\\Documentos\\Modulo4\\Python\\class\\imagenes\\lp4.jpeg","C:\\Users\\USER\\OneDrive\\Documentos\\Modulo4\\Python\\class\\imagenes\\lp5.jpeg"]

        root.title("ingresar datos")

        self.setapUi()

    def setapUi(self):
        ttk.Label(self.root, text="Marca").grid(row=0,column=0)
        self.marca=tk.StringVar()
        ttk.Entry(self.root,textvariable=self.marca).grid(row=0,column=1)

        ttk.Label(self.root, text="Procesador").grid(row=1,column=0)
        self.procesador=tk.StringVar()
        ttk.Entry(self.root,textvariable=self.procesador).grid(row=1,column=1)

        ttk.Label(self.root, text="Memoria").grid(row=2,column=0)
        self.memoria=tk.StringVar()
        ttk.Entry(self.root,textvariable=self.memoria).grid(row=2,column=1)

        ttk.Label(self.root, text="Tarjeta grafica").grid(row=3,column=0)
        self.tarjetaGrafica=tk.StringVar()
        ttk.Entry(self.root,textvariable=self.tarjetaGrafica).grid(row=3,column=1)
        
        ttk.Label(self.root, text="Precio").grid(row=4,column=0)
        self.precio=tk.StringVar()
        ttk.Entry(self.root,textvariable=self.precio).grid(row=4,column=1)

        ttk.Button(self.root,text="Agregar Laptop",command=self.agregarLaptop).grid(row=5,column=0)

        self.mostrarLaptos=tk.Text(self.root,height=10,width=50)
        self.mostrarLaptos.grid(row=6,column=0,columnspan=2)

        self.canva=tk.Canvas(self.root,width=200,height=200)
        self.canva.grid(row=1,column=3,rowspan=6)



        ttk.Label(self.root, text="Marca").grid(row=12,column=0)
        self.marcab=tk.StringVar()
        ttk.Entry(self.root,textvariable=self.marcab).grid(row=12,column=1)

        ttk.Label(self.root, text="Procesador").grid(row=13,column=0)
        self.procesadorb=tk.StringVar()
        ttk.Entry(self.root,textvariable=self.procesadorb).grid(row=13,column=1)

        ttk.Label(self.root, text="Memoria").grid(row=14,column=0)
        self.memoriab=tk.StringVar()
        ttk.Entry(self.root,textvariable=self.memoriab).grid(row=14,column=1)

        ttk.Label(self.root, text="Espacio").grid(row=15,column=0)
        self.espacio=tk.StringVar()
        ttk.Entry(self.root,textvariable=self.espacio).grid(row=15,column=1)

        ttk.Label(self.root, text="duracion bateria").grid(row=16,column=0)
        self.duracionBateria=tk.StringVar()
        ttk.Entry(self.root,textvariable=self.duracionBateria).grid(row=16,column=1)
        
        ttk.Label(self.root, text="Precio").grid(row=17,column=0)
        self.preciob=tk.StringVar()
        ttk.Entry(self.root,textvariable=self.preciob).grid(row=17,column=1)

        ttk.Button(self.root,text="Agregar Laptop",command=self.laptopBusinnes).grid(row=18,column=0)

        self.mostrarLaptosB=tk.Text(self.root,height=10,width=50)
        self.mostrarLaptosB.grid(row=19,column=0,columnspan=2)

        self.canva1=tk.Canvas(self.root,width=200,height=200)
        self.canva1.grid(row=19,column=3,rowspan=6)

    def agregarLaptop(self):
        nuevaLaptop=laptopGaming(self.marca.get(),self.procesador.get(),self.memoria.get(),self.tarjetaGrafica.get(),self.precio.get())    
        self.laptops.append(nuevaLaptop)
        
        self.mostrarLaptos.insert(tk.END, f"{nuevaLaptop}")

        self.mostrarImagenAleatoria()

    def laptopBusinnes(self):
        nuevaLaptop=laptapBusiness(self.marcab.get(),self.procesadorb.get(),self.memoriab.get(),self.espacio.get(),self.duracionBateria.get(),self.preciob.get())    
        self.laptopsbiniues.append(nuevaLaptop)
        
        self.mostrarLaptosB.insert(tk.END, f"{nuevaLaptop}")

        self.mostrarImagenAleatoriab()

    def mostrarImagenAleatoria(self):
        ImagenPaht=random.choice(self.imagenes)
        Imagen=Image.open(ImagenPaht)
        Imagen=Imagen.resize((200,200),Image.Resampling.LANCZOS)
        photo=ImageTk.PhotoImage(Imagen)

        self.canva.create_image(0,0,anchor=tk.NW,image=photo)
        self.canva.image=photo

    def mostrarImagenAleatoriab(self):
        ImagenPaht=random.choice(self.imagenes)
        Imagen=Image.open(ImagenPaht)
        Imagen=Imagen.resize((200,200),Image.Resampling.LANCZOS)
        photo=ImageTk.PhotoImage(Imagen)

        self.canva1.create_image(0,0,anchor=tk.NW,image=photo)
        self.canva1.image=photo

        pass

root =tk.Tk()

app=App(root)
root.mainloop()
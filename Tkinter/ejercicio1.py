import tkinter as tk
from tkinter import messagebox

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplicación Básica con Tkinter")
        self.geometry("600x400")
    
    #OTROS WIDGETS
        Frame1 = tk.Frame(self)
        tk.Label(Frame1, text = "Nombre:").grid(row=0,column=0,pady=5)
        self.entry1 = tk.Entry(Frame1)
        self.entry1.grid(row=0,column=1,pady=5)
        Frame1.pack(pady=10)
        
        Frame2 = tk.Frame(self)
        tk.Label(Frame2, text = "Telefono:").grid(row=0,column=0,pady=5)
        self.entry2 = tk.Entry(Frame2)
        self.entry2.grid(row=0,column=1,pady=5)
        Frame2.pack(pady=10)
        
        #BOTONES
        Frame3 = tk.Frame(self)
        tk.Button(Frame3, text="Guardar", command=self.guardar_datos).grid(row=0, column=0,padx=10,pady=5)
        tk.Button(Frame3, text="Eliminar", command=self.eliminar_datos).grid(row=0, column=1,pady=5)
        
        Frame3.pack(pady=10)
        
        self.lista = tk.Listbox(self, width=50,height=10)
        self.lista.pack(pady=10)
    
    def eliminar_datos(self):
        seleccion = self.lista.curselection()
        if seleccion:
            self.lista.delete(seleccion)
            messagebox.showinfo("Info", "Elemento eliminado correctamente")
        else:
            messagebox.showwarning("Advertencia", "Por favor seleccione un elemento para eliminar")
        
    def guardar_datos(self):
        nombre = self.entry1.get()
        telefono = self.entry2.get()
        # validaciones
        if nombre and telefono:
            self.lista.insert(tk.END, f'Nombre: {nombre}, Telefono: {telefono}')
            messagebox.showinfo("Datos", "Datos guardados correctamente.")
            #Limpiar los campos despues de guardar
            self.entry1.delete(0,tk.END)
            self.entry2.delete(0,tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, complete ambos campos.")
obj = Aplicacion()
obj.mainloop()
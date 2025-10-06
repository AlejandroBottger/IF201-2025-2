import tkinter as tk
from tkinter import messagebox

class Ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ventana Prueba")
        self.geometry("600x600")
        self.configure(background="Light gray")
        
        self.boton_presionado = False # Booleano para cambiar label 1
        
        #frames: bg es: background para cambiar el color del fondo
        
        frame1 = tk.Frame(self, bg="light gray")
        frame1.pack(pady=50)
        frame2 = tk.Frame(self, bg="light gray")
        frame2.pack(pady=100)
        
        #labels: fg es: foreground para cambiar de color al contenido
        
        self.label1 = tk.Label(frame1, text="Hola Mundo", font="Arial, 20" ,fg="Red")
        self.label1.grid(row=0, column=0,pady= 50)
        
        self.label2 = tk.Label(frame2, text="Ingresa tu nombre", font="12", bg = "light gray")
        self.label2.grid(row=0,column=0,pady=2)
        
        #entrys:
        self.entry1 = tk.Entry(frame2) 
        self.entry1.grid(row=0, column=1, padx=5, pady=0)
        
        #botones:
        self.btn1 = tk.Button(frame1, text="Boton")
        self.btn1.grid(row=1, column=0, pady=0)
        
        self.btn2 = tk.Button(frame2, text="Saludar", command=self.saludar)
        self.btn2.grid(row=1,column=0,pady=5)
        
        self.btn1.bind("<Button-1>",self.presionar_boton) #otra manera de ejecutar eventos en botones al presionar
        self.bind("<ButtonRelease-1>", self.soltar_boton) #evento (al soltar)

    #metodos:

    def presionar_boton(self, event): #necesita ir event porque se usa el .bind
        self.boton_presionado = True
        self.label1.config(text="Boton presionado")# messagebox.showinfo("Boton", "Boton presionado")
        
        
    def soltar_boton(self, event):
        if self.boton_presionado:
            self.label1.config(text="Hola Mundo")
            self.boton_presionado = False
    
    def saludar(self):
        nombre = self.entry1.get()
        if nombre and nombre.isalpha(): #isaplha() es para verificar que el texto de entrada sea solo letras
            messagebox.showinfo("Saludo", f'Hola {nombre}')
        else:
            messagebox.showerror("Error", "Por favor elige un nombre")
    
if __name__ == "__main__":    
    Obj = Ventana()
    Obj.mainloop()
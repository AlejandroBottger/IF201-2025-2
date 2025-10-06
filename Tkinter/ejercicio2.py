import tkinter as tk
from tkinter import messagebox

class Operacion:
    def sumar(self, a, b):
        return a + b
    
    def restar(self, a, b):
        return a - b

class Ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Herencia Multiple y operaciones")
        self.geometry("300x200")
        

class Aplicacion(Ventana,Operacion):
    def __init__(self):
        super().__init__()
        Operacion.__init__(self)
    
    #OTROS WIDGETS
        tk.Label(self, text = "Numero 1").pack(pady=5)
        self.entry1 = tk.Entry(self)
        self.entry1.pack(pady=5)
        
        tk.Label(self, text = "Numero 2").pack(pady=5)
        self.entry2 = tk.Entry(self)
        self.entry2.pack(pady=5)
        
        frame = tk.Frame(self)
        tk.Button(frame, text = "Sumar", command=self.relizar_suma).grid(row=0, column=0,padx=10, pady=5)
        tk.Button(frame, text = "Restar", command=self.relizar_resta).grid(row=0,column=1, pady=5)
        frame.pack(pady=10)
        
    def relizar_suma(self):
        try:
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())
            resultado = self.sumar(num1,num2)
            messagebox.showinfo("Resultado", f'La suma es: {resultado}')
        except ValueError:
            messagebox.showerror("Valores incorrectos")
    def relizar_resta(self):
        try:
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())
            resultado = self.restar(num1,num2)
            messagebox.showinfo("Resultado", f'La suma es: {resultado}')
        except ValueError:
            messagebox.showerror("Valores incorrectos")

if __name__ == "__main__":            
    obj = Aplicacion()
    obj.mainloop()
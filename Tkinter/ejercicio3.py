import tkinter as tk
from tkinter import messagebox

contador = 0

class AgendaPersonal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Agenda Personal")
        self.geometry("600x400")
        self.configure(background= "Light blue")
        #Labels:
        
        frame1 = tk.Frame(self)
        tk.Label(frame1, text= "Nombre:", font="Arial, 12", background="gray").grid(row=0,column=0,pady=5)
        self.entry1 = tk.Entry(frame1)
        self.entry1.grid(row=0,column=1,pady=5)
        frame1.pack(pady=5)
        
        frame2 = tk.Frame(self)
        tk.Label(frame2, text= "Telefono:").grid(row=0,column=0,pady=5)
        self.entry2 = tk.Entry(frame2)
        self.entry2.grid(row=0,column=1,pady=5)
        frame2.pack(pady=5)
        
        #Buttons:
        
        frame3 = tk.Frame(self)
        tk.Button(frame3, text="Guardar", background="Blue", command=self.savedata).grid(row=0,column=0,pady=5)
        tk.Button(frame3, text="Salir", command=self.quit).grid(row=0,column=2,padx=5,pady=5)
        tk.Button(frame3, text="Eliminar Seleccionado", font="Sans, 16", command=self.deseleccion).grid(row=0,column=1,pady=5)
        frame3.pack(pady=5)
        
        self.lista = tk.Listbox(self,width=50,height=5)
        self.lista.pack(pady=5)
    
    def savedata(self):
        global contador
        nombre = self.entry1.get()
        fono = self.entry2.get()
        contador = contador + 1
        if nombre and fono:
            self.lista.insert(tk.END, f'{contador}. {nombre} {fono}')   
            self.entry1.delete(0,tk.END)
            self.entry2.delete(0,tk.END)
        else:
            messagebox.showwarning("Advertencia", "Debe completar los datos")
            
    def deseleccion(self):
        selected = self.lista.curselection()
        if selected:
            self.lista.delete(selected)
        else:
            messagebox.showwarning("Advertencia", "Debe seleccionar el elemento para eliminar")
            
if __name__ == "__main__":        
    Obj = AgendaPersonal()
    Obj.mainloop()        
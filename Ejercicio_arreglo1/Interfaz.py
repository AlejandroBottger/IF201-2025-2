import tkinter as tk
from tkinter import ttk, messagebox
from ArchivosPacientes import Archivo

class Ventana:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Pacientes")
        self.root.geometry("900x500")

        self.archivo = Archivo("pacientes.txt")
        self.archivo.abrir()
        self.pacientes = self.archivo.mostrar()

        especialidades = sorted(set(p.especialidad for p in self.pacientes))
        self.comb = ttk.Combobox(root, values=especialidades, state="readonly")
        self.comb.pack(pady=5)
        self.comb.bind("<<ComboboxSelected>>", self.filtrar)

        columnas = ("ID", "Nombre", "Edad", "Diagnóstico", "Especialidad", "Costo", "Iniciales")
        self.tree = ttk.Treeview(root, columns=columnas, show="headings", height=10)
        for c in columnas:
            self.tree.heading(c, text=c)
            self.tree.column(c, width=120)
        self.tree.pack(pady=10, fill="x")

        self.cargar_datos(self.pacientes)

        self.lbl_max = tk.Label(root, text="")
        self.lbl_min = tk.Label(root, text="")
        self.lbl_max.pack()
        self.lbl_min.pack()

        ttk.Button(root, text="Mostrar Promedios", command=self.mostrar_promedios).pack(pady=5)
        ttk.Button(root, text="Exportar Filtrados", command=self.exportar_filtrados).pack(pady=5)

        self.actualizar_info()

    def cargar_datos(self, lista):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for p in lista:
            self.tree.insert("", tk.END, values=(p.id, p.nombre, p.edad, p.diagnostico, p.especialidad, p.costo, p.iniciales()))

    def filtrar(self, event=None):
        esp = self.comb.get()
        filtrados = [p for p in self.pacientes if p.especialidad == esp]
        self.cargar_datos(filtrados)

    def mostrar_promedios(self):
        dicc = self.archivo.promedio_por_especialidad(self.pacientes)
        texto = "\n".join([f"{esp}: {prom:.2f}" for esp, prom in dicc.items()])
        messagebox.showinfo("Promedios por Especialidad", texto)

    def exportar_filtrados(self):
        esp = self.comb.get()
        if not esp:
            messagebox.showwarning("Atención", "Seleccione una especialidad primero.")
            return
        filtrados = [p for p in self.pacientes if p.especialidad == esp]
        with open("pacientes_filtrados.txt", "w", encoding="utf-8") as f:
            for p in filtrados:
                f.write(f"{p.id};{p.nombre};{p.edad};{p.diagnostico};{p.especialidad};{p.costo}\n")
        messagebox.showinfo("Exportado", f"Archivo exportado con {len(filtrados)} pacientes.")

    def actualizar_info(self):
        mayor = self.archivo.paciente_mayor_costo(self.pacientes)
        dicc = self.archivo.promedio_por_especialidad(self.pacientes)
        esp_min = self.archivo.especialidad_menor_promedio(dicc)

        self.lbl_max.config(text=f"Paciente mayor costo: {mayor.nombre.upper()} - Diagnóstico: {mayor.diagnostico.upper()}")
        self.lbl_min.config(text=f"Especialidad menor promedio: {esp_min.lower()}")


if __name__ == "__main__":
    root = tk.Tk()
    app = Ventana(root)
    root.mainloop()

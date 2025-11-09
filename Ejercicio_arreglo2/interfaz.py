import tkinter as tk
from tkinter import ttk, messagebox
from clases import ArchivoSocios
from funciones import socio_mayor_mensualidad,promedio_por_plan,plan_promedio_mas_bajo

archivo = ArchivoSocios("socios.txt")
socios = archivo.abrir()

maximo = socio_mayor_mensualidad(socios)
promedios = promedio_por_plan(socios)
plan_min = plan_promedio_mas_bajo(promedios)

def mostrar_datos():
    for fila in tree.get_children():
        tree.delete(fila)
    plan = combo.get()
    filtrados = [s for s in socios if s.plan == plan] if plan != "Todos" else socios
    for s in filtrados:
        tree.insert("", "end", values=(s.id, s.nombre, s.edad, s.plan, s.mensualidad))

def mostrar_promedios():
    texto = "\n".join([f"{p}: ${v:.2f}" for p, v in promedios.items()])
    messagebox.showinfo("Promedios por plan", texto)

ventana = tk.Tk()
ventana.title("Gestión de Socios - FitLife")
ventana.geometry("650x400")

ttk.Label(ventana, text="Filtrar por plan:").pack(pady=5)
combo = ttk.Combobox(ventana, values=["Todos"] + list(set(s.plan for s in socios)))
combo.current(0)
combo.pack()
combo.bind("<<ComboboxSelected>>", lambda e: mostrar_datos())

columnas = ("ID", "Nombre", "Edad", "Plan", "Mensualidad")
tree = ttk.Treeview(ventana, columns=columnas, show="headings", height=8)
for col in columnas:
    tree.heading(col, text=col)
tree.pack(pady=10, fill="x")

lbl_max = ttk.Label(ventana, text=f"SOCIO CON MENSUALIDAD MÁXIMA: {maximo.nombre.upper()}")
lbl_max.pack(pady=3)
lbl_min = ttk.Label(ventana, text=f"PLAN CON MENOR PROMEDIO: {plan_min.lower()}")
lbl_min.pack(pady=3)

ttk.Button(ventana, text="Mostrar promedios por plan", command=mostrar_promedios).pack(pady=10)

mostrar_datos()
ventana.mainloop()
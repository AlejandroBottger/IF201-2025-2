from tkinter import *
from tkinter import ttk, messagebox

# --- Datos base ---
categorias = ("Tecnología", "Hogar", "Ropa", "Alimentos")  # Tupla
productos = []  # Lista de diccionarios

# --- Funciones de control ---
def agregar_producto():
    codigo = txt_codigo.get()
    nombre = txt_nombre.get()
    categoria = cbo_categoria.get()
    precio = txt_precio.get()

    if not codigo or not nombre or not categoria or not precio:
        messagebox.showwarning("Validación", "Todos los campos son obligatorios")
        return

    # Diccionario del producto
    producto = {
        "codigo": codigo,
        "nombre": nombre,
        "categoria": categoria,
        "precio": float(precio)
    }
    productos.append(producto)
    actualizar_treeview()
    limpiar_campos()

def actualizar_treeview():
    for item in tree.get_children():
        tree.delete(item)
    for prod in productos:
        tree.insert("", "end", values=(prod["codigo"], prod["nombre"], prod["categoria"], prod["precio"]))

def limpiar_campos():
    txt_codigo.delete(0, END)
    txt_nombre.delete(0, END)
    cbo_categoria.set("")
    txt_precio.delete(0, END)

def seleccionar_registro(event):
    seleccionado = tree.focus()
    if not seleccionado:
        return
    valores = tree.item(seleccionado, "values")
    txt_codigo.delete(0, END)
    txt_codigo.insert(0, valores[0])
    txt_nombre.delete(0, END)
    txt_nombre.insert(0, valores[1])
    cbo_categoria.set(valores[2])
    txt_precio.delete(0, END)
    txt_precio.insert(0, valores[3])

def eliminar_producto():
    seleccionado = tree.focus()
    if not seleccionado:
        messagebox.showwarning("Eliminar", "Seleccione un registro para eliminar")
        return
    valores = tree.item(seleccionado, "values")
    codigo = valores[0]
    for p in productos:
        if p["codigo"] == codigo:
            productos.remove(p)
            break
    actualizar_treeview()
    limpiar_campos()

def modificar_producto():
    seleccionado = tree.focus()
    if not seleccionado:
        messagebox.showwarning("Modificar", "Seleccione un registro para modificar")
        return
    valores = tree.item(seleccionado, "values")
    codigo_original = valores[0]
    for p in productos:
        if p["codigo"] == codigo_original:
            p["codigo"] = txt_codigo.get()
            p["nombre"] = txt_nombre.get()
            p["categoria"] = cbo_categoria.get()
            p["precio"] = float(txt_precio.get())
            break
    actualizar_treeview()
    limpiar_campos()

# --- Ventana principal ---
ventana = Tk()
ventana.title("Gestión de Productos con Tkinter")
ventana.geometry("700x400")
ventana.config(padx=10, pady=10)

# --- Frame del formulario ---
frm_form = Frame(ventana)
frm_form.pack(fill=X, pady=10)

Label(frm_form, text="Código:").grid(row=0, column=0, padx=5, pady=5, sticky=E)
txt_codigo = Entry(frm_form)
txt_codigo.grid(row=0, column=1, padx=5, pady=5)

Label(frm_form, text="Nombre:").grid(row=1, column=0, padx=5, pady=5, sticky=E)
txt_nombre = Entry(frm_form)
txt_nombre.grid(row=1, column=1, padx=5, pady=5)

Label(frm_form, text="Categoría:").grid(row=0, column=2, padx=5, pady=5, sticky=E)
cbo_categoria = ttk.Combobox(frm_form, values=categorias, state="readonly")
cbo_categoria.grid(row=0, column=3, padx=5, pady=5)

Label(frm_form, text="Precio:").grid(row=1, column=2, padx=5, pady=5, sticky=E)
txt_precio = Entry(frm_form)
txt_precio.grid(row=1, column=3, padx=5, pady=5)

# --- Botones ---
frm_btn = Frame(ventana)
frm_btn.pack(pady=10)

Button(frm_btn, text="Agregar", width=10, command=agregar_producto).grid(row=0, column=0, padx=5)
Button(frm_btn, text="Modificar", width=10, command=modificar_producto).grid(row=0, column=1, padx=5)
Button(frm_btn, text="Eliminar", width=10, command=eliminar_producto).grid(row=0, column=2, padx=5)
Button(frm_btn, text="Limpiar", width=10, command=limpiar_campos).grid(row=0, column=3, padx=5)

# --- TreeView ---
frm_tree = Frame(ventana)
frm_tree.pack(fill=BOTH, expand=True)

columnas = ("Código", "Nombre", "Categoría", "Precio")
tree = ttk.Treeview(frm_tree, columns=columnas, show="headings")

for col in columnas:
    tree.heading(col, text=col)
    tree.column(col, width=150)

tree.pack(fill=BOTH, expand=True)
tree.bind("<ButtonRelease-1>", seleccionar_registro)

ventana.mainloop()

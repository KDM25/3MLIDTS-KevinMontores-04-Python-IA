### Formulario de registro
## Almacenamiento en TXT sin validación

import tkinter as tk
from tkinter import messagebox


### Definición de funciones

def limpiar_campos():
    tbNombre.delete(0, tk.END)
    tbApellidos.delete(0, tk.END)
    tbTelefono.delete(0, tk.END)
    tbEdad.delete(0, tk.END)
    tbEstatura.delete(0, tk.END)
    var_genero.set(0)

    tbNombre.focus()


def borrar_fun():
    limpiar_campos()


def guardar_valores():
    # Obtener valores desde los Entry
    nombre = tbNombre.get()
    apellidos = tbApellidos.get()
    telefono = tbTelefono.get()
    edad = tbEdad.get()
    estatura = tbEstatura.get()

    # Obtener género
    genero = ""

    if var_genero.get() == 1:
        genero = "Hombre"

    elif var_genero.get() == 2:
        genero = "Mujer"

    elif var_genero.get() == 3:
        genero = "Otro"

    # Ruta fija fuera de OneDrive
    ruta_archivo = r"C:\Users\monto\Documents\#3MAgoDic26-python.txt"

    try:
        with open(ruta_archivo, "a", encoding="utf-8") as archivo:

            archivo.write(f"Nombre: {nombre}\n")
            archivo.write(f"Apellidos: {apellidos}\n")
            archivo.write(f"Teléfono: {telefono}\n")
            archivo.write(f"Edad: {edad}\n")
            archivo.write(f"Estatura: {estatura}\n")
            archivo.write(f"Género: {genero}\n")
            archivo.write("------------------------\n")

        messagebox.showinfo(
            "Registro",
            "Los datos fueron guardados correctamente."
        )

        limpiar_campos()

    except Exception as error:

        messagebox.showerror(
            "Error",
            f"No se pudieron guardar los datos.\n\n{error}"
        )


### Creación de ventana

ventana = tk.Tk()

ventana.title("Formulario de Registro")
ventana.geometry("520x500")
ventana.resizable(False, False)


### Fuentes

fuente = ("Arial", 11)
fuente_titulo = ("Arial", 18, "bold")
fuente_subtitulo = ("Arial", 11, "bold")


### Variable RadioButton

var_genero = tk.IntVar()
var_genero.set(0)


### Frame principal

framePrincipal = tk.Frame(
    ventana,
    padx=40,
    pady=25
)

framePrincipal.pack(
    fill="both",
    expand=True
)


### Título

lbTitulo = tk.Label(
    framePrincipal,
    text="Formulario de Registro",
    font=fuente_titulo
)

lbTitulo.grid(
    row=0,
    column=0,
    columnspan=2,
    pady=(0, 20)
)


### Nombre

lbNombre = tk.Label(
    framePrincipal,
    text="Nombres:",
    font=fuente
)

lbNombre.grid(
    row=1,
    column=0,
    sticky="w",
    padx=5,
    pady=7
)


tbNombre = tk.Entry(
    framePrincipal,
    font=fuente,
    width=30
)

tbNombre.grid(
    row=1,
    column=1,
    padx=5,
    pady=7
)


### Apellidos

lbApellidos = tk.Label(
    framePrincipal,
    text="Apellidos:",
    font=fuente
)

lbApellidos.grid(
    row=2,
    column=0,
    sticky="w",
    padx=5,
    pady=7
)


tbApellidos = tk.Entry(
    framePrincipal,
    font=fuente,
    width=30
)

tbApellidos.grid(
    row=2,
    column=1,
    padx=5,
    pady=7
)


### Teléfono

lbTelefono = tk.Label(
    framePrincipal,
    text="Teléfono:",
    font=fuente
)

lbTelefono.grid(
    row=3,
    column=0,
    sticky="w",
    padx=5,
    pady=7
)


tbTelefono = tk.Entry(
    framePrincipal,
    font=fuente,
    width=30
)

tbTelefono.grid(
    row=3,
    column=1,
    padx=5,
    pady=7
)


### Edad

lbEdad = tk.Label(
    framePrincipal,
    text="Edad:",
    font=fuente
)

lbEdad.grid(
    row=4,
    column=0,
    sticky="w",
    padx=5,
    pady=7
)


tbEdad = tk.Entry(
    framePrincipal,
    font=fuente,
    width=30
)

tbEdad.grid(
    row=4,
    column=1,
    padx=5,
    pady=7
)


### Estatura

lbEstatura = tk.Label(
    framePrincipal,
    text="Estatura:",
    font=fuente
)

lbEstatura.grid(
    row=5,
    column=0,
    sticky="w",
    padx=5,
    pady=7
)


tbEstatura = tk.Entry(
    framePrincipal,
    font=fuente,
    width=30
)

tbEstatura.grid(
    row=5,
    column=1,
    padx=5,
    pady=7
)


### Género

lbGenero = tk.Label(
    framePrincipal,
    text="Género:",
    font=fuente_subtitulo
)

lbGenero.grid(
    row=6,
    column=0,
    sticky="w",
    padx=5,
    pady=(12, 5)
)


frameGenero = tk.Frame(framePrincipal)

frameGenero.grid(
    row=6,
    column=1,
    sticky="w",
    pady=(12, 5)
)


rbHombre = tk.Radiobutton(
    frameGenero,
    text="Hombre",
    variable=var_genero,
    value=1,
    font=fuente
)

rbHombre.pack(
    side="left",
    padx=5
)


rbMujer = tk.Radiobutton(
    frameGenero,
    text="Mujer",
    variable=var_genero,
    value=2,
    font=fuente
)

rbMujer.pack(
    side="left",
    padx=5
)


rbOtro = tk.Radiobutton(
    frameGenero,
    text="Otro",
    variable=var_genero,
    value=3,
    font=fuente
)

rbOtro.pack(
    side="left",
    padx=5
)


### Botones

frameBotones = tk.Frame(framePrincipal)

frameBotones.grid(
    row=7,
    column=0,
    columnspan=2,
    pady=25
)


btnBorrar = tk.Button(
    frameBotones,
    text="Borrar valores",
    command=borrar_fun,
    font=fuente,
    width=15
)

btnBorrar.pack(
    side="left",
    padx=10
)


btnGuardar = tk.Button(
    frameBotones,
    text="Guardar",
    command=guardar_valores,
    font=fuente,
    width=15
)

btnGuardar.pack(
    side="left",
    padx=10
)


### Cursor inicial

tbNombre.focus()


### Ejecución

ventana.mainloop()

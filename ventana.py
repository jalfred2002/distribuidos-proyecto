import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import *


# funcion validar datos
def validar():
    validacion = True
    if (
        vehiculo.get() == ""
        or velocidad.get() == ""
        or retraso.get() == ""
        or rumbo.get() == ""
    ):
        validacion = False

        print(f"{vehiculo}")
    return validacion


# llenado de la barra de estado
def llenar():
    for i in range(101):
        progressbar["value"] = i
        ventana.update_idletasks()  # Actualiza la ventana
        ventana.after(
            60
        )  # Simulación de trabajo (ajusta el tiempo según tus necesidades)

    messagebox.showinfo("Información", "proceso completado")


# funcion validar datos
def limpiar():
    # Elimina todo el contenido del campos
    vehiculo.delete(0, tk.END)
    velocidad.delete(0, tk.END)
    retraso.delete(0, tk.END)
    rumbo.delete(0, tk.END)


# funcion enviar datos
def enviar_datos():

    if validar() == True:
        limpiar()
        messagebox.showinfo("Información", "Su vehiculo ha sido enviado")
        llenar()
    else:
        messagebox.showinfo("Información", "Todos los campos deben estar completos")


# Cuadro de dialogo
ventana = tk.Tk()


# dimencionees de la ventana
ancho_ventana = 800
alto_ventana = 500

x_ventana = ventana.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = ventana.winfo_screenheight() // 2 - alto_ventana // 2
# centrar ventana
posicion = (
    str(ancho_ventana)
    + "x"
    + str(alto_ventana)
    + "+"
    + str(x_ventana)
    + "+"
    + str(y_ventana)
)
ventana.geometry(posicion)
# titulo de la ventana
ventana.title("Principal")

# contenide de la ventana
label = Label(ventana, text="Gestion de vehiculo", font=("Helvetica", 18, "bold"))
label.pack(pady=30)

lvehiculo = Label(
    ventana,
    text="nombre del vehiculo:",
)
lvehiculo.place(x=30, y=100)

vehiculo = tk.Entry(ventana, highlightthickness=1, highlightbackground="blue")
vehiculo.pack(pady=20)
vehiculo.place(x=180, y=100, width="200px")

lvelocidad = Label(
    ventana,
    text="velocidad del vehiculo:",
)
lvelocidad.place(x=30, y=150)

velocidad = tk.Entry(ventana, highlightthickness=1, highlightbackground="blue")
velocidad.pack(pady=20)
velocidad.place(x=180, y=150, width="200px")

lretraso = Label(
    ventana,
    text="Promedio de retraso:",
)
lretraso.place(x=30, y=200)

retraso = tk.Entry(ventana, highlightthickness=1, highlightbackground="blue")
retraso.pack(pady=20)
retraso.place(x=180, y=200, width="200px")

lrumbo = Label(
    ventana,
    text="Rumbo inicial:",
)
lrumbo.place(x=30, y=250)

rumbo = tk.Entry(ventana, highlightthickness=1, highlightbackground="blue")
rumbo.pack(pady=20)
rumbo.place(x=180, y=250, width="200px")


# boton de enviar
boton_enviar = tk.Button(
    ventana, text="Enviar vehiculo", fg="white", command=enviar_datos
)
boton_enviar.configure(bg="#3371FF")
boton_enviar.pack()
boton_enviar.place(x=180, y=300, width="200px")


# barra de  progreso
lestado = Label(
    ventana,
    text="Barra de estado del puente",
)
lestado.place(x=30, y=360, width="300px")

progressbar = Progressbar(ventana, orient=tk.HORIZONTAL, length=300, mode="determinate")
progressbar.pack()
progressbar.place(relx=0.5, rely=0.8, anchor="center", width=500)

ventana.mainloop()

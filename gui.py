import tkinter as tk
from tkinter import messagebox
from game import JuegoAhorcado
from messages import MENSAJES_ES


ventana = tk.Tk()
ventana.title("Juego del Ahorcado")
ventana.geometry("400x400")

juego = None

def mostrar_frame(frame):
    frame.tkraise()
def salir():
    if messagebox.askokcancel("Salir", "¿Seguro que quieres salir?"):
        ventana.destroy()

# INICIO

frame_inicio = tk.Frame(ventana)
frame_inicio.place(relwidth=1, relheight=1)

tk.Label(
    frame_inicio, 
    text="Bienvenido al juego del Ahorcado", 
    font=("Helvetica", 16)
).pack(pady=20)

tk.Button(
    frame_inicio, 
    text="Jugar", 
    command=lambda: mostrar_frame(frame_categorías)
).pack(pady=10)

tk.Button(frame_inicio, 
    text="Salir", 
    command=salir
).pack(pady=20)


#CATEGORÍAS

frame_categorías = tk.Frame(ventana)
frame_categorías.place(relwidth=1, relheight=1)

tk.Label(
    frame_categorías,
    text="Selecciona una categoría",
    font=("Helvetica", 16)
).pack(pady=20)

def seleccionar_categoria(categoria):
    global juego
    juego = JuegoAhorcado(categoria)
    palabra_label.config(text=juego.mostrar_palabra())
    estado.config(text=f"Intentos restantes: {juego.intentos_restantes}")
    boton_jugar.config(state=tk.NORMAL)
    mostrar_frame(frame_juego)

tk.Button(frame_categorías, text="Animales", command=lambda: seleccionar_categoria("animales")).pack(pady=10)
tk.Button(frame_categorías, text="Frutas", command=lambda: seleccionar_categoria("frutas")).pack(pady=10)
tk.Button(frame_categorías, text="Países", command=lambda: seleccionar_categoria("paises")).pack(pady=10)

tk.Button(frame_categorías, text="Volver", command=lambda: mostrar_frame(frame_inicio)).pack(pady=20)


# JUEGO
frame_juego = tk.Frame(ventana)
frame_juego.place(relwidth=1, relheight=1)


estado = tk.Label(frame_juego, text="")
estado.pack()

palabra_label = tk.Label(frame_juego, text="", font=("Helvetica", 18))
palabra_label.pack()

entrada = tk.Entry(frame_juego)
entrada.pack()

# 🔥 función del botón
def jugar():
    letra = entrada.get()
    entrada.delete(0, tk.END)

    resultado = juego.intentar_letra(letra)
    palabra_label.config(text=juego.mostrar_palabra())

    if resultado == "correcto":
        estado.config(text=MENSAJES_ES["correcta"])
    elif resultado == "repetida":
        estado.config(text=MENSAJES_ES["repetida"])
    elif resultado == "ganaste":
        estado.config(text=MENSAJES_ES["ganaste"].format(palabra=juego.palabra_secreta))
        boton_jugar.config(state=tk.DISABLED)
    elif resultado == "perdiste":
        estado.config(text=MENSAJES_ES["perdiste"].format(palabra=juego.palabra_secreta))
        boton_jugar.config(state=tk.DISABLED)
    elif resultado == "incorrecto":
        estado.config(text=MENSAJES_ES["incorrecto"].format(intentos=juego.intentos_restantes))

boton_jugar = tk.Button(frame_juego, text="Jugar", command=jugar)
boton_jugar.pack()

def jugar_evento(event):
    jugar()

entrada.bind("<Return>", jugar_evento)

def reiniciar():
    juego.reiniciar_juego()
    palabra_label.config(text=juego.mostrar_palabra())
    estado.config(text=f"Intentos restantes: {juego.intentos_restantes}")
    boton_jugar.config(state=tk.NORMAL)
    entrada.focus()

tk.Button(frame_juego, text="Reiniciar", command=reiniciar).pack(pady=10)
tk.Button(frame_juego, text="Volver al inicio", command=lambda: mostrar_frame(frame_inicio)).pack(pady=10)

mostrar_frame(frame_inicio)
ventana.mainloop()
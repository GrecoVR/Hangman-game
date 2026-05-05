import tkinter as tk
from game import JuegoAhorcado

juego = JuegoAhorcado("animales")

ventana = tk.Tk()
ventana.title("Juego del Ahorcado")
ventana.geometry("400x400")

label = tk.Label(ventana, text="¡Bienvenido al juego del Ahorcado!")
label.pack()

estado = tk.Label(ventana, text="")
estado.pack()

palabra_label = tk.Label(ventana, text="")
palabra_label.pack()

entrada = tk.Entry(ventana)
entrada.pack()

# 🔥 función del botón
def jugar():
    letra = entrada.get()
    entrada.delete(0, tk.END)

    resultado = juego.intentar_letra(letra)

    palabra_label.config(text=juego.mostrar_palabra())

    if resultado == "¡Correcto!":
        estado.config(text="¡Correcto!")
    elif resultado == "Ya has adivinado esa letra. Intenta con otra.":
        estado.config(text="Ya has adivinado esa letra. Intenta con otra.")
    elif resultado == f"¡Felicidades! Has adivinado la palabra: {juego.palabra_secreta}":
        estado.config(text=resultado)
        fin_juego(resultado)
    elif resultado == f"¡Has perdido! La palabra secreta era: {juego.palabra_secreta}":
        estado.config(text=resultado)
        fin_juego(resultado)
    elif resultado == f"Letra incorrecta. Intentos restantes: {juego.intentos_restantes}":
        estado.config(text=resultado)

def fin_juego(mensaje):
    estado.config(text=mensaje)
    boton_jugar.config(state=tk.DISABLED)

boton_jugar = tk.Button(ventana, text="Jugar", command=jugar)
boton_jugar.pack()

boton_reiniciar = tk.Button(ventana, text="Reiniciar", command=juego.reiniciar_juego)
boton_reiniciar.pack()

ventana.mainloop()
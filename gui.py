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

# 🔥 función para mostrar palabra
def mostrar_palabra():
    resultado = ""
    for letra in juego.palabra_secreta:
        if letra in juego.letras_adivinadas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado

# 🔥 función del botón
def jugar():
    letra = entrada.get()
    entrada.delete(0, tk.END)

    if letra not in juego.letras_adivinadas:
        juego.letras_adivinadas.add(letra)

    if letra not in juego.palabra_secreta:
        juego.intentos_restantes -= 1
        estado.config(text=f"Intentos restantes: {juego.intentos_restantes}")

    palabra_label.config(text=mostrar_palabra())

    if intentos_restantes := juego.intentos_restantes <= 0:
        fin_juego(f"¡Has perdido! La palabra era: {juego.palabra_secreta}")
    if comprobar_victoria():
        fin_juego("¡Felicidades! Has ganado.")

def comprobar_victoria():
    if all(letra in juego.letras_adivinadas for letra in juego.palabra_secreta):
        estado.config(text="¡Felicidades! Has ganado.")
        return True
    elif juego.intentos_restantes <= 0:
        estado.config(text=f"¡Has perdido! La palabra era: {juego.palabra_secreta}")
        return True
    return False

def fin_juego(mensaje):
    estado.config(text=mensaje)
    boton_jugar.config(state=tk.DISABLED)

boton_jugar = tk.Button(ventana, text="Jugar", command=jugar)
boton_jugar.pack()

def reiniciar():
    juego.letras_adivinadas.clear()
    juego.intentos_restantes = 6
    juego.palabra_secreta = juego.categoria.cargar_palabra_secreta()
    boton_jugar.config(state=tk.NORMAL)

boton_reiniciar = tk.Button(ventana, text="Reiniciar", command=reiniciar)
boton_reiniciar.pack()

ventana.mainloop()
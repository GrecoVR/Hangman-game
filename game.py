from word_manager import WordManager
from display import mostrar_ahorcado, mostrar_tablero
from input_handler import obtener_letra

class JuegoAhorcado:
    def __init__(self, categoria):
        self.categoria = WordManager(categoria)
        self.palabra_secreta = self.categoria.cargar_palabra_secreta().lower()
        self.letras_adivinadas = set()
        self.intentos_restantes = 6

    def jugar(self):
        print("¡Bienvenido al juego del Ahorcado!")
        while self.intentos_restantes > 0:
            mostrar_ahorcado(self.intentos_restantes)
            mostrar_tablero(self.palabra_secreta, self.letras_adivinadas)
            print(f"Intentos restantes: {self.intentos_restantes}")
            letra = obtener_letra()
            if letra in self.letras_adivinadas:
                print("Ya has adivinado esa letra. Intenta con otra.")
                continue
            self.letras_adivinadas.add(letra)
            if letra in self.palabra_secreta:
                self.letras_adivinadas.add(letra)
                if all(l in self.letras_adivinadas for l in self.palabra_secreta):
                    print(f"¡Felicidades! Has adivinado la palabra: {self.palabra_secreta}")
                    break
            else:
                self.intentos_restantes -= 1
                print(f"Letra incorrecta. Intentos restantes: {self.intentos_restantes}")
        else:
            print(f"¡Has perdido! La palabra secreta era: {self.palabra_secreta}")

        if self.intentos_restantes > 0:
            print(f"¡Gracias por jugar! ¡Hasta la próxima!: La palabra secreta era: {self.palabra_secreta}")

    def intentar_letra(self, letra):
        letra = letra.lower().strip()
        if letra in self.letras_adivinadas:
            return "repetida"
        self.letras_adivinadas.add(letra)
        if letra in self.palabra_secreta:
            if all(l in self.letras_adivinadas for l in self.palabra_secreta):
                return "ganaste"
            return "correcto"
        else:
            self.intentos_restantes -= 1
            if self.intentos_restantes <= 0:
                return "perdiste"
            return "incorrecto"
        
    def verificar_victoria(self):
        return all(letra in self.letras_adivinadas for letra in self.palabra_secreta)
    
    def reiniciar_juego(self):
        self.letras_adivinadas = set()
        self.intentos_restantes = 6
        self.palabra_secreta = self.categoria.cargar_palabra_secreta().lower()

    def mostrar_palabra(self):
        resultado = ""
        for letra in self.palabra_secreta:
            if letra in self.letras_adivinadas:
                resultado += letra + " "
            else:
                resultado += "_ "
        return resultado
import random
import os

class WordManager:
    def __init__(self, categoria):
        self.directorio_actual = os.path.dirname(__file__)
        self.ruta_archivo_palabras = os.path.join(self.directorio_actual, "data", f"{categoria}.txt")

        with open(self.ruta_archivo_palabras, "r", encoding="utf-8") as archivo:
            self.palabras = [p.strip() for p in archivo if p.strip()]

    def cargar_palabra_secreta(self):
        return random.choice(self.palabras)
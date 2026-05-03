from game import JuegoAhorcado

if __name__ == "__main__":
    categoria = input("Selecciona una categoría (animales, frutas, países): ")
    game = JuegoAhorcado(categoria)
    game.jugar()
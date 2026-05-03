def mostrar_tablero(palabra_secreta, letras_adivinadas):
    tablero = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            tablero += letra + " "
        else:
            tablero += "_ "
    print(tablero)

def mostrar_ahorcado(intentos_restantes):
    estados = [
        """
         _______
         |     |
         |     O
         |    /|\\
         |    / \\
        _|_
        """,
        """
         _______
         |     |
         |     O
         |    /|\\
         |    /
        _|_
        """,
        """
         _______
         |     |
         |     O
         |    /|\\
         |
        _|_
        """,
        """
         _______
         |     |
         |     O
         |    /|
         |
        _|_
        """,
        """
         _______
         |     |
         |     O
         |     |
         |
        _|_
        """,
        """
         _______
         |     |
         |     O
         |
         |
        _|_
        """,
        """
         _______
         |     |
         |
         |
         |
        _|_
        """
    ]

    print(estados[6 - intentos_restantes])
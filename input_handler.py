def obtener_letra():
    letra = input("Adivina una letra: ").lower()
    if len(letra) != 1 or not letra.isalpha():
        print("Por favor, ingresa una letra válida.")
        return obtener_letra()
    return letra
# Convertit l'argument texte en nombre entier et renvoie ce nombre
def b(texte):
    try:
        text_to_int = int(texte)
        return text_to_int
    except :
        print("Ce n'est pas un nombre ! ")

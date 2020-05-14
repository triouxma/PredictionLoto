# - si le paramètre texte possède 9 caractères : ajouter le caractère '0' en début de chaîne et renvoyer le résultat
# - sinon renvoyer le texte tel quel
def i(texte):
    mot = texte
    if len(texte) ==9:
        mot = '0' + mot
    return mot

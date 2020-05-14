# Pour chaque nombre contenu dans l'argument liste :
# - si le nombre est supérieur ou égale à 50 : retirer 50 à ce nombre
# - sinon ne pas modifier ce nombre
# Renvoyer la liste modifiée
def p(liste):
    return [elmt - 50 if elmt>=50 else elmt for elmt in liste ]
    # TODO

from fonctions_secretes_du_loto.h import h

# Applique la fonction h() à chaque valeur contenue dans l'argument liste et renvoie la liste modifiée
def q(liste):
    liste = [h(i) for i in liste]

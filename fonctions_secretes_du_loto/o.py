# Convertir chaque élément du paramètre liste en chaînes de caractères et renvoyer la liste modifiée
def o(liste):
    try :
        liste = [str(i) for i in liste]
        return liste
    except :
        print("Problème avec la liste")

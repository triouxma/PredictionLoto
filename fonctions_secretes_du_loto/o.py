# Convertir chaque élément du paramètre liste en chaînes de caractères et renvoyer la liste modifiée
def o(liste):
    try :
        list_to_list = list()
        for i in liste:
            list_to_list.append(str(i))
        return list_to_list
    except :
        print("Problème avec la liste")


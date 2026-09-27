liste = [ "22", "80", "443", "8080"]
print(f"Le premier element du tableau est :  {liste[0]}")
print(f"Le dernier element du tableau est : {liste[-1]}")
print(f"le nombre d'element est : {len(liste)}")
liste.append(3389)
liste.pop(1)
print(liste)
#liste.remove("80")
print(liste)
#pour ajouter plusieurs element de la liste
liste.extend(["443", "59", "79"])
#pour remplacer un element de la liste
liste[0] = "21"
print(liste)
#pour supprimer un element de la liste
liste.pop(5)
print(liste)
#pour effacer la liste
liste.clear()
print("La liste finale est : {}".format(liste))
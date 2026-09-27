import statistics
liste_entier = []
nombres = input("donner un liste de nombre separe par des virgules : ").split(",")
for nombre in nombres:
    nombre_entier = int(nombre)
    liste_entier.append(nombre_entier)
print(liste_entier)
somme = sum(liste_entier)
print(f"La somme total des nombre entier dans la liste est : {somme}")
moyenne = statistics.mean(liste_entier)
print(f"La moyenne est : {moyenne}")
n = 0
for entier in liste_entier:
    if entier > moyenne:
        n += 1
print(f"le nombre de nombre superieur a la moyenne est : {n}")
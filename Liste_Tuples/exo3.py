from random import shuffle
chaine = input("donner une chaine sous forme de mot1/mot2/mot/..").split("/")
print(chaine)
shuffle(chaine)
print(chaine)
if len(chaine) < 10:
    print(chaine[0] +"," + chaine[1])
else:
    print(chaine[-1] +"," + chaine[-2] + "," +chaine[-3])
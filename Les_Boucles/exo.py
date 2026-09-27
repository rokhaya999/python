from random import randint
just_price = randint(1, 1000)
print(just_price)
running = True
while running:
    user_price = int(input("donner un nombre entre 1 et 1000 : "))
    if user_price == just_price:
        print("vous avez trouvé le bon nombre")
        running = False
    elif user_price > just_price:
        print("c'est moins")
    elif user_price < just_price:
        print("c'est plus")
print("fin du jeu")    
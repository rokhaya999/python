ip = input("donner une ip : ")
port_valid = False
while not port_valid:

    try:

        port = int(input("donner un numero de port : "))
        port_valid = True
    except ValueError:
        print("donner un port valide")
statut = input("donner le statut du port up ou down : ")

if statut.lower() == "up":
    est_actif = True
else:
    est_actif = False
if port < 1024:
    est_port_privi = True
else:
    est_port_privi = False
print("rapport de l'ip " + ip + " port, " +str(port)) 
if est_actif and est_port_privi:
    print("l'interface active et port priviligé")
elif est_actif and not est_port_privi:
    print("l'interface active mais port standard")
else:
    print("Pas actif")
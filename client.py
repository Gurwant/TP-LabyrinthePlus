import socket
import select


hote = "localhost"
port = 10000


serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.connect((hote, port))
print("Connexion établie avec le serveur sur le port {}".format(port))
print("Appuyer sur entrée pour recevoir des messages")
msg_a_envoyer = ""
while msg_a_envoyer != b"Demarrage de la partie":
    try:
        a_lire, wlist, xlist = select.select([serveur],[], [], 0.05)
    except select.error:
        pass
    else:
        for message in a_lire :
            msg_recu = serveur.recv(1024).decode()
            if msg_recu == "__Answer":
                msg_a_envoyer = input("> ")
            else :
                print(msg_recu)

    msg_a_envoyer = input("> ")
    msg_a_envoyer = msg_a_envoyer.encode()
    serveur.send(msg_a_envoyer)

#Demmarage de la partie

#Chargement de la carte

nom_carte = serveur.recv(1024).decode()
carte = Pam(nom_carte[:-4],"Cartes\\" + nom_carte)

#Ajoute les robots sur la carte

msg_recu = serveur.recv(1024).decode()
while msg_recu != "play" :
    msg_recu = serveur.recv(1024).decode()
    carte.robot(msg_recu)

#Joue

print("Fermeture de la connexion")
connexion_avec_serveur.close()

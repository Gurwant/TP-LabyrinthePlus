import socket
import select


hote = "localhost"
port = 10000


serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.connect((hote, port))
print("Connexion établie avec le serveur sur le port {}".format(port))
print("Appuyer sur entrée pour recevoir des messages")
msg_a_envoyer = ""
while msg_a_envoyer != b"fin":
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

print("Fermeture de la connexion")
connexion_avec_serveur.close()

import socket
import select
import sys
import re

hote = "localhost"
port = 10000

print("On tente de se connecter au serveur...")
try :
    serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serveur.connect((hote, port))
    print("Connexion établie avec le serveur.")
except:
    print("Echec lors de la connexion au serveur.")
    sys.exit(1)

def my_input(ques, exreg):
    """Fonction pour demander une entrée et redemander tant qu'elle n'est pas
    conforme à l'expression régulière passée en parametre"""

    entree = input(ques)
    while not re.fullmatch(exreg, entree) :
        entree = input(ques)
    return(entree)

def set_up_player ():
    serveur.send(my_input("Veuillez entrer votre nom : ", "[\w]*").encode())
    serveur.send(my_input("Veuillez entrer le caractere representant votre robot : "
        ,"([^ \t\n\r\f\vOoXx]){1}").encode())
    msg_recu = ""
    while msg_recu != "\nDemarrage de la partie\n" :
        serveur.send(my_input("Veuillez entrer C pour commencer à jouer.\n>","[Cc]{1}").lower().encode())
        msg_recu = serveur.recv(1024).decode()
        print(msg_recu)

set_up_player()

msg_recu = ""
while not msg_recu.startswith("End") :
    msg_recu = serveur.recv(1024).decode()
    if msg_recu == "Play" :
        serveur.send(my_input("A vous de jouer.\n> ","[nseo][1-9]*"))
    else:
        print(msg_recu)

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

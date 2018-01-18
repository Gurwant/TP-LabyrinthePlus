import socket
import select
import os
import re
from pam import *
from utilisateur import *
from game import *

def map_choice ():
    """ Menu du Jeu :
            -Affiche les cartes disponibles
            -Retourne la Carte choisie"""

    maps = []

    #On charge les maps disponnibles
    for f_name in os.listdir(".\Cartes") :
        if f_name.endswith('.txt') :
            try :
                carte = Pam(f_name[:-4], 'Cartes\\' + f_name)
            except ValueError as err:
                print("Erreur lors de la lecture de {} : {}.".format('Cartes\\' + f_name, str(err)))
            else:
                maps.append(carte)

    #On affiche les diferentes maps a choisir
    print("Labyrinthes existants :")
    for i, carte in enumerate(maps) :
        print("\t%i - %s" % (i + 1, carte.name))

    #On prend le choix de l'utilisateur
    choice = input("Entrez un numéro de labyrinthe pour commencer a jouer : ")
    while not re.fullmatch(r'[1-' + str(len(maps)) + ']{1}', choice) :
        choice = input("Entrez un numéro de labyrinthe pour commencer a jouer : ")

    return(maps[int(choice) - 1])

pam = map_choice()

#On lance le serveur
hote = ''
port = 10000

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind((hote, port))
serveur.listen(3)

serveur_lance = True
clients_connectes = []
joueurs_prets = 0

print("On attend les clients")
#On ecoute les nouvelles connexions et les messages tant que deux clients au moins ne sont pas connectés et qu'un 'c' n'est pas msg_recu
while serveur_lance:
    # On regarde si de nouveaux clients veulent se connecter et on les ajoutes à clients connectés
    connexions_demandees, wlist, xlist = select.select([serveur],[], [], 0.05)
    for connexion in connexions_demandees:
        connexion_avec_client, infos_connexion = connexion.accept()
        clients_connectes.append(Utilisateur(connexion_avec_client))

    # Maintenant, on écoute la liste des clients connectés
    clients_a_lire = []
    try:
        clients_a_lire, wlist, xlist = select.select((c.link for c in clients_connectes),[], [], 0.05)
    except select.error:
        pass
    else:
        # On parcourt la liste des clients à lire
        for client in clients_a_lire:
            for cl in clients_connectes :
                if client == cl.link:
                    print(cl)
                    msg_recu = client.recv(1024).decode()
                    if cl.name == '' :
                        cl.name = msg_recu
                    elif cl.robot == '' :
                        cl.robot = msg_recu[0]
                    elif msg_recu.lower() == 'c' :
                        if len(clients_connectes) >= 2 :
                            if joueurs_prets == len(clients_connectes) :
                                serveur_lance = False
                            else:
                                joueurs_prets += 1
                        else :
                            client.send(b"Il n'y a pas assez de joueurs pour demarrer la partie")
                    else :
                        for cl_to_send in clients_connectes:
                            if cl_to_send.link != client :
                                cl_to_send.link.send((cl.name + " : " + msg_recu).encode())

print("Demarrage de la partie")
lab = Game(pam, clients_connectes)
print(lab)
print("game init")
for client in clients_connectes :
    print(client)
    client.link.send(b"Demarrage de la partie")
    client.link.send(pam.name.encode())

win = False
i = 0
while not win :
    joueur = clients_connectes[i % len(clients_connectes)]
    clients_a_lire = []
    try:
        clients_a_lire, wlist, xlist = select.select((c.link for c in clients_connectes),[], [], 0.05)
    except select.error:
        pass
    else:
        # On parcourt la liste des clients à lire
        for client in clients_a_lire:
            msg_recu = client.recv(1024).decode()
            if msg_recu.lower.startswith("m:") :
                for cl_to_send in clients_connectes:
                    if cl_to_send.link != client :
                        cl_to_send.link.send((cl.name + " : " + msg_recu).encode())
            elif client == joueur.link :
                win = labyrinthe.jouer(joueur,msg_recu)



for client in clients_connectes:
    client.link.close()

connexion_principale.close()

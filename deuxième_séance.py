# -*- coding: utf-8 -*-
"""
Created on Mon May 10 09:40:02 2024

@author: Matéo,Lionel,Hugo,Fatoumata 
"""


###############################################################################
##                                TRANS2                                     ##
##  Entrée : une matrice d'adjacence M                                       ##
##  Retourne la matrice M après avoir ajouté des liens transitifs            ##
###############################################################################
def trans2(M):
    # Parcourir chaque sommet i
    for i in range(len(M)):
        Entrant = []  # Liste des sommets ayant une arête entrante vers i
        Sortant = []  # Liste des sommets ayant une arête sortante depuis i
        
        # Déterminer les arêtes entrantes et sortantes pour le sommet i
        for j in range(len(M[i])):
            if M[i][j] == 1:
                Sortant.append(j)
            if M[j][i] == 1:
                Entrant.append(j)
        
        print(i, Entrant, Sortant)  # Afficher les sommets entrants et sortants pour le sommet i
        
        # Ajouter des liens transitifs entre les sommets entrants et sortants
        for k in range(len(Entrant)):
            for l in range(len(Sortant)):
                M[Entrant[k]][Sortant[l]] = 1
    
    return M  # Retourner la matrice d'adjacence modifiée

# Exemple de matrice d'adjacence
M = [
    [0, 1, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 1, 0, 1],
    [0, 0, 0, 1, 1]
]

# Afficher la matrice après ajout des liens transitifs
print(trans2(M))
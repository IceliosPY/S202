# -*- coding: utf-8 -*-
"""
Created on Mon May 15 10:15:50 2023

@author: Matéo, Lionel, Hugo, Fatoumata
"""

import random 
import numpy as np


###############################################################################
##                                GRAPHE                                     ##
##  Entrée :                                                                 ##
##      n : un entier représentant la taille de la matrice                   ##
##      a : un entier représentant la borne inférieure des valeurs           ##
##      b : un entier représentant la borne supérieure des valeurs           ##
##  Retourne :                                                               ##
##      Une matrice de taille n avec des valeurs appartenant à l'intervalle  ##
##      [a, b] et des valeurs infinies de manière aléatoire.                 ##
###############################################################################
def graphe(n, a, b):
    # Initialiser la matrice vide et les compteurs
    M = []
    cptInf = 0  # Compteur pour les valeurs infinies
    cpt = 0     # Compteur pour les valeurs définies

    # Parcourir chaque ligne de la matrice
    for i in range(n):
        L = []  # Initialiser une nouvelle ligne
        # Parcourir chaque colonne de la matrice
        for j in range(n):
            # Si le nombre de valeurs définies a atteint la moitié de la matrice
            if cpt >= n * n / 2:
                L.append(np.inf)
                cptInf += 1
            # Si le nombre de valeurs infinies a atteint la moitié de la matrice
            elif cptInf >= n * n / 2:
                L.append(random.randint(a, b))
                cpt += 1
            else:
                # Décider aléatoirement entre une valeur infinie et une valeur définie
                if random.randint(1, 2) == 1:
                    L.append(np.inf)
                    cptInf += 1
                else:
                    L.append(random.randint(a, b))
                    cpt += 1
        M.append(L)  # Ajouter la ligne à la matrice
    return M  # Retourner la matrice générée

# Exemple d'utilisation de la fonction graphe
n = 5
a = 1
b = 10
matrice = graphe(n, a, b)
for ligne in matrice:
    print(ligne)

###############################################################################
##                                GRAPHE2                                    ##
##  Entrée :                                                                 ##
##      n : un entier représentant la taille de la matrice                   ##
##      p : un flottant représentant la proportion de valeurs définies       ##
##      a : un entier représentant la borne inférieure des valeurs           ##
##      b : un entier représentant la borne supérieure des valeurs           ##
##  Retourne :                                                               ##
##      Une matrice de taille n avec des valeurs appartenant à l'intervalle  ##
##      [a, b] mélangées avec des valeurs infinies selon la proportion p.    ##
###############################################################################
def graphe2(n, p, a, b):
    M = []
    cpt = 0
    
    """
    L'objectif est d'ajouter dans une liste d'abord toutes les valeurs définies
    puis les valeurs infinies et à la fin de mélanger le tableau
    """
    for i in range(n * n):
        if cpt < n * n * p:
            M.append(random.randint(a, b))
            cpt += 1
        else:
            M.append(np.inf)
            
    random.shuffle(M)  # Permet de mélanger la liste M
    matrice = []
    for i in range(n):
        l = []
        for j in range(n):
            l.append(M.pop(0))
        matrice.append(l)

    return matrice

# Exemple d'utilisation de la fonction graphe2
n = 5
p = 0.5
a = 1
b = 10
matrice = graphe2(n, p, a, b)
for ligne in matrice:
    print(ligne)
# -*- coding: utf-8 -*-
"""
Created on Mon May 15 08:06:02 2023

@author: Matéo,Lionel,Hugo,Fatoumata 
"""
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


###############################################################################
##                               DJIKSTRA                                    ##
##  Entrée : une matrice de distances (matrice) et un sommet de départ       ##
##  Retourne un dictionnaire contenant les distances minimales et les        ##
##  prédécesseurs pour chaque sommet                                         ##
###############################################################################
def djikstra(matrice, depart):
    #Initialisations 
    dico = initialisation(matrice, depart)  # Initialisation de Dijkstra
    # Liste des sommets dont la distance minimale est déterminée
    A = [depart]
    # Permet de prévoir le cas où il y a au moins un sommet qui n'est pas accessible
    boucle = False  
    
    
    # Boucle jusqu'à ce que tous les sommets soient traités ou qu'un sommet inaccessible soit détecté
    while len(matrice) - 1 > len(A) and not boucle:
        sommet_minimum = minimum(dico, A)  # Trouver le sommet avec la distance minimale qui n'est pas encore traité
        if sommet_minimum is None:
            boucle = True           # Si aucun sommet n'est trouvé, il y a des sommets inaccessibles
        else:
            A.append(sommet_minimum) # Ajouter le sommet trouvé à la liste des sommets traités
            
            
            # Mettre à jour les distances des sommets adjacents
            for i in range(len(matrice[A[-1]])):
                if isinstance(matrice[A[-1]][i], int):
                # Vérifier si un chemin plus court a été trouvé
                    if test(matrice, dico, A[-1], i):
                        dico[i][0] = dico[A[-1]][0] + matrice[A[-1]][i]  # Mettre à jour la distance et le prédecesseur du sommet
                        dico[i][1] = A[-1]
    
    return dico
    
###############################################################################
##                             INITIALISATION                                ##
##  Entrée : une matrice de distances (matrice) et un sommet de départ       ##
##  Retourne un dictionnaire contenant les distances initiales et les        ##
##  prédécesseurs pour chaque sommet                                         ##
###############################################################################
def initialisation(matrice, depart):
    dico = {} # Initialiser le dictionnaire pour stocker les distances et les prédecesseurs
    
    
    
    # Parcourir chaque sommet dans le graphe
    for i in range(len(matrice[0])): 
        if i == depart: 
        # Pour le sommet de départ, la distance à lui-même est 0 et il n'a pas de prédecesseur
            dico[i] = [0, 0]
        else:
            # Si il existe un chemin direct entre le sommet de départ et le sommet i
            if isinstance(matrice[depart][i], int):
            
                dico[i] = [matrice[depart][i], depart] # La distance est le coût direct et le prédecesseur est le sommet de départ
            else:
                dico[i] = [matrice[depart][i], None] # Si aucun chemin direct n'existe, la distance est infinie et il n'a pas de prédecesseur
    return dico  # Retourner le dictionnaire des distances et prédecesseurs


###############################################################################
##                               MINIMUM                                     ##
##  Entrée : un dictionnaire des distances (dico) et une liste des sommets   ##
##  traités (sommets_colors)                                                 ##
##  Retourne le sommet avec la distance minimale qui n'a pas encore été      ##
##  traité                                                                   ##
###############################################################################
def minimum(dico, sommets_colors):
    # Initialiser la distance minimale avec l'infini
    mini = float('inf')
    # Initialiser le sommet minimum avec None
    sommet = None
    # Parcourir chaque clé (sommet) dans le dictionnaire
    for cle in dico.keys():
    # Vérifier que la distance du sommet est un entier (ce qui signifie qu'il est atteignable)
        if isinstance(dico[cle][0], int):
        # Si le sommet n'est pas encore traité et que sa distance est inférieure à la distance minimale actuelle
            if cle not in sommets_colors and dico[cle][0] < mini:
                mini = dico[cle][0] # Mettre à jour la distance minimale et le sommet correspondant
                sommet = cle
               
    return sommet # Retourner le sommet avec la distance minimale
    
    
###############################################################################
##                                 TEST                                      ##
##  Entrée : une matrice de distances (matrice), un dictionnaire des         ##
##  distances (dico), et deux sommets (i, j)                                 ##
##  Retourne vrai si la distance pour atteindre j via i est plus courte que  ##
##  la distance actuelle à j                                                 ##
###############################################################################
def test(matrice, dico, i, j):
    return dico[i][0] + matrice[i][j] < dico[j][0] # Retourne vrai si la distance pour atteindre j via i est plus courte que la distance actuelle à j


###############################################################################
##                          CHEMIN_PLUS_COURT                                ##
##  Entrée : une matrice de distances (matrice), un sommet de départ et un   ##
##  sommet d'arrivée                                                         ##
##  Retourne la distance et le chemin le plus court pour aller de depart à   ##
##  arrivee                                                                  ##
###############################################################################
def chemin_plus_court(matrice, depart, arrivee):
    # Appliquer l'algorithme de Dijkstra pour obtenir les distances et les prédecesseurs
    dico = djikstra(matrice, depart)
    chemin = []
    sommet_courant = arrivee
    # Initialiser la liste pour stocker le chemin
    while sommet_courant != depart:
        chemin.append(sommet_courant)
        sommet_courant = dico[sommet_courant][1]
    
    chemin.append(depart)
    return dico[arrivee][0], chemin[::-1]











###############################################################################
##                                  TESTS                                    ##
###############################################################################
def test_dijkstra(): ## teste l'algorithme de djikstra
    inf = float('inf')

    M = [
        [inf, 86, inf, 34, inf, 134],
        [86, inf, 93, inf, inf, inf],
        [inf, 93, inf, 47, 56, inf],
        [34, inf, 47, inf, inf, inf],
        [inf, inf, 56, inf, inf, 62],
        [134, inf, inf, inf, 62, inf]
    ]

    result = djikstra(M, 0)
    print("Résultat du test Dijkstra à partir du nœud 0:")
    for noeud, (distance, predecesseur) in result.items():
        print(f"  Nœud {noeud}: Distance = {distance}, Prédécesseur = {predecesseur}")

def test_chemin_plus_court(): ## test chemin le plus cours
    inf = float('inf')

    M = [
        [inf, 4, 6, inf, 8, inf, inf, inf],
        [inf, inf, 1, inf, 2, inf, inf, inf],
        [inf, inf, inf, 4, inf, 4, 6, inf],
        [inf, inf, inf, inf, inf, inf, 3, inf],
        [inf, inf, inf, inf, inf, 1, inf, inf],
        [inf, 2, inf, 4, 1, 2, 2, inf],
        [inf, inf, inf, inf, inf, inf, inf, inf],
        [inf, inf, inf, 3, inf, inf, 2, inf]
    ]

    distance, chemin = chemin_plus_court(M, 0, 5)
    print("\nChemin le plus court du nœud 0 au nœud 5:")
    print(f"  Distance: {distance}")
    print(f"  Chemin: {' -> '.join(map(str, chemin))}")

# Exécuter les tests
test_dijkstra()
test_chemin_plus_court()

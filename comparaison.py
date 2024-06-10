# -*- coding: utf-8 -*-

import Djikstra as dj
import BelmanFort as bf
import generateurMatrice as gm
import time as time
import numpy as np
import matplotlib.pyplot as plt

###############################################################################
##                              TEMPSDIJ                                     ##
##  Entrée : un entier n représentant la taille de la matrice                ##
##  Retourne le temps de calcul de l'algorithme de Dijkstra                  ##
###############################################################################
def TempsDij(n):
    M = gm.graphe(n, 0, 3)
    debut = time.perf_counter()
    dj.djikstra(M, 0)
    fin = time.perf_counter()
    
    return fin - debut

###############################################################################
##                              TEMPSBF                                      ##
##  Entrée : un entier n représentant la taille de la matrice                ##
##  Retourne le temps de calcul de l'algorithme de Bellman-Ford              ##
###############################################################################
def TempsBf(n):
    M = gm.graphe(n, 0, 3)
    debut = time.perf_counter()
    bf.bellman_ford_largeur(M, 0)
    fin = time.perf_counter()
    
    return fin - debut

###############################################################################
##                             COMPARAISON                                   ##
##  Entrée : un entier n représentant la taille de matrice jusqu'à laquelle  ##
##  on calcule                                                               ##
##  Affiche un graphique avec les temps de calcul des deux algos en fonction ##
##  de la taille de la matrice                                               ##
###############################################################################
def comparaison(n):
    dij = []
    bef = []
    
    for i in range(2, n):
        M = gm.graphe(i, 0, 3)
        
        # Mesurer le temps pour l'algorithme de Dijkstra
        debut = time.perf_counter()
        dj.djikstra(M, 0)
        fin = time.perf_counter()
        dij.append(fin - debut)
        
        # Mesurer le temps pour l'algorithme de Bellman-Ford
        debut = time.perf_counter()
        bf.bellman_ford_largeur(M, 0)
        fin = time.perf_counter()
        bef.append(fin - debut)
    
    X = np.arange(2, n, 1)
    plt.plot(X, dij, "r", label="Dijkstra")
    plt.plot(X, bef, "b", label="Bellman-Ford")
    plt.legend()
    plt.xlabel("Taille de la matrice")
    plt.ylabel("Temps de calcul (secondes)")
    plt.title("Comparaison des temps de calcul de Dijkstra et Bellman-Ford")
    plt.show()

comparaison(200)
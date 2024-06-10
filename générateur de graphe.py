# -*- coding: utf-8 -*-
"""
Created on Mon May 10 09:40:02 2024

@author: Matéo, Lionel, Hugo, Fatoumata 
"""

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import Djikstra as dj
import BelmanFort as bl

###############################################################################
##                        TRACER_DIJKSTRA                                    ##
##  Entrée : une matrice de distances (matrice), un sommet de départ (debut) ##
##  et un sommet de fin (fin)                                                ##
##  Retourne et trace le graphe avec le plus court chemin en rouge           ##
###############################################################################
def tracer_dijkstra(matrice, debut, fin):
    shortest_path = dj.chemin_plus_court(matrice, debut, fin)[1]
    return tracer(matrice, shortest_path)

###############################################################################
##                        TRACER_BELLMAN_FORD                                ##
##  Entrée : une matrice de distances (matrice), un sommet de départ (debut) ##
##  et un sommet de fin (fin)                                                ##
##  Retourne et trace le graphe avec le plus court chemin en rouge           ##
###############################################################################
def tracer_Bellman_Ford(matrice, debut, fin):
    shortest_path = bl.chemin_plus_court(matrice, debut, fin)[1]
    return tracer(matrice, shortest_path)

###############################################################################
##                                TRACER                                     ##
##  Entrée : une matrice de distances (matrice) et une liste de sommets      ##
##  (shortest_path)                                                          ##
##  Permet de tracer le graphe et de mettre en rouge les sommets du plus     ##
##  court chemin                                                             ##
###############################################################################
def tracer(matrice, shortest_path):
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if matrice[i][j] == np.inf:
                matrice[i][j] = 0
                
    matrice = np.array(matrice)
    
    G = nx.DiGraph(matrice)
    # dessiner le graphe avec des poids d'arêtes
    pos = nx.spring_layout(G)  # positionnement des sommets
    labels = nx.get_edge_attributes(G, "weight")  # récupérer les poids des arêtes
    nx.draw_networkx_nodes(G, pos, node_size=500)
    nx.draw_networkx_edges(G, pos, width=2, alpha=0.5)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=10, font_color="red")  # affiche le poids des arêtes
    nx.draw_networkx_labels(G, pos, font_size=16, font_family="sans-serif")  # affiche le nom des sommets
    nx.draw_networkx_nodes(G, pos, nodelist=shortest_path, node_color='red')  # met les sommets en rouge
    plt.axis("off")
    plt.show()

###############################################################################
##                        TEST_TRACE_DIJKSTRA                                ##
##  Entrée : aucune                                                          ##
##  Teste et trace le plus court chemin avec l'algorithme de Dijkstra sur    ##
##  un exemple de matrice                                                    ##
###############################################################################
def test_trace_dijkstra():
    matrice = [[np.inf, 86, np.inf, 34, np.inf, 134],
               [86, np.inf, 93, np.inf, np.inf, np.inf],
               [np.inf, 93, np.inf, 47, 56, np.inf],
               [34, np.inf, 47, np.inf, np.inf, np.inf],
               [np.inf, np.inf, 56, np.inf, np.inf, 62],
               [134, np.inf, np.inf, np.inf, 62, np.inf]]

    tracer_dijkstra(matrice, 1, 5)

###############################################################################
##                      TEST_TRACE_BELLMAN_FORD                              ##
##  Entrée : aucune                                                          ##
##  Teste et trace le plus court chemin avec l'algorithme de Bellman-Ford sur##
##  un exemple de matrice                                                    ##
###############################################################################
def test_trace_Bellman_Ford():
    matrice = [[np.inf, 86, np.inf, 34, np.inf, 134],
               [86, np.inf, 93, np.inf, np.inf, np.inf],
               [np.inf, 93, np.inf, 47, 56, np.inf],
               [34, np.inf, 47, np.inf, np.inf, np.inf],
               [np.inf, np.inf, 56, np.inf, np.inf, 62],
               [134, np.inf, np.inf, np.inf, 62, np.inf]]

    tracer_Bellman_Ford(matrice, 1, 5)
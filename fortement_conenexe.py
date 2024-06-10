<# -*- coding: utf-8 -*-
"""
Created on Mon May 10 09:40:02 2024

@author: Matéo, Lionel, Hugo, Fatoumata 
"""

import random
import matplotlib.pyplot as plt

###############################################################################
##                                  FC                                       ##
##  Entrée : une matrice M                                                   ##
##  Retourne True si le graphe associé à la matrice M est fortement connexe  ##
##  sinon False                                                              ##
###############################################################################
def fc(M):
    M = Roy_Warshall(M)
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j] == 0:
                return False
    return True

###############################################################################
##                              ROY_WARSHALL                                 ##
##  Entrée : une matrice M                                                   ##
##  Retourne la matrice M avec toutes les fermetures transitives             ##
###############################################################################
def Roy_Warshall(M):
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j] == 1:
                for k in range(len(M[i])):
                    if M[j][k] == 1:
                        M[i][k] = 1
    return M

###############################################################################
##                            TEST_STAT_FC                                   ##
##  Entrée : un entier n qui est la taille des matrices                      ##
##  Retourne le nombre de graphes associés aux matrices de taille n qui sont ##
##  fortement connexes                                                       ##
###############################################################################
def test_stat_fc(n):
    nb = 0
    for i in range(100):
        M = graphe(n, 0.5)
        if fc(M):
            nb += 1
    return nb

###############################################################################
##                           TEST_STAT_FC2                                   ##
##  Entrée : un entier n qui est la taille des matrices et p qui est la      ##
##  proportion de 1 dans la matrice                                          ##
##  Retourne le nombre de graphes associés aux matrices de taille n qui sont ##
##  fortement connexes                                                       ##
###############################################################################
def test_stat_fc2(n, p):
    nb = 0
    for i in range(100):
        M = graphe(n, p)
        if fc(M):
            nb += 1
    return nb

###############################################################################
##                                GRAPHE                                     ##
##  Entrée : un entier n qui est la taille des matrices et p qui est la      ##
##  proportion de 1 dans la matrice                                          ##
##  Retourne une matrice de taille n et de proportion de 1 p                 ##
###############################################################################
def graphe(n, p):
    M = []
    cpt = 0
    for i in range(n * n):
        if cpt < n * n * p:
            M.append(1)
            cpt += 1
        else:
            M.append(0)
    random.shuffle(M)
    matrice = []
    for i in range(n):
        l = []
        for j in range(n):
            l.append(M.pop(0))
        matrice.append(l)
    return matrice

###############################################################################
##                                SEUIL                                      ##
##  Entrée : un entier n qui est la taille des matrices                      ##
##  Retourne le pourcentage du seuil                                         ##
###############################################################################
def seuil(n):
    p = 1
    while p * 100 <= test_stat_fc2(n, p):
        p -= 1 / 100
    return p * 100

###############################################################################
##                            AFFICHER_GRAPHE                                ##
##  Affiche le graphe du seuil en fonction de la taille de la matrice        ##
##  PS : Il met du temps à se réaliser                                       ##
###############################################################################
def afficher_graphe():
    X = []
    Y = []
    for i in range(10, 41, 1):
        X.append(i)
        Y.append(seuil(i))
    plt.plot(X, Y)

################################################################################
##                           AFFICHER_GRAPHE2                                 ##
##  Affiche le graphe log-log du seuil en fonction de la taille de la matrice ##
##  PS : Il met du temps à se réaliser                                        ##
################################################################################
def afficher_graphe2():
    X = []
    Y = []
    for i in range(10, 41, 1):
        X.append(i)
        Y.append(seuil(i))
    plt.loglog(X, Y)

# Exemple de matrices pour les tests
matrice = [[0, 1, 0, 0, 0],
           [0, 0, 1, 0, 0],
           [0, 0, 0, 0, 1],
           [0, 0, 0, 1, 0],
           [0, 1, 0, 0, 0]]

M = [[0, 1, 0, 1],
     [0, 0, 1, 0],
     [0, 1, 0, 0],
     [0, 0, 1, 0]]

print(fc(matrice))
print(fc(M))
print("Taille de matrice : 19 = ", test_stat_fc(19), "%")

print(str(seuil(15)) + '%')  # Pour n = 15, le seuil est de 32%
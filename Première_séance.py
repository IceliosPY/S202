# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 15:35:40 2023

@author: romain
"""

import numpy as np
import random
import time
import matplotlib.pyplot as plt

###############################################################################
##                                TRANS1                                     ##
##  Entrée : une matrice M                                                   ##
##  Retourne la matrice M après avoir ajouté des liens transitifs            ##
###############################################################################
def trans1(M):
    n = len(M)
    matrice = M.copy()
    for i in range(2, n+1):
        P = np.dot(M, matrice)
        matrice += red(P)
    return red(matrice)

###############################################################################
##                                RED                                        ##
##  Entrée : une matrice M                                                   ##
##  Retourne la matrice M avec toutes les valeurs supérieures à 1 réduites à ##
##  1                                                                        ##
###############################################################################
def red(M):
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j] > 1:
                M[i][j] = 1
    return M

###############################################################################
##                                TEMPS                                      ##
##  Entrée : un entier n représentant la taille de la matrice                ##
##  Retourne le temps d'exécution de la fonction trans1 sur une matrice      ##
##  aléatoire de taille n                                                    ##
###############################################################################
def temps(n):
    M = []
    for i in range(n):
        l = []
        for j in range(n):
            l.append(random.randint(0, 1))
        M.append(l)

    start = time.perf_counter()
    trans1(M)
    stop = time.perf_counter()
    
    return stop - start

'''
Affichage des résultats
'''
tmp = []
X = []

for i in range(10, 200):
    X.append(i)
    tmp.append(temps(i))

plt.loglog(X, tmp)

print((np.log(temps(500)) - np.log(temps(450))) / (np.log(500) - np.log(450)))

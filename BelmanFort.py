import numpy as np
import generateurMatrice as gm
import random
import matplotlib.pyplot as plt

##########################################################################################################################
##                          BELLMAN_FORD_ALEATOIRE                                                                      ##
##                                                                                                                      ##
##Entrée : une matrice M et un sommet de départ depart                                                                  ##
##Retourne un dictionnaire dico réalisant le parcours de Bellman-Ford avec un ordre des sommets aléatoire               ##
##                                                                                                                      ##                                    
###########################################################################################################################

def bellman_ford_aleatoire(M, depart):
    # Initialiser les distances et les prédecesseurs avec la fonction initialisation
    dico = initialisation(M, depart)
    # Variable pour suivre si une modification a été faite lors d'une itération
    modif = True
    # Compteur pour le nombre d'itérations
    nbOccurence = 1
    
    
    # Générer un parcours aléatoire des arêtes du graphe
    listTest = parcours_aleatoire(M)  # Générer un parcours aléatoire
    
    
    # Répéter jusqu'à ce qu'aucune modification ne soit faite ou jusqu'à atteindre le nombre maximal d'itérations
    while modif and nbOccurence < len(M):
        modif = False # Réinitialiser la variable de modification
        # Parcourir chaque paire (i, j) dans le parcours aléatoire
        for (i, j) in listTest:
        # Vérifier si une distance plus courte est trouvée via le sommet i
            if test(M, dico, i, j): 
                dico[j][0] = dico[i][0] + M[i][j]   # Mettre à jour la distance et le prédecesseur du sommet j
                dico[j][1] = i
                modif = True  # Indiquer qu'une modification a été faite
        nbOccurence += 1 # Incrémenter le compteur d'itérations
    
    return dico, nbOccurence # Retourner le dictionnaire des distances et prédecesseurs ainsi que le nombre d'itérations effectuées

#############################################################################################################################
##                          BELLMAN_FORD_LARGEUR                                                                           ##
##Entrée : une matrice M et un sommet de départ depart                                                                     ##
##Retourne un dictionnaire dico réalisant le parcours de Bellman-Ford avec un ordre des sommets d'un parcours largeur      ##
##                                                                                                                         ##                                     
#############################################################################################################################



def bellman_ford_largeur(M, depart):
    # Initialiser les distances et les prédecesseurs avec la fonction initialisation
    dico = initialisation(M, depart)
    # Variable pour suivre si une modification a été faite lors d'une itération
    modif = True
    # Compteur pour le nombre d'itérations
    nbOccurence = 1
    
    # Générer un parcours en largeur à partir du sommet de départ
    listTest = parcours_largeur(M, depart)
    
    # Répéter jusqu'à ce qu'aucune modification ne soit faite ou jusqu'à atteindre le nombre maximal d'itérations
    while modif and nbOccurence < len(M):
        modif = False  # Réinitialiser la variable de modification
        # Parcourir chaque paire (i, j) dans le parcours en largeur
        for (i, j) in listTest:
            # Vérifier si une distance plus courte est trouvée via le sommet i
            if test(M, dico, i, j):
                # Mettre à jour la distance et le prédecesseur du sommet j
                dico[j][0] = dico[i][0] + M[i][j]
                dico[j][1] = i
                # Indiquer qu'une modification a été faite
                modif = True
        # Incrémenter le compteur d'itérations
        nbOccurence += 1
    
    # Retourner le dictionnaire des distances et prédecesseurs ainsi que le nombre d'itérations effectuées
    return dico, nbOccurence
    
    
###########################################################################################################################
##                         BELLMAN_FORD_PROFONDEUR                                                                       ##
##Entrée : une matrice M et un sommet de départ depart                                                                   ##                                 
##Retourne un dictionnaire dico réalisant le parcours de Bellman-Ford avec un ordre des sommets d'un parcours profondeur ##
###########################################################################################################################


def bellman_ford_profondeur(M, depart):
    # Initialiser les distances et les prédecesseurs avec la fonction initialisation
    dico = initialisation(M, depart)
    # Variable pour suivre si une modification a été faite lors d'une itération
    modif = True
    # Compteur pour le nombre d'itérations
    nbOccurence = 1
    
    # Générer un parcours en profondeur à partir du sommet de départ
    listTest = parcours_profondeur(M, depart)
    
    # Répéter jusqu'à ce qu'aucune modification ne soit faite ou jusqu'à atteindre le nombre maximal d'itérations
    while modif and nbOccurence < len(M):
        modif = False  # Réinitialiser la variable de modification
        # Parcourir chaque paire (i, j) dans le parcours en profondeur
        for (i, j) in listTest:
            # Vérifier si une distance plus courte est trouvée via le sommet i
            if test(M, dico, i, j):
                # Mettre à jour la distance et le prédecesseur du sommet j
                dico[j][0] = dico[i][0] + M[i][j]
                dico[j][1] = i
                # Indiquer qu'une modification a été faite
                modif = True
        # Incrémenter le compteur d'itérations
        nbOccurence += 1
    
    # Retourner le dictionnaire des distances et prédecesseurs ainsi que le nombre d'itérations effectuées
    return dico, nbOccurence


###########################################################################################
##                             INITIALISATION                                            ##
##                             Entrée : une matrice M et un sommet de départ d           ##
##  Retourne un dico qui permet de faire l'initialisation du parcours de Bellman-Ford    ## 
##                                                                                       ## 
###########################################################################################

def initialisation(M, d):
    import numpy as np  # Importer numpy pour utiliser np.inf
    # Initialiser un dictionnaire pour stocker les distances et les prédecesseurs
    dico = {}
    
    # Parcourir chaque sommet dans le graphe
    for i in range(len(M[0])):
        if i == d:
            # Pour le sommet de départ, la distance à lui-même est 0 et son prédecesseur est lui-même
            dico[i] = [0, d]
        else:
            # Pour les autres sommets, initialiser la distance à l'infini et le prédecesseur à None
            dico[i] = [np.inf, None]
    
    # Retourner le dictionnaire des distances et prédecesseurs
    return dico

###############################################################################
##                                 TEST                                      ##
###############################################################################

def test(M, dico, i, j):
    # Vérifie si la distance pour atteindre j via i est plus courte que la distance actuelle pour j
    return dico[i][0] + M[i][j] < dico[j][0]
    
    
###############################################################################
##                          PARCOURS_ALEATOIRE                               ##
##                          Entrée : une Matrice M                           ##
##  Retourne une liste des sommets de la matrice M dans un ordre aléatoire   ##
##                                                                           ##
###############################################################################
import random
def parcours_aleatoire(M):
    # Initialiser une liste pour stocker les sommets
    sommet = []
    
    # Générer un ordre aléatoire des sommets
    while len(sommet) < len(M):
        # Choisir un sommet aléatoire
        alea = random.randint(0, len(M) - 1)
        # Ajouter le sommet à la liste s'il n'est pas déjà présent
        if alea not in sommet:
            sommet.append(alea)
    
    # Créer une liste de paires (i, j) pour les arêtes à partir de l'ordre des sommets
    return creerTest(M, sommet)
    
    
###############################################################################
##                          PARCOURS_LARGEUR                                 ##
##  Entrée : une Matrice M                                                   ##
##  Retourne une liste des sommets de la matrice M dans l'ordre du parcours  ##
##  en largeur                                                               ##
###############################################################################

def parcours_largeur(M, depart):
    # Initialiser une liste pour stocker les sommets dans l'ordre du parcours en largeur
    sommet = []
    # Initialiser une liste avec le sommet de départ pour gérer les sommets à visiter
    listCourant = [depart]
    
    # Parcourir les sommets jusqu'à ce que la liste des sommets à visiter soit vide
    while len(listCourant) > 0:
        # Retirer le premier sommet de la liste des sommets à visiter
        courant = listCourant.pop(0)
        # Ajouter ce sommet à la liste des sommets visités
        sommet.append(courant)
        
        # Parcourir les voisins du sommet actuel
        for i in range(len(M[courant])):
            # Vérifier s'il existe une arête entre le sommet courant et le sommet i
            # et que ce sommet n'est pas déjà dans les listes des sommets à visiter ou visités
            if isinstance(M[courant][i], int) and i not in listCourant and i not in sommet:
                # Ajouter le sommet voisin à la liste des sommets à visiter
                listCourant.append(i)
    
    # Créer une liste de paires (i, j) pour les arêtes à partir de l'ordre des sommets visités
    return creerTest(M, sommet)
    
    
###############################################################################
##                          PARCOURS_PROFONDEUR                              ##
##  Entrée : une Matrice M                                                   ##
##  Retourne une liste des sommets de la matrice M dans l'ordre du parcours  ##
##  en profondeur                                                            ##
###############################################################################

def parcours_profondeur(M, depart):
    """
    Entrée : une Matrice M
    Retourne une liste des sommets de la matrice M dans l'ordre du parcours en profondeur
    """
    # Initialiser une liste pour stocker les sommets dans l'ordre du parcours en profondeur
    sommet = []
    # Initialiser une liste avec le sommet de départ pour gérer les sommets à visiter
    listCourant = [depart]
    
    # Parcourir les sommets jusqu'à ce que la liste des sommets à visiter soit vide
    while len(listCourant) > 0:
        # Retirer le dernier sommet de la liste des sommets à visiter (profondeur)
        courant = listCourant.pop()
        # Ajouter ce sommet à la liste des sommets visités
        sommet.append(courant)
        
        # Parcourir les voisins du sommet actuel en ordre inverse
        for i in range(len(M[courant]), 0, -1):
            i = i - 1  # Ajuster l'indice car range est exclusif à la fin
            # Vérifier s'il existe une arête entre le sommet courant et le sommet i
            # et que ce sommet n'est pas déjà dans les listes des sommets à visiter ou visités
            if isinstance(M[courant][i], int) and i not in listCourant and i not in sommet:
                # Ajouter le sommet voisin à la liste des sommets à visiter
                listCourant.append(i)
    
    # Créer une liste de paires (i, j) pour les arêtes à partir de l'ordre des sommets visités
    return creerTest(M, sommet)

###############################################################################
##                              CREER_TEST                                   ##
##  Entrée : une matrice M et une liste de sommets liste                     ##
##  Retourne une liste contenant tous les tests à réaliser dans l'algorithme ##
###############################################################################

def creerTest(M, liste):
    """
    Entrée : une matrice M et une liste de sommets liste
    Retourne une liste contenant tous les tests à réaliser dans l'algorithme
    """
    # Initialiser une liste pour stocker les paires (i, j) représentant les tests à réaliser
    testListe = []
    
    # Parcourir chaque sommet dans la liste fournie
    for i in range(len(liste)):
        # Parcourir chaque voisin du sommet actuel
        for j in range(len(M[liste[i]])):
            # Vérifier s'il existe une arête entre le sommet actuel et le voisin j
            if isinstance(M[liste[i]][j], int):
                # Ajouter la paire (i, j) à la liste des tests à réaliser
                testListe.append([liste[i], j])
    
    # Retourner la liste des tests
    return testListe

#####################################################################################
##                          CHEMIN_PLUS_COURT                                      ##
##  Entrée : une matrice M, et deux indices depart et arrivee qui représentent     ##
##  le sommet de départ et d'arrivée                                               ##
##  Retourne la taille et le chemin le plus court pour aller de depart à arrivee   ##
#####################################################################################

def chemin_plus_court(M, depart, arrivee):
    """
    Entrée : une matrice M, et deux indices depart et arrivee qui représentent le sommet de départ et d'arrivée
    Retourne la taille et le chemin le plus court pour aller de depart à arrivee
    """
    # Appliquer l'algorithme de Bellman-Ford avec parcours en largeur pour obtenir les distances et prédecesseurs
    dico = bellman_ford_largeur(M, depart)[0]
    
    # Initialiser une liste pour stocker le chemin le plus court
    listSommet = []
    # Initialiser le sommet courant à l'arrivée
    sommetCourant = arrivee
    
    # Tracer le chemin de l'arrivée au départ en utilisant les prédecesseurs
    while sommetCourant != depart:
        listSommet.append(sommetCourant)
        sommetCourant = dico[sommetCourant][1]
    
    # Ajouter le sommet de départ à la fin du chemin
    listSommet.append(depart)
    
    # Retourner la distance totale et le chemin inversé (du départ à l'arrivée)
    return dico[arrivee][0], listSommet[::-1]


################################################################################
##                                  TESTS                                     ##
################################################################################

def test_Bellman_Ford(): ## test pour belmonford 
    M = [
        [np.inf, 3, np.inf, np.inf, np.inf, np.inf],
        [np.inf, np.inf, 4, np.inf, 2, 1],
        [np.inf, -1, np.inf, np.inf, np.inf, np.inf],
        [2, np.inf, np.inf, np.inf, 8, np.inf],
        [np.inf, np.inf, np.inf, np.inf, np.inf, 9],
        [np.inf, np.inf, np.inf, np.inf, -3, np.inf]
    ]
    
    distance, chemin = chemin_plus_court(M, 0, 5)
    print("Chemin le plus court du nœud 0 au nœud 5 avec Bellman-Ford:")
    print(f"  Distance: {distance}")
    print(f"  Chemin: {' -> '.join(map(str, chemin))}")

def graphe(): ## compare chacuns des parcours 
    X = []
    alea = []
    lar = []
    prof = []
    for i in range(20):
        M = gm.graphe(50, 0, 5)
        X.append(i)
        alea.append(bellman_ford_aleatoire(M, 3)[1])
        lar.append(bellman_ford_largeur(M, 3)[1])
        prof.append(bellman_ford_profondeur(M, 3)[1])
    
    axes = plt.gca()
    axes.set_xlim(0, 20)
    axes.set_yticks([0, 10], minor=True)
    plt.plot(X, alea, 'b', label="Parcours Aléatoire")
    plt.plot(X, lar, 'r', label="Parcours Largeur")
    plt.plot(X, prof, 'g', label="Parcours Profondeur")
    
    plt.legend()
    plt.show()

# Exécuter les tests
test_Bellman_Ford()
graphe()

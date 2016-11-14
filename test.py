import random

k = 3
graphe = {}
ss = [[] for i in range(k)]

with open("fichier.graph", "r") as fichier:
    i = 0
    for line in fichier:
        if i == 0:
            nbNodes, nbEdges = [int(j) for j in line.split()]
        else:
            graphe[i] = [int(j) for j in line.split()]
        i += 1

liste_noeuds_non_utilises = [i + 1 for i in range(nbNodes)]
liste_voisins = [[] for x in range(k)

for s in enumerate(ss):
    i = random.choice(liste_noeuds_non_utilises)
    s.append(i)

    liste_noeuds_non_utilises.remove(i)






import random

k = 3
graphe = {}
ss = [[] for i in range(k)]

with open("graphes/fichier.graph", "r") as fichier:
    i = 0
    for line in fichier:
        if i == 0:
            nbNodes, nbEdges = [int(j) for j in line.split()]
        else:
            graphe[i] = [int(j) for j in line.split()]
        i += 1

liste_noeuds_non_utilises = [i + 1 for i in range(nbNodes)]

liste_voisins = []

for j in range(k):
    i = random.choice(liste_noeuds_non_utilises)
    ss[j].append(i)
    liste_voisins.extend([j for j in graphe[i] if j not in liste_voisins and j in liste_noeuds_non_utilises])
    liste_noeuds_non_utilises.remove(i)

while len(liste_noeuds_non_utilises) > 0:
    if len(liste_voisins) > 0:
        i = random.choice(liste_voisins)
        liste_voisins.remove(i)
    else:
        i = random.choice(liste_noeuds_non_utilises)

    liste_noeuds_non_utilises.remove(i)
    count = [len([j for j in graphe[i] if j in s]) for s in ss]
    s = count.index(max(count))
    ss[s].append(i)
    liste_voisins.extend([j for j in graphe[i] if j not in liste_voisins and j in liste_noeuds_non_utilises])


for s in ss:
    poids = 0
    cut = 0
    for i in s:
        for j in graphe[i]:
            if j in s:
                poids += 0.5
            else:
                cut += 1
    ratio = cut / poids
    print ratio


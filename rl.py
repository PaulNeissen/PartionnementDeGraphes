import random

import time
import sys

k = 3
graphe = {}
ss = [[] for i in range(k)]
file_name = "../bz/3elt.graph"


print "Loading " + file_name + "... "

with open(file_name, "r") as fichier:
    i = 0
    for line in fichier:
        if i == 0:
            nbNodes, nbEdges = [int(j) for j in line.split()]
        else:
            graphe[i] = [int(j) for j in line.split()]
        i += 1

liste_noeuds_non_utilises = [i + 1 for i in range(nbNodes)]

liste_voisins = []



print "Initialization... "

for j in range(k):
    i = random.choice(liste_noeuds_non_utilises)
    ss[j].append(i)
    liste_voisins.extend([j for j in graphe[i] if j not in liste_voisins and j in liste_noeuds_non_utilises])
    liste_noeuds_non_utilises.remove(i)


print "Add nodes in cluster... "

loading_tool = len(liste_noeuds_non_utilises)/40
it = 0

while len(liste_noeuds_non_utilises) > 0:
    if it % loading_tool == 0:
        sys.stdout.write("-")
        sys.stdout.flush()
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
    it += 1
sys.stdout.write("\n")
sys.stdout.flush()

print "Ratio Calcul... "

sum_ratio = 0.0
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
    sum_ratio += ratio

print "Sum_ratio : " + str(sum_ratio)


print "\nRecherche Locale : \n"
for index,s in enumerate(ss):
	print s 
	print "\n"
	for i in s:
		for j in graphe[i]:
			if j not in s








	



	


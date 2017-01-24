import random
from pprint import pprint
import time
import sys

start_time = time.time()

k = 3
graphe = {}
ss = [[] for i in range(k)]
ss_inverse = {}
file_name = "./petit.graph"
#file_name = "../bz/fichier.graph"


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
    ss_inverse[i] = j
    liste_voisins.extend([j for j in graphe[i] if j not in liste_voisins and j in liste_noeuds_non_utilises])
    liste_noeuds_non_utilises.remove(i)
    if i in liste_voisins:
        liste_voisins.remove(i)


print "Add nodes in cluster... "

loading_tool = float(len(liste_noeuds_non_utilises)) / 100
it = 0
while len(liste_noeuds_non_utilises) > 0:
    
    sys.stdout.write("  %d %% \r" % int(it / loading_tool))
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
    ss_inverse[i] = s
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

print "Sum_ratio : " + str(sum_ratio) + "\n"


meilleur = {"numero":-1, "ratio": sum_ratio, "ss":0}
continuer = True
while continuer:
    Trouve = False
    liste_bords = []
    for index,s in enumerate(ss):
        for i in s:
            border = False
            for j in graphe[i]:
                if j not in s:
                    border = True
                    liste_bords.append({"numero":i, "ss":ss_inverse[j]})
                    break

    nombre_total = len(liste_bords)
    it = 0
    for au_bord in liste_bords:
        it += 1
        
        sys.stdout.write("  %f %% \r" % (float(it) / nombre_total * 100))
        sys.stdout.flush()

        numero = au_bord["numero"]
        ss_destination = au_bord["ss"]

        ss_origine = ss_inverse[numero]
        ss[ss_origine].remove(numero)
        ss[ss_destination].append(numero)
        ss_inverse[numero] = ss_destination

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
            sum_ratio += ratio
		
        if sum_ratio < meilleur["ratio"]:
            meilleur["ratio"] = sum_ratio
            meilleur["numero"] = numero
            meilleur["ss"] = ss_destination
            Trouve = True

        ss[ss_destination].remove(numero)
        ss[ss_origine].append(numero)
        ss_inverse[numero] = ss_origine

    print "Meilleur ratio : %f" % meilleur["ratio"]

    if not(Trouve):
        continuer = False
    else:
        numero = meilleur["numero"]
        ss_destination = meilleur["ss"]
        ss_origine = ss_inverse[numero]
        ss[ss_origine].remove(numero)
        ss[ss_destination].append(numero)
        ss_inverse[numero] = ss_destination

print "\nSolution finale :\n----------------"

print ss

print("\n--- %s seconds ---" % (time.time() - start_time))

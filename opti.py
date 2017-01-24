from gurobipy import *
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

with open(file_name, "r") as fichier:
    i = 0
    for line in fichier:
        if i == 0:
            nbNodes, nbEdges = [int(j) for j in line.split()]
        else:
            graphe[i] = [int(j) for j in line.split()]
        i += 1

variables = [[False for j in range(nbNodes)] for i in range(k)]


model = Model ()

x = model.addVar(obj=3000, vtype="C", name="x")
y = model.addVar(obj=4000, vtype="C", name="y")
model.update()

L2 = LinExpr([7,5], [x,y])
model.addConstr(L2, ">", 5)

model.ModelSense = 1
model.optimize()

if model.Status == GRB.OPTIMAL:
	print 'Opt. Value =', model.ObjVal
	print 'x^*, y^* =', x.X, y.X

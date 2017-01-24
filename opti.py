from gurobipy import *
import random
from pprint import pprint
import time
import sys


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

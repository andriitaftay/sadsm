
from gurobipy import *

p = [3,4,5,2,8,7,9]
w = [5,8,3,1,9,11,20]
C = 15

m = Model("Problem 2: Knapsack")

x = m.addVars(len(p), vtype=GRB.BINARY)

m.setObjective(quicksum(p[i]*x[i] for i in range(len(x))), GRB.MAXIMIZE)

m.addConstr(quicksum(w[i]*x[i] for i in range(len(x))) <= C)

m.optimize()

for a in m.getVars():
    print(a.varName, a.X)
print(f"Result: {m.objVal}")
print(f"Capacity = {C}")
used = sum(w[i]*int(x[i]) for i in range(len(x)))
print(f"UsedCapacity = {used}")


from gurobipy import *

p = [3,4,5,2,8,7,9]
p2 = sum(p)*0.5
m = Model("Problem 1")

x = m.addVars(len(p), vtype=GRB.BINARY)

m.setObjective(p2 - quicksum(p[i]*x[i] for i in range(len(x))), GRB.MINIMIZE)

m.addConstr(p2 - quicksum(p[i]*x[i] for i in range(len(x))) >=0)

m.optimize()

for a in m.getVars():
    print(a.varName, a.X)
print(f"Result: {m.objVal}")
print(f"Sum/2 = {p2}")

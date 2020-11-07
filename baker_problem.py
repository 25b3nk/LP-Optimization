import pulp

model = pulp.LpProblem("Maximize Bakery profits for thirty days", sense=pulp.LpMaximize)
cakeA = pulp.LpVariable("cakeA", lowBound=0, cat=pulp.LpInteger)
cakeB = pulp.LpVariable("cakeB", lowBound=0, cat=pulp.LpInteger)

# Profits :: Cake A : 20  Cake B : 40
model += 20 * cakeA + 40 * cakeB

# Oven usage :: Cake A : 0.5 day  Cake B : 1 day :: Number of ovens : 1
model += 0.5 * cakeA + cakeB <= 30

# Personnel usage :: Cake A : 1 day  Cake B : 2.5 days :: Number of persons : 2
# Since there are two bakers, the limit would be 30 days x 2 = 60
model += cakeA + 2.5 * cakeB <= 60

# Packaging units usage :: Cake A : 1 day  Cake B : 2 day :: Number of units : 1 unit for 22 days
model += cakeA + 2 * cakeB <= 22

model.solve()

print("Number of Cake A to be baked: {}".format(cakeA.varValue))
print("Number of Cake B to be baked: {}".format(cakeB.varValue))

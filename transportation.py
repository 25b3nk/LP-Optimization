'''
Link to the problem:
https://coin-or.github.io/pulp/CaseStudies/a_transportation_problem.html
'''

import pulp
import json

# Ingredient wise price and other nutritional facts
data = json.load(open('transportation.json'))

# Names of warehouses and bars
warehouses = ["A", "B"]
bars = ["1", "2", "3", "4", "5"]

variable_dict = {}
sum_list = []

# Initialize the problem
prob = pulp.LpProblem(name="Beer transportation problem", sense=pulp.LpMinimize)

# Creates a list of costs of each transportation path
costs = [   #Bars
         #1 2 3 4 5
         [2,4,5,2,1],#A   Warehouses
         [3,1,3,2,3] #B
         ]

# Create varaiables for each route, example: Beer transported from warehouse 'A' to Bar '1' would be 'A1'
# Also create sum list of cost of the route per crate multiplied with the route variable
for i, w in enumerate(warehouses):
    for j, b in enumerate(bars):
        var = w + b
        variable_dict[var] = pulp.LpVariable(var, lowBound=0, cat=pulp.LpInteger)
        sum_list.append(costs[i][j] * variable_dict[var])
prob += pulp.lpSum(sum_list)

# Setting the maimum limit for number of crates for each warehouse
for w in warehouses:
    prob += pulp.lpSum([variable_dict[w + b] for b in bars]) <= data[w]

# Setting the minimum limit for number of crates to be distributed for each bar
for b in bars:
    prob += pulp.lpSum([variable_dict[w + b] for w in warehouses]) >= data[b]

prob.writeLP("BeerTransportModel.lp")
prob.solve()
for v in prob.variables():
    print("{} = {}".format(v.name, v.varValue))

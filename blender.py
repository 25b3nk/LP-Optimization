'''
Link to the problem:
https://coin-or.github.io/pulp/CaseStudies/a_blending_problem.html
'''

import pulp
import json

# Ingredient wise price and other nutritional facts
blender_data = json.load(open('blender.json'))

ingredients_list = [val for val in blender_data]
nutition_attributes = ['protein', 'fat', 'fibre', 'salt']

# Nutrition requirement per 100 grams
nutition_requirements = {'protein': 12.0, 'fat': 8.0, 'fibre': 2.0, 'salt': 0.4}

# Nutrition wise either minimum or maximum
nutition_requirements_factor = {'protein': 'min', 'fat': 'min', 'fibre': 'max', 'salt': 'max'}
variable_dict = {}

# Initialize the problem
prob = pulp.LpProblem(name="Whiskas cat food problem", sense=pulp.LpMinimize)

# Create varaiables for each ingredient, where each ingredient is represented in quantity of 1 gram
for ingredient in ingredients_list:
    variable_dict[ingredient] = pulp.LpVariable(ingredient, lowBound=0, cat=pulp.LpInteger)

# Defining the objective function - Cost of the production
prob += pulp.lpSum([blender_data[ingredient]['price'] * variable_dict[ingredient] for ingredient in ingredients_list])

# Since max weight has to be 100 grams
prob += pulp.lpSum([variable_dict[ingredient] for ingredient in ingredients_list]) == 100

# Nutritional constraints modelling
for nutrient in nutition_attributes:
    if nutition_requirements_factor[nutrient] == 'min':
        prob += pulp.lpSum([blender_data[ingredient][nutrient] * variable_dict[ingredient] for ingredient in ingredients_list]) >= nutition_requirements[nutrient]
    elif nutition_requirements_factor[nutrient] == 'max':
        prob += pulp.lpSum([blender_data[ingredient][nutrient] * variable_dict[ingredient] for ingredient in ingredients_list]) <= nutition_requirements[nutrient]

prob.writeLP("WhiskasModel.lp")
prob.solve()
for v in prob.variables():
    print("{} = {}".format(v.name, v.varValue))

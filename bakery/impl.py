from pulp import *

class Bakery(object):
  def __init__(self, ingredients, products):
    self.ingredients = ingredients
    self.products = products
    for k, v in self.products.items():
      v['cost'] = 0
      for i, quantity in v['ingredients'].items():
        v['cost'] += quantity * ingredients[i]['cost']
      v['margin'] = v['price'] - v['cost']

  def prepare(self, max_time):
    # Define the problem
    prob = LpProblem("The bakery production", LpMaximize)

    # Variables
    lp_products = {p: LpVariable(p, 0, cat=LpInteger) for p in self.products.keys()}

    # Objective
    prob += lpSum([v['margin'] * lp_products[k] for k, v in self.products.items()])

    # Time constraint
    prob += lpSum([v['time'] * lp_products[k] for k, v in self.products.items()]) <= max_time

    # Stock constraints
    for k, v in self.ingredients.items():
      prob += lpSum([lp_products[p] * self.products[p]['ingredients'][k]] for p in self.products) <= v['stock']

    prob.solve()
    print("Status:", LpStatus[prob.status])

    # Each of the variables is printed with it's resolved optimum value
    for v in prob.variables():
      print(v.name, "=", v.varValue)

    # The optimised objective function value is printed to the screen
    print("Total margin = ", value(prob.objective))

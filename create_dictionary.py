from Outdated.dictionary import recipe
from needed import needed
from inventory import save, load
from shop import shop
from tier import tier
import random
import csv

data = []
recipes = {}

# keys
item1 = 0
item2 = 1
product = 2

with open('recipes.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        data.append(row)
    
for recipe in data:

    if not recipes:
        recipes[recipe[product]] = []
        print(recipe[product])

    if recipe[product] not in recipes:
        recipes[recipe[product]] = []
        print(recipe[product])


for recipe in data:
    first = recipe[item1]
    second = recipe[item2]

    recipes[recipe[product]].append((first, second))

print(recipes)
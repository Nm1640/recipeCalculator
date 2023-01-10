from dictionary import recipe
from needed import needed
from inventory import save, load
from shop import shop
from tier import tier
import random

inventory = []
load(inventory)

def path_weight(path, needed, storage):
    for item in path:
        pass
    
def find_random_path(item):
    # find a random path to cook the given recipe.
    item1 = 0
    item2 = 1
    
    # create the path
    path = []
    base_items = []
    path.append(item)

    # Start the loop
    for item in path:
        # print()
        # print(item)
        
        # Skip all items that are in shop or blank
        if item in shop:
            # print('In Shop')
            base_items.append(item)
            continue

        if item == '':
            # print('item empty')
            continue

        # add the ingredients to the end of path
        ingredients = random.choice(recipe[item])
        # print(ingredients)
        path.append(ingredients[item1])
        path.append(ingredients[item2])

    print(path)
    # print(len(base_items), base_items)

def main():
    pick_random = random.choice(list(recipe.keys()))
    for _ in range(10):
        find_random_path(pick_random)

if __name__ == '__main__':
    main()
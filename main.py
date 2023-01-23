from Outdated.dictionary import recipe
from needed import needed
from inventory import save, load
from shop import shop
from tier import tier
import random

inventory = []
load(inventory)

def random_path(item):
    # create a random list of items that will create the given item.
    # output should be: [ITEM, [item, item, item], [item, item, item], [item, item, item]]
    path = []
    path.append(item)
    path.append(random.choice(recipe[item]))

    for item in path:
        print(item)


def main():
    pick_random = random.choice(list(recipe.keys()))
    random_path(pick_random)

if __name__ == '__main__':
    main()
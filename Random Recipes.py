from Outdated.dictionary import recipe
from shop import shop
import random

def find_random_path(item):
    path = [item]
    base_items = set()
    while path:
        item = path.pop()
        if item in shop:
            base_items.add(item)
            continue
        elif item in recipe:
            path.extend(random.sample(recipe[item], 2))
    return base_items
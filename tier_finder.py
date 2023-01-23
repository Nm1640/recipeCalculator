from Outdated.dictionary import recipe
from needed import needed
from inventory import save, load
from shop import shop

item1 = 0
item2 = 1

# T1 = S + ''
# T2 = S + S
# T3 = T1 + S
# T4 = T1 + T1
# T5 = T2 + S
# T6 = remainder

tier1 = []
tier2 = []
tier3 = []
tier4 = []
tier5 = []
tier6 = []

tiers = [
tier1,
tier2,
tier3,
tier4,
tier5,
tier6,
]

print()
print()
# Find T1 recipe
for product in recipe:
    print(product)
    for combinations in recipe[product]:
        # skip all items in shop
        if product in shop:
            print(F'> {product} in shop. skipping.')
            break

        # find single item recipe
        if combinations[item2] == '':
            tier1.append(product)
            print(f'> {product} added to T1 {combinations}')
            break
print()
print()
# Find T2 recipe
for product in recipe:
    print(product)
    for combinations in recipe[product]:
        # Skip all Shop and T1 items
        if product in shop:
            print(F'> {product} in shop. skipping.')
            break
        elif product in tier1:
            print(F'> {product} in T1. skipping.')
            break

        # If item 1 and 2 are both in the shop: T2
        
        if combinations[item1] in shop and combinations[item2] in shop:
            tier2.append(product)
            print(f'>{product} added to T2, {combinations} both in shop.')
            break
print()
print()
# find T3 recipe
for product in recipe:
    print(product)
    for combinations in recipe[product]:
        # Skip all Shop and T1 - T2 items
        if product in shop:
            print(F'> {product} in shop. skipping.')
            break
        elif product in tier1:
            print(F'> {product} in T1. skipping.')
            break
        elif product in tier2:
            print(F'> {product} in T2. skipping.')
            break

        # If Item 1 or 2 is T1 and other is in shop.
        if (combinations[item1] in tier1 and combinations[item2] in shop) or (combinations[item1] in shop and combinations[item2] in tier1):
            tier3.append(product)
            print(f'{product} added to T3, {combinations}')
            break
print()
print() 
# find T4 recipe
for product in recipe:
    print(product)
    for combinations in recipe[product]:
        # Skip all Shop and T1 - T3 items
        if product in shop:
            print(F'> {product} in shop. skipping.')
            break
        elif product in tier1:
            print(F'> {product} in T1. skipping.')
            break
        elif product in tier2:
            print(F'> {product} in T2. skipping.')
            break
        elif product in tier3:
            print(F'> {product} in T3. skipping.')
            break

        # If Item 1 and Item 2  are both T1 Items
        if (combinations[item1] in tier1 and combinations[item2] in tier1) or (combinations[item1] in tier1 and combinations[item2] in tier1):
            tier4.append(product)
            print(f'{product} added to T4, {combinations}')
            break 
print()
print() 
# find T5 recipe
for product in recipe:
    print(product)
    for combinations in recipe[product]:
        # Skip all Shop and T1 - T4 items
        if product in shop:
            print(F'> {product} in shop. skipping.')
            break
        elif product in tier1:
            print(F'> {product} in T1. skipping.')
            break
        elif product in tier2:
            print(F'> {product} in T2. skipping.')
            break
        elif product in tier3:
            print(F'> {product} in T3. skipping.')
            break
        elif product in tier4:
            print(F'> {product} in T4. skipping.')
            break

        if (combinations[item1] in shop and combinations[item2] in tier2) or (combinations[item1] in tier2 and combinations[item2] in shop):
            tier5.append(product)
            print(f'{product} added to T5, {combinations}')
            break 

for product in recipe:
    if product not in shop and product not in tier1 and product not in tier2 and product not in tier3 and product not in tier4 and product not in tier5 and product not in tier6:
        tier6.append(product)

print('---')
for i in range(6):
    print(i + 1)
    print(tiers[i])
# Data will be transfered in lists of three:
example = ['item_a', 'item_b', 'item_c']

# Item A + B = C

# Item B can be NULL

example = ['item_a', '', 'item_c']

# Recipe calc should do T1 items first starting with Miracle Dinner, then do T6 down to T2.
# T1, T6 -> T2 

# Now we will create a path.
# A Path will include all 96 recipes and how to make them.
# example
path = [
    ['item_a', 'item_B', 'item_c'],
    ['item_a', 'item_B', 'item_c'],
    ['item_a', 'item_B', 'item_c'],
    ['item_a', 'item_B', 'item_c'],
    ['item_a', 'item_B', 'item_c'],
    ['item_a', 'item_B', 'item_c'],
    ['item_a', 'item_B', 'item_c']
]

# IDEAS:
# make top down recipes solver.
# Randomly pick from the 96, that need to be made, find the higher tier items do those first.

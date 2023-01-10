# Data will be transfered in lists of three:
example = ['item_a', 'item_b', 'item_c']

# Item A + B = C

# Item B can be NULL

example = ['item_a', '', 'item_c']

# Recipe calc should do T1 items first starting with Miracle Dinner, then do T6 down to T2.
# T1, T6 -> T2 

# Create a list of all possible recipe combinations for a given recipe
example = [ # Bad example lacks the listed format above should be [['item_a', 'item_b', 'item_c'], ['item_a', 'item_b', 'item_c'], ['item_a', 'item_b', 'item_c']]
    ['Gradual Syrup', 'Sap Syrup', 'Super Shroom Shake', 'Sap Soup', 'Pink Apple']
    ['Gradual Syrup', 'Sap Syrup', 'Slimy Shroom', 'Sap Soup', 'Honey Jar']
    ['Gradual Syrup', 'Honey Jar', 'Long-Last Shake']
    ['Gradual Syrup', 'Sap Syrup', 'Life Shroom', 'Sap Soup', 'Red Apple']
    ['Gradual Syrup', 'Turtley Leaf', 'Long-Last Shake']
    ['Gradual Syrup', 'Sap Syrup', 'Ultra Shroom Shake', 'Sap Soup', '']
    ['Gradual Syrup', 'Stamina Juice', 'Long-Last Shake', 'Inky Soup', 'Peachy Peach', 'Inky Sauce', 'Life Shroom']
    ['Gradual Syrup', 'Sap Syrup', 'Shroom Shake', 'Sap Soup', 'Primordial Fruit']
    ['Gradual Syrup', 'Herb Tea', 'Long-Last Shake', 'Smelly Herb', 'Dayzee Tear']
    ['Gradual Syrup', 'Sap Syrup', 'Life Shroom', 'Sap Soup', 'Primordial Fruit']
]

# lets give each of these a weight, 
# A & B weight will be determined the same way:
    # is item AB in shop?
        # What is item AB's difficulty? (Easiest will give 10 points hardest will give no points)
    # is C a T1 recipe?
        # is B empty? if so + 10

# C weight will be determined by the following:
    # Is Item C Still in the 96 Needed? x 10
    # Is Item C being used more than once? / 10

# 
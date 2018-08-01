#import pizza_mod

#pizza_mod.make_pizza(16, 'Pepperoni')
#pizza_mod.make_pizza(12, 'Mushrooms', 'Green Peppers', 'Extra Cheese')

# from pizza_mod import make_pizza
# make_pizza(16, 'Pepperoni')
# make_pizza(12, 'Mushrooms', 'Green Peppers', 'Extra Cheese')

# from pizza_mod import make_pizza as mp
# mp(16, 'Pepperoni')
# mp(12, 'Mushrooms', 'Green Peppers', 'Extra Cheese')

import pizza_mod as p
p.make_pizza(16, 'Pepperoni')
p.make_pizza(12, 'Mushrooms', 'Green Peppers', 'Extra Cheese')

# from pizza_mod import *
# make_pizza(16, 'Pepperoni')
# make_pizza(12, 'Mushrooms', 'Green Peppers', 'Extra Cheese')
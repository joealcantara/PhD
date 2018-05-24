from math import sqrt
import numpy as np
import pandas as pd 

plot1 = [1, 3]
plot2 = [2, 5]

plot1 = np.array(plot1)
plot2 = np.array(plot2)

euclidean_distance = sqrt( (plot1[0] - plot2[0])**2 + (plot1[1] - plot2[1])**2 )
print(euclidean_distance)

def ed(p, q):
    m = sqrt((q-p)**2)
    return m 

print(ed(plot1, plot2)) 
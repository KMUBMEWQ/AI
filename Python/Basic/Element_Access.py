# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 11:38:38 2019

@author: WEI QUN

P40
"""

import numpy as np
X = np.array([[51, 55], [14, 19], [0, 4]])
print(X)
print(X[0])
print(X[0][1])

for row in X:
    print(row)

X = X.flatten()
print(X)

X[np.array([0, 2, 4])]

print (X > 15)
""""
X=X[X>15]
print (X)
"""
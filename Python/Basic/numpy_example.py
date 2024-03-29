# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 11:20:46 2019

@author: WEI QUN
"""

import numpy as np
x = np.array([1.0, 2.0, 3.0])
print(x)
print(type(x))

y = np.array([2.0, 4.0, 6.0])
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x / 2)

A = np.array([[1,2], [3,4]])
print(A)
print(A.shape)
print(A.dtype)

B = np.array([[3,0], [0,6]])
print(A + B)
print(A * B)
print(A * 10)
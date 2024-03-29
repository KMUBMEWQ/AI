# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:13:37 2019

@author: homew

P53
"""
""" 
AND
"""
import numpy as np
def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    
    tmp = np.sum(w * x) + b
  # print(tmp)
    if tmp <= 0:
        return 0
    else: 
        return 1
print("This is for AND")    
print(AND(0,0))
print(AND(0,1))
print(AND(1,0))
print(AND(1,1))

""" 
NAND
"""
def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w * x) + b 
  #  print(tmp)
    if tmp <= 0:
        return 0
    else:
        return 1
print("This is for NAND")    
print(NAND(0,0))
print(NAND(0,1))
print(NAND(1,0))
print(NAND(1,1))

""" 
OR
"""
def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w * x) + b 
  #  print(tmp)
    if tmp <= 0:
        return 0
    else:
        return 1
print("This is for OR")    
print(OR(0,0))
print(OR(0,1))
print(OR(1,0))
print(OR(1,1))

"""
XOR
"""
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y
print("This is for XOR ")
print(XOR(0,0))
print(XOR(0,1))
print(XOR(1,0))
print(XOR(1,1))


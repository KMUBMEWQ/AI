# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 11:50:19 2019

@author: WEI QUN

P43
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 6.1, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label = "sin")
plt.plot(x, y2, linestyle = "--", label = "cos")
plt.xlabel("x")
plt.ylabel("y")
plt.title('sin & cos')
plt.legend()
plt.show()
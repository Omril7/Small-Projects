# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 11:38:10 2022

@author: Omri Leizerovitch
"""

import numpy as np
import matplotlib.pyplot as plt

a = -2
b = 2
x = np.linspace(a, b, 10**5)

m = 15
for n in range(-m,m+1):
    Sm1 = x**(2/3) + 0.9*((3.3-x**2)**0.5) * np.sin(np.pi * x * n)
    Sm2 = np.flip(Sm1)
    plt.xlim([-3,3])
    plt.ylim([-2,3])

    plt.plot(x, Sm1, color='r')
    plt.plot(x, Sm2, color='r')
    plt.title("Sin Love")
        
    plt.show()
    plt.pause(0.001)

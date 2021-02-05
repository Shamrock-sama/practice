# -*- coding:UTF-8 -*-
'''
Analytical and numerical integral
'''

from scipy import integrate
import numpy as np


# analytical
def f(x, c, k, a, b, m):
    if x>= 0:
        return (a * x + b) ** m * k / c * (x * V_hub / c) ** (k - 1) * np.exp(-(x * V_hub / c) ** k) * V_hub
    else:
        return 0



uplimit = 0.25
V_hub = 15
I_ref = 0.16
c = I_ref * (0.75 * V_hub + 3.3)
k = 0.27 * V_hub + 1.4
a = 0
b = 2000
m = 4
v, err = integrate.quad(f, 0, uplimit, args=(c, k, a, b, m))
print(v ** (1 / m))

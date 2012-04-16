'''
Created on Apr 14, 2012

@author: tepexa
'''

"""
E(x_n) = 1 + P(x_0)E(x_0) + P(x_2)E(x_0) + ... + P(x_n)E(x_n)

E(x_n) = (1 + P(x_0)E(x_0) + ... + P(x_n-1)E(x_n-1)) / (1 - P(x_n))

P(x_m) = (m-2)!(m^2 - 3m + 3)(n-m+1)/n!

"""
from pylab import *
def fac(n): 
    return prod(range(1,n+1))

def p(n,m):
    return (n-m+1)*(m**2-3*m+3)*fac(m-2)
res = [0, 0, 2]

for n in range(3,11):
    top = fac(n)
    for i in range(2,n):
        top += p(n,i) * res[i]
    bot = fac(n) - p(n,n)
    
    res.append(float(top)/bot)
    print top, bot    
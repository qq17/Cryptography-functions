import numpy as np
from sludv import sludv
from stepen import stepen
from obr import obr

a = 5
b = 1
m = 11
x = 8
y = 5

print(f'y^2 = {sludv(y, y, m, prnt=False)}')
print(f'x^3 + ax + b = {(stepen(x, 3, m, prnt=False) + sludv(a, x, m, prnt=False) + b)%m}')

l2 = sludv(((sludv(3, sludv(x, x, m, prnt=False), m, prnt=False) + a)%m), obr(sludv(2, y, m, prnt=False), m), m, prnt=False)
print(f'l_2*({x}, {y}) = {l2}')

c2 = (y - sludv(l2, x, m, prnt=False))%m
print(f'c_2*({x}, {y}) = {c2}')

x2 = (sludv(l2, l2, m, prnt=False) - sludv(2, x, m, prnt=False))%m
print(f'x_2*({x}, {y}) = {x2}')

y2 = (-(sludv(l2, x2, m, prnt=False) + c2))%m
print(f'y_2*({x}, {y}) = {y2}')

lp = sludv((y-y2)%m, obr((x-x2)%m, m), m, prnt=False)
print(f'l_({x2}, {y2})+({x}, {y}) = {lp}')

cp = (y - sludv(lp, x, m, prnt=False))%m
print(f'c_({x2}, {y2})+({x}, {y}) = {cp}')

xp = (sludv(lp, lp, m, prnt=False) - x - x2)%m
print(f'x_({x2}, {y2})+({x}, {y}) = {xp}')

yp = (-(sludv(lp, xp, m, prnt=False) + cp))%m
print(f'y_({x2}, {y2})+({x}, {y}) = {yp}')
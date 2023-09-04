import numpy as np
from binevklid import binevkl
from phi import phi
from stepen import stepen
from sludv import sludv

# esli n | (p-1)/n + 1

n = 3
p = 43
a = 22

print(f'x^{n} = {a} (mod {p})')
print(f'phi({p}) = {phi(p)}')
print(binevkl(n, phi(p)))
s = (p - 1) / n
print(f'({a})^({s}) = {stepen(a, s, p, prnt=False)}')
t = (((p - 1) / n) + 1) / n
print(f'({a})^({s + 1}) = ({a})^({n}*{t}) = ({a})^({n*t}) = {stepen(a, n*t, p, prnt=False)}')

x0 = stepen(a, t, p, prnt=False)
print(f'\nx0 = ({a})^({t}) = {stepen(a, t, p, prnt=False)} (mod {p})')

x = [x0]

l = stepen(n, s, p, prnt=False)
print(f'({n})^({s}) = {l} (mod {p})')

i = 1
while sludv(x[-1], l, p, prnt=False) not in x:
    x.append(sludv(x[-1], l, p, prnt=False))
    print(f'x{i} = ({x[-2]})*({l}) = {x[-1]} (mod {p})')
    i += 1

# x1 = sludv(x0, l, p, prnt=False)
# print(f'x1 = ({x0})*({l}) = {x1} (mod {p})')
#
# x2 = sludv(x1, l, p, prnt=False)
# print(f'x2 = ({x1})*({l}) = {x2} (mod {p})')
import numpy as np
from binevklid import binevkl
from phi import phi
from stepen import stepen
from sludv import sludv
from obr import obr

# esli not (n | (p-1)/n + 1) and n | (p-1)/n

n = 3
p = 31
a = 15

print(f'x^{n} = {a} (mod {p})')
print(f'phi({p}) = {phi(p)}')
print(binevkl(n, phi(p)))

s = (p - 1) / n
c = stepen(a, s/n, p, prnt=False)
print(f'c = R{p}({a}^{s/n}) = {c}')

#vvesti is tablicy pervoobraznyh korney
g = 3

print(f'(({g})^({s}))^y = c = {c} (mod {p})')
g_v_stepen_s = stepen(g, s, p, prnt=False)
print(f'({g_v_stepen_s})^y = {c}')

print(f'({c})^(-1) = ({g})^({-s})')


print(f'({a})^({s/n}) * ({g})^({-s}) = 1 (mod {p})')

e1 = -s+s/n
e2 = -s-s/n

k1 = sludv(stepen(a, s/(2*n), p, prnt=False), obr(stepen(g, -e1, p, prnt=False), p), p, prnt=False)
k2 = sludv(stepen(a, s/(2*n), p, prnt=False), obr(stepen(g, -e2, p, prnt=False), p), p, prnt=False)

print(f'({a})^({s/(2*n)}) * ({g})^({e1}) = {k1} (mod {p})')
print(f'({a})^({s/(2*n)}) * ({g})^({e2}) = {k2} (mod {p})')

if k1 == 1:
    k = k1
    e = e1
if k2 == 1:
    k = k2
    e = e2

domnoj_na_a = sludv(a, k, p, prnt=False)
print(f'({a})^({s/(2*n)+1}) * ({g})^({e}) = {domnoj_na_a} = x^({n}) (mod {p})')

t1 = (s/(2*n)+1) / 2
t2 = e/2
x0 = sludv(stepen(a, t1, p, prnt=False), obr(stepen(g, -t2, p, prnt=False), p), p, prnt=False)
print(f'\nx0 = ({a})^({t1}) * ({g})^({t2}) = {x0} (mod {p})')

x = [x0]

l = sludv(s/(2*n), 1, n, prnt=False)
if l == 1:
    l = -1
print(f'{s/(2*n)} = {l} (mod {n})')

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
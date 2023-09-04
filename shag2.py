import numpy as np
from binevklid import binevkl
from phi import phi
from stepen import stepen
from sludv import sludv
from obr import obr

# esli not (n | (p-1)/n + 1) and not (n | (p-1)/n)
# ili esli D(n, p-1) = 1

n = 3
p = 31
a = 15


print(f'x^{n} = {a} (mod {p})')
print(f'phi({p}) = {phi(p)}')
print(binevkl(n, phi(p)))

s = (p - 1) / n
r = sludv(s, 1, n, prnt=False)

# # esli D(n, p-1) = 1
# r = sludv((p-1), 1, n, prnt=False)
# s = (p - 1)

print(f'R{n}({s}) = {r}')

Q = s // n
print(f'({a})^({s}) = ({a})^({n}*{Q}+{r}) = {stepen(a, s, p, prnt=False)} = {stepen(a, n*Q+r, p, prnt=False)}')

obr_mod_n = obr(n*Q+r, n)
print(f'q*({n}*{Q}+{r}) = -1 (mod {n})')
q = (-1*obr_mod_n)%n
print(f'q = -1*({obr_mod_n}) = {q} (mod {n})')

t = (q * (n * Q + r) + 1) / n
print(f'{q}*({n}*{Q}+{r}) = {n}*{t} - 1')

vozved_v_q = stepen(stepen(a, s, p, prnt=False), q, p, prnt=False)
print(f'(({a})^({s}))^({q}) = ({a})^({s*q}) = {vozved_v_q}')

domnoj_na_a = sludv(a, vozved_v_q, p, prnt=False)
print(f'{a}*(({a})^({s}))^({q}) = ({a})^({s*q+1}) = {domnoj_na_a} = x^({n}) (mod {p})')

e = (s*q+1) / n
# print(f'({a})^({s + 1}) = ({a})^({n}*{e}) = ({a})^({n * e}) = {stepen(a, n * e, p, prnt=False)}')

x0 = stepen(a, e, p, prnt=False)
print(f'\nx0 = ({a})^({e}) = {stepen(a, e, p, prnt=False)} (mod {p})')

x = [x0]

l = stepen(n, s*q, p, prnt=False)
if l == 1:
    l = -1
print(f'({n})^({s*q}) = {l} (mod {n})')

# x1 = sludv(x0, l, p, prnt=False)
i = 1
while sludv(x[-1], l, p, prnt=False) not in x:
    x.append(sludv(x[-1], l, p, prnt=False))
    print(f'x{i} = ({x[-2]})*({l}) = {x[-1]} (mod {p})')
    i += 1

# print(sludv(x[-1], l, p, prnt=False))

# x2 = sludv(x1, l, p, prnt=False)
# print(f'x2 = ({x1})*({l}) = {x2} (mod {p})')
#
# x3 = sludv(x2, l, p, prnt=False)
# print(f'x1 = ({x2})*({l}) = {x3} (mod {p})')
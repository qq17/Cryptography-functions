import numpy as np
from prettytable import PrettyTable

n = 2
a = 170
p = 187

d = 1
while True:
    w_sq = (d*d-a)%p
    print(f'd = {d}, w^2 = {w_sq}')
    f = False
    for i in range(p):
        if (i*i)%p == w_sq:
            print(f'w^2 = {w_sq}, w = {i}')
            # f = True
            break
    else:
        w = w_sq
        print(f'nevychet w^2 = {w}')
        break
    d += 1

s = (p+1)/n

x = np.polynomial.polynomial.Polynomial([d, 1])
print(x)


i = 0
av = [s]
bv = [x]
cv = [1]


while av[i]!=1:
    av.append(av[i]//2)
    bt = bv[i]*bv[i]
    bi = np.polynomial.polynomial.Polynomial([k%p for k in bt.coef])
    if len(bi.coef) > n:
        if bi.coef[n]!=0:
            bi = np.polynomial.polynomial.Polynomial([(bi.coef[0]+w*bi.coef[n])%p]+
                                                     [(k) % p for k in bi.coef[(0+1):2]]+
                                                     [0]+
                                                     [(k)%p for k in bi.coef[(2+1):]])
    bv.append(bi)
    ct = cv[i]*(bv[i]**(av[i]%2))
    ci = np.polynomial.polynomial.Polynomial([k%p for k in ct.coef])
    if len(ci.coef) > n:
        if ci.coef[n]!=0:
            ci = np.polynomial.polynomial.Polynomial([(ci.coef[0]+w*ci.coef[2])%p]+
                                                     [(k) % p for k in ci.coef[(0+1):2]]+
                                                     [0]+
                                                     [(k)%p for k in ci.coef[(2+1):]])
    cv.append(ci)
    # cv.append(1)
    i += 1

print([av, bv, cv])

t = PrettyTable(['i']+list(range(i+1)))
t.add_row(['a', *av])
t.add_row(['b', *bv])
t.add_row(['c', *cv])
print(t)

ct = cv[i]*bv[i]
ci = np.polynomial.polynomial.Polynomial([k%p for k in ct.coef])
if len(ci.coef) > n:
    if ci.coef[n]!=0:
        ci = np.polynomial.polynomial.Polynomial([(ci.coef[0]+w*ci.coef[2])%p]+
                                                 [(k) % p for k in ci.coef[(0+1):2]]+
                                                 [0]+
                                                 [(k)%p for k in ci.coef[(2+1):]])
    cv.append(ci)

print('+ ans:', ci)

ci = np.polynomial.polynomial.Polynomial([(-k)%p for k in ci.coef])
print('- ans:', ci)
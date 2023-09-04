import numpy as np
from stepen import stepen
from primes import primes
from sludv import sludv

m = 53
a = 50
b = 27
B = [2, 3]
print(f'{a}^x = {b} (mod {m})')
print(f'B = {B}')

i = 1
while i<50:
    # print(f'\ni = {i}')
    d = stepen(a, i, m, prnt=False)
    # print(f'({i})^2 = {x} (mod {m})')

    p = primes(d)
    # print(f'{x} = {p}')

    # p = [1, 2, 3, 4, 5, 6, 7]

    # print([el in B for el in p].count(False))
    if [el in B for el in p].count(False) == 0:
        print(f'\ni = {i}')
        print(f'({a})^({i}) = {d} (mod {m})')
        print(f'{d} = {p}')
        print(f'{d} good')
    # else:
    #     print(f'\ni = {i}')
    #     print(f'({a})^({i}) = {d} (mod {m})')
    #     print(f'{d} = {p}')
    #     print(f'{d} bad')

    # z = sludv(d, b, m, prnt=False)
    # print('z = ', z)
    # p = primes(z)
    # if [el in B for el in p].count(False) == 0:
    #     print(f'i = {i}')
    #     print(f'({a})^({i}) * {b} = {z} (mod {m}) good')
    #     print(f'{z} = {p}')
    #     print(f'{z}')

    i += 1

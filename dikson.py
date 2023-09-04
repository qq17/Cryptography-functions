import numpy as np
from sludv import sludv
from primes import primes

m = 1817
B = [2, 3, 5]
print(f'm = {m}')
print(f'B = {B}')

i = np.floor(np.sqrt(m))+1
print('start', i)

while i<(np.floor(np.sqrt(m))+100):
    # print(f'\ni = {i}')
    x = sludv(i, i, m, prnt=False)
    # print(f'({i})^2 = {x} (mod {m})')

    p = primes(x)
    # print(f'{x} = {p}')

    # p = [1, 2, 3, 4, 5, 6, 7]

    # print([el in B for el in p].count(False))
    if [el in B for el in p].count(False) == 0:
        print(f'\ni = {i}')
        print(f'({i})^2 = {x} (mod {m})')
        print(f'{x} = {p}')
        print(f'{x} prinadl S')
    # else:
    #     print(f'\ni = {i}')
    #     print(f'({i})^2 = {x} (mod {m})')
    #     print(f'{x} = {p}')
    #     print(f'{x} ne prinadl S')
    i += 1

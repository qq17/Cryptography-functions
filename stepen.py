from prettytable import PrettyTable
from sludv import sludv

def stepen(num, stpn, m, prnt=True):
    i = 0
    av = [stpn]
    bv = [num]
    cv = [1]

    while av[i] != 1:
        av.append(av[i] // 2)
        bv.append(sludv(bv[i], bv[i], m, prnt=prnt))
        cv.append(sludv(cv[i], bv[i] ** (av[i] % 2), m, prnt=prnt))
        i += 1

    if prnt == True:
        print([av, bv, cv])

        t = PrettyTable(['i'] + list(range(i + 1)))
        t.add_row(['a', *av])
        t.add_row(['b', *bv])
        t.add_row(['c', *cv])
        print(t)

        print('ans', sludv(cv[i], bv[i], m))
    return sludv(cv[i], bv[i], m, prnt=False)


if __name__ == '__main__':
    a = 52
    b = 29
    m = 53

    print((b**a)%m)

    i = 0
    av = [a]
    bv = [b]
    cv = [1]

    while av[i]!=1:
        av.append(av[i]//2)
        bv.append(sludv(bv[i], bv[i], m))
        cv.append(sludv(cv[i], bv[i]**(av[i]%2), m))
        i += 1

    print([av, bv, cv])

    t = PrettyTable(['i']+list(range(i+1)))
    t.add_row(['a', *av])
    t.add_row(['b', *bv])
    t.add_row(['c', *cv])
    print(t)

    print('ans', sludv(cv[i], bv[i], m))
from prettytable import PrettyTable

def sludv(a, b, m, prnt = True):
    i = 0
    av = [a]
    bv = [b]
    bs = ['-']
    cv = [0]
    cs = ['-']

    while av[i] != 1:
        bs[i] = (bv[i] * 2)
        cs[i] = (cv[i] + bv[i] * (av[i] % 2))

        av.append(av[i] // 2)
        bv.append(bs[i] % m)
        cv.append(cs[i] % m)
        bs.append('-')
        cs.append('-')
        i += 1

    if prnt == True:
        print((a * b) % m)
        print([av, bv, bs, cv, cs])

        t = PrettyTable(['i'] + list(range(i + 1)))
        t.add_row(['a', *av])
        t.add_row(['b', *bv])
        t.add_row(['b\'', *bs])
        t.add_row(['c', *cv])
        t.add_row(['c\'', *cs])
        print(t)
    return (a * b) % m


if __name__ == '__main__':
    a = 6
    b = 8
    m = 11

    print((a*b)%m)

    i = 0
    av = [a]
    bv = [b]
    bs = ['-']
    cv = [0]
    cs = ['-']

    while av[i]!=1:
        bs[i]=(bv[i]*2)
        cs[i]=(cv[i]+bv[i]*(av[i]%2))

        av.append(av[i]//2)
        bv.append(bs[i]%m)
        cv.append(cs[i]%m)
        bs.append('-')
        cs.append('-')
        i += 1

    print([av, bv, bs, cv, cs])

    t = PrettyTable(['i']+list(range(i+1)))
    t.add_row(['a', *av])
    t.add_row(['b', *bv])
    t.add_row(['b\'', *bs])
    t.add_row(['c', *cv])
    t.add_row(['c\'', *cs])
    print(t)
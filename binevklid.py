from prettytable import PrettyTable
import numpy as np

def binevkl(a, m):
    k = 1
    while (a != 1 and a != 0) and (m != 1 and m != 0):
        old_a = a
        old_m = m
        a = min(old_a, old_m)
        m = max(old_a, old_m)
        print(f'{k}*D({m}, {a})')

        if (a % 2 == 0) and (m % 2 == 0):
            a = a / 2
            m = m / 2
            k = k * 2
        elif a % 2 == 0:
            a = a / 2
        elif m % 2 == 0:
            m = m / 2
        else:
            m = m - a

    return np.gcd(int(a), int(m))

if __name__ == '__main__':
    # a = 3
    # m = 22

    a = 1245
    m = 201
    old_a = a
    old_m = m
    a = min(old_a, old_m)
    m = max(old_a, old_m)

    az = a
    mz = m

    # a | e[0][0]
    # m | e[0][1]

    v = [[a, m]]
    c1 = [1, 0]
    c2 = [0, 1]
    e = [[c1.copy(), c2.copy()]]

    # print(e)
    i = 0
    k = 1
    while (a != 1 and a != 0) and (m != 1 and m != 0):
        old_a = a
        old_m = m
        a = min(old_a, old_m)
        m = max(old_a, old_m)
        if a != old_a:
            old_c1 = c1.copy()
            c1 = c2.copy()
            c2 = old_c1.copy()
        v.append([a, m])
        e.append([c1.copy(), c2.copy()])
        print(f'{k}*D({a}, {m})')

        if a == m:
            break

        if (a%2 == 0) and (m%2 == 0):
            a = a/2
            m = m/2
            k = k*2
            v.append([a, m])
            e.append([[1, 0], [0, 1]])
        # print('a = ', a)
        # print('m = ', m)
        while m%2==0 or m>a:
            # print('m>a')
            if a%2 == 0:
                if c1[0]%2==0 and c1[1]%2==0:
                    pass
                else:
                    if c1[0]>0:
                        c1[0]=c1[0]-az
                        c1[1]=c1[1]+mz
                    else:
                        c1[0]=c1[0]+az
                        c1[1]=c1[1]-mz
                    v[-1].append(a)
                    e[-1].append(c1.copy())
                a = a / 2
                c1[0] = c1[0]/2
                c1[1] = c1[1]/2
                # print('a delit na 2', e)
                v[-1].append(a)
                e[-1].append(c1.copy())
            elif m%2 == 0:
                if c2[0]%2==0 and c2[1]%2==0:
                    pass
                    # c2[0] = c2[0]/2
                    # c2[1] = c2[1]/2
                else:
                    if c2[0]>0:
                        c2[0]=c2[0]-mz
                        c2[1]=c2[1]+az
                    else:
                        c2[0]=c2[0]+mz
                        c2[1]=c2[1]-az
                    v[-1].append(m)
                    e[-1].append(c2.copy())
                m = m/2
                c2[0] = c2[0] / 2
                c2[1] = c2[1] / 2
                # print('m delit na 2', e)
                v[-1].append(m)
                e[-1].append(c2.copy())
            else:
                # if m<a:
                #     old_a = a
                #     old_m = m
                #     a = min(old_a, old_m)
                #     m = max(old_a, old_m)
                #     old_c1 = c1
                #     c1 = c2
                #     c2 = old_c1
                #     v.append([a, m])
                #     e.append([c1.copy(), c2.copy()])
                #     print('proc')
                #     continue
                m = m - a
                # print('before m minus a', e)
                c2[0] = c2[0] - c1[0]
                c2[1] = c2[1] - c1[1]
                # print('m minus a', e)
                v[-1].append(m)
                e[-1].append(c2.copy())

            # print(v)
            # print(e)

    for i, tv in enumerate(v):
        t = PrettyTable(['a', 'c1', 'c2'])
        for j, s in enumerate(tv):
            t.add_row([s, e[i][j][0], e[i][j][1]])
        print(t)

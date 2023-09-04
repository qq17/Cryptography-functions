from prettytable import PrettyTable
import numpy as np

def obr(a, m):
    i = 1
    q = ['-', '-']
    v = [0, 1]
    r = [m, a]

    while r[i] != 1:
        q.append(r[i - 1] // r[i])
        v.append(v[i - 1] - v[i] * q[i + 1])
        r.append(r[i - 1] % r[i])
        i += 1

    return v[i]

if __name__ == '__main__':
    # a = 3
    # m = 22

    a = np.polynomial.polynomial.Polynomial([1, 0, 0, 0, 0, 1])
    print(a)
    b = np.polynomial.polynomial.Polynomial([9, 1, 0, 1])
    print(b)
    m = 11

    a1 = [-1, 0, 0, 0, 0, 1]
    b1 = [9, 1, 0, 1]

    i = 1
    q = ['-', '-']
    # u = [1, 0]
    # v = [0, 1]
    r = [a, b]

    n = 0
    while True:
        koef = None
        ca = a.coef.tolist()
        # print(ca)
        sa = 0
        for i in range(len(ca) - 1, -1, -1):
            if ca[i] != 0:
                sa = i
                break

        cb = b.coef.tolist()
        # print(cb)
        sb = 0
        for i in range(len(cb) - 1, -1, -1):
            if cb[i] != 0:
                sb = i
                break

        sd = sa - sb
        # print(f'sd = {sd}')
        if (sd < 0):
            break

        if b.coef[0] == 0 and sb == 0:
            break

        # print('usl = ', a.coef[0] == 0 and sa == 0)
        if a.coef[0] == 0 and sa == 0:
            break

        while True:
            print(f'a = {a}')
            print('/')
            print(f'b = {b}')
            ca = a.coef.tolist()
            # print(ca)
            sa = 0
            for i in range(len(ca)-1, -1, -1):
                if ca[i] != 0:
                    sa = i
                    break
            # sa = len(ca) - ca.index(1) - 1
            # print(f'sa = {sa}')
            # ca.reverse()
            # print(ca)

            cb = b.coef.tolist()
            # print(cb)
            sb = 0
            for i in range(len(cb) - 1, -1, -1):
                if cb[i] != 0:
                    sb = i
                    break
            # print(f'sb = {sb}')

            sd = sa - sb
            # print(f'sd = {sd}')
            if (sd<0):
                break
            if a.coef[0] == 0 and sa == 0:
                break

            k = obr(cb[sb], m) * ca[sa]
            print(f'k = {k}')
            cd = [0]*(sd+1)
            cd[sd] = k
            d = np.polynomial.polynomial.Polynomial(cd)
            if koef is None:
                koef = d
            else:
                koef = koef + d
            print(f'a = {a}')
            print('-')
            # print(f'd = {d}')
            f = b*d
            cf = (np.array(f.coef)%m).tolist()
            f = np.polynomial.polynomial.Polynomial(cf)
            print(f'f = {f}')
            mf = a-f
            cmf = (np.array(mf.coef)%m).tolist()
            mf = np.polynomial.polynomial.Polynomial(cmf)
            print('=')
            print(f'mf = {mf}\n')
            a = mf

        print(f'koef = {koef}\n')
        q.append(koef)
        r.append(a)
        n += 1
        old_b = b
        b = a
        a = old_b

    # while r[i]!=1 and r[i]!=0:
    #     print(r)
    #     q.append(r[i-1]//r[i])
    #     # u.append(u[i - 1] - u[i] * q[i + 1])
    #     # v.append(v[i-1]-v[i]*q[i+1])
    #     r.append(r[i-1]%r[i])
    #     i += 1
    #
    print([q, r])
    #
    t = PrettyTable(['i']+list(range(2+n)))
    t.add_row(['q', *q])
    # t.add_row(['u', *u])
    # t.add_row(['v', *v])
    t.add_row(['r', *r])
    print(t)

    f1 = r[-2]
    print(f'f1 = {f1}')
    o = obr(f1.coef[-1], m)
    print(f'o = {o}')
    f1 = f1*o
    cf1 = (np.array(f1.coef)%m).tolist()
    f1 = np.polynomial.polynomial.Polynomial(cf1)
    print(f'f1 = {f1}')
    #
    #
    # a = np.polynomial.polynomial.Polynomial(a1)
    # print(a)
    # b = np.polynomial.polynomial.Polynomial(b1)
    # print(b)
    # m = 11
    #
    # i = 1
    # q = ['-', '-']
    # # u = [1, 0]
    # # v = [0, 1]
    # r = [a, b]
    #
    # n = 0
    # while True:
    #     koef = None
    #     ca = a.coef.tolist()
    #     # print(ca)
    #     sa = 0
    #     for i in range(len(ca) - 1, -1, -1):
    #         if ca[i] != 0:
    #             sa = i
    #             break
    #
    #     cb = b.coef.tolist()
    #     # print(cb)
    #     sb = 0
    #     for i in range(len(cb) - 1, -1, -1):
    #         if cb[i] != 0:
    #             sb = i
    #             break
    #
    #     sd = sa - sb
    #     print(f'sd = {sd}')
    #     if (sd < 0):
    #         break
    #
    #     if b.coef[0] == 0 and sb == 0:
    #         break
    #
    #     print('usl = ', a.coef[0] == 0 and sa == 0)
    #     if a.coef[0] == 0 and sa == 0:
    #         break
    #
    #     while True:
    #         print(f'a = {a}')
    #         print(f'b = {b}')
    #         ca = a.coef.tolist()
    #         # print(ca)
    #         sa = 0
    #         for i in range(len(ca) - 1, -1, -1):
    #             if ca[i] != 0:
    #                 sa = i
    #                 break
    #         # sa = len(ca) - ca.index(1) - 1
    #         print(f'sa = {sa}')
    #         # ca.reverse()
    #         # print(ca)
    #
    #         cb = b.coef.tolist()
    #         # print(cb)
    #         sb = 0
    #         for i in range(len(cb) - 1, -1, -1):
    #             if cb[i] != 0:
    #                 sb = i
    #                 break
    #         print(f'sb = {sb}')
    #
    #         sd = sa - sb
    #         print(f'sd = {sd}')
    #         if (sd < 0):
    #             break
    #         if a.coef[0] == 0 and sa == 0:
    #             break
    #
    #         k = obr(cb[sb], m) * ca[sa]
    #         print(f'k = {k}')
    #         cd = [0] * (sd + 1)
    #         cd[sd] = k
    #         d = np.polynomial.polynomial.Polynomial(cd)
    #         if koef is None:
    #             koef = d
    #         else:
    #             koef = koef + d
    #         print(f'a = {a}')
    #         print(f'd = {d}')
    #         f = b * d
    #         cf = (np.array(f.coef) % m).tolist()
    #         f = np.polynomial.polynomial.Polynomial(cf)
    #         print(f'f = {f}')
    #         mf = a - f
    #         cmf = (np.array(mf.coef) % m).tolist()
    #         mf = np.polynomial.polynomial.Polynomial(cmf)
    #         print(f'mf = {mf}\n')
    #         a = mf
    #
    #     print(f'koef = {koef}\n')
    #     q.append(koef)
    #     r.append(a)
    #     n += 1
    #     old_b = b
    #     b = a
    #     a = old_b
    #
    # # while r[i]!=1 and r[i]!=0:
    # #     print(r)
    # #     q.append(r[i-1]//r[i])
    # #     # u.append(u[i - 1] - u[i] * q[i + 1])
    # #     # v.append(v[i-1]-v[i]*q[i+1])
    # #     r.append(r[i-1]%r[i])
    # #     i += 1
    # #
    # print([q, r])
    # #
    # t = PrettyTable(['i'] + list(range(2 + n)))
    # t.add_row(['q', *q])
    # # t.add_row(['u', *u])
    # # t.add_row(['v', *v])
    # t.add_row(['r', *r])
    # print(t)
    #
    # f2 = r[-2]
    #
    # print(f'f1 = {f1}')
    # print(f'f2 = {f2}')
    #
    # ff=f1*f2
    # print(ff)
    # cff = (np.array(ff.coef) % m).tolist()
    # ff = np.polynomial.polynomial.Polynomial(cff)
    # print(f'ff = {ff}\n')
    #
    # # print(v[i])
    # # print((a*v[i])%m)
    #
    # # b = 695
    # # n = 47
    # # for i in range(30):
    # #     print(b)
    # #     b -= n
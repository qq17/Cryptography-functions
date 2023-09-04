from prettytable import PrettyTable

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

    a = 2
    m = 11

    i = 1
    q = ['-', '-']
    u = [1, 0]
    v = [0, 1]
    r = [m, a]

    while r[i]!=1 and r[i]!=0:
        print(r)
        q.append(r[i-1]//r[i])
        u.append(u[i - 1] - u[i] * q[i + 1])
        v.append(v[i-1]-v[i]*q[i+1])
        r.append(r[i-1]%r[i])
        i += 1

    print([q, u, v, r])

    t = PrettyTable(['i']+list(range(i+1)))
    t.add_row(['q', *q])
    t.add_row(['u', *u])
    t.add_row(['v', *v])
    t.add_row(['r', *r])
    print(t)

    print(v[i])
    print((a*v[i])%m)

    # b = 695
    # n = 47
    # for i in range(30):
    #     print(b)
    #     b -= n
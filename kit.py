m = [2, 3, 5, 7]

# a = [1, 2, 2, 3]
# b = [1, 0, 4, 2]
# c = []
#
# for i in range(4):
#     c.append((a[i]*b[i])%m[i])
# print(c)
#
# d = [0, 2, 3, 1]
# r = []
#
# for i in range(4):
#     r.append((c[i]+d[i])%m[i])
# print(r)


a = [0, 2, 3, 1]
b = [0, 1, 1, 2]
c = []

for i in range(4):
    c.append((a[i]*b[i])%m[i])
print(c)

d = [1, 0, 4, 2]
r = []

for i in range(4):
    r.append((c[i]+d[i])%m[i])
print(r)


from prettytable import PrettyTable
from obr import obr


print(obr(2, 3))
# i = 0
cc = [r]
pc = []
raz = []
ch = []

for i in range(3):
    print('cc', cc)
    pc.append(cc[i][0])
    print('pc',pc[i])
    raz.append([(cc[i][j]-pc[i])%m[i+j] for j in range(len(cc[i]))])
    print('raz',raz)
    print('i', i)
    print('r',raz[i][1])
    print('f', m[i], m[i+1], obr(m[i], m[i + 1]))
    print([(raz[i][j] * obr(m[i], m[i + j])) % m[i + j] for j in range(1, 4 - i)])
    ch.append(['*'] + [(raz[i][j] * obr(m[i], m[i + j])) % m[i + j] for j in range(1, 4 - i)])
    print('ch',ch)
    if (i+1!=3):
        cc.append(ch[i][1:])
    # print(cc)
    i += 1

print([cc, pc, raz, ch])

t = PrettyTable(['i']+list(range(i)))
t.add_row(['cc', *cc])
t.add_row(['pc', *pc])
t.add_row(['raz', *raz])
t.add_row(['ch', *ch])
print(t)

wasd = lambda x, Vc1: [x+Vcm for Vcm in [Vc1]][0]
print(wasd(1, 7))
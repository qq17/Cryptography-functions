import numpy as np

def mul(mtx, m, i, k): #m ignored
    mtx[i, :] = (mtx[i,:]*k)
    # print((mtx[0, :] * k))
    # print((mtx[0,:]*k)%7)
    return mtx

def add(mtx, m, i, j, k): #m ignored
    s = (mtx[i,:]*k)
    mtx[j, :] = (mtx[j, :] + s)
    # print((mtx[0, :] * k))
    # print((mtx[0,:]*k)%7)
    return mtx

def mulm(mtx, m, i, k):
    mtx[i, :] = (mtx[i,:]*k)%m
    # print((mtx[0, :] * k))
    # print((mtx[0,:]*k)%7)
    return mtx

def addm(mtx, m, i, j, k):
    s = (mtx[i,:]*k)%m
    mtx[j, :] = (mtx[j, :] + s)%m
    # print((mtx[0, :] * k))
    # print((mtx[0,:]*k)%7)
    return mtx

a = np.array([np.array([3, 1, 0]),
              np.array([0, 1, 1]),
              np.array([4, 0, 1])], dtype=float)

b = np.array([4, 5, 11])

m = 96

mtx = np.c_[a, b]
print(mtx)

mtx = mulm(mtx, m, 2, 3)
print(mtx)

mtx = addm(mtx, m, 0, 2, -4)
print(mtx)

mtx = addm(mtx, m, 1, 2, -92)
print(mtx)

mtx = mulm(mtx, m, 2, -41)
print(mtx)

mtx = addm(mtx, m, 2, 1, -1)
print(mtx)

mtx = addm(mtx, m, 1, 0, -1)
print(mtx)

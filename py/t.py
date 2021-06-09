def merge(List):
    sortProcess(List, 0, len(List) - 1)

def sortProcess(l, f, e):
    if f == e:
        return
    mid = int((f + e) / 2)
    sortProcess(l, f, mid)
    sortProcess(l, mid + 1, e)
    mergeProcess(l, f, mid, e)

def mergeProcess(l, f, mid, e):
    L = l[f: mid + 1]
    R = l[mid + 1: e + 1]
    i = 0
    j = 0
    k = f
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            l[k] = L[i]
            i += 1
        else:
            l[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        l[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        l[k] = R[j]
        j += 1
        k += 1

import numpy as np

i = np.random.randint(low = -100, high = 100, size = 4).tolist()
i = [1,1,3,5,2,5,6]
merge(i)
print(i)
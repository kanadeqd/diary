def antiSort(L):
    l = 0
    e = len(L) - 1
    sort(L, l, e)


def sort(L, l, e):
    if l == e:
        return
    mid = int((l + e) / 2)
    sort(L, l, mid)
    sort(L, mid + 1, e)
    merge(L, l, mid, e)


def merge(L, l, mid, e):
    left = L[l: mid + 1]
    right = L[mid + 1: e + 1]
    i = 0
    j = 0
    k = l
    while (i < len(left) and j < len(right)):
        if left[i] <= right[j]:
            L[k] = left[i]
            i += 1
        else:
            print((left[i], right[j]))
            L[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        L[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        L[k] = right[j]
        j += 1
        k += 1


L = [1,3,4,2]
antiSort(L)
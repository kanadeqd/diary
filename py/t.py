def getMax(List, f, e):
    if f == e:
        return List[f]

    mid = int((f + e) / 2)
    left = getMax(List, f, mid)
    right = getMax(List, mid + 1, e)

    return max(left, right)

x = [1,2,3,4,5,6,7]
getMax(x,0,len(x)-1)
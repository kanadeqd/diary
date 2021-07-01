def getMax(st):
    arr = getList(st)
    re = []
    for _ in range(len(arr)):
        re.append(" ")
    c = -1
    r = -1
    m = 0
    for i in range(0, len(arr)):
        if r > i:
            re[i] = min(re[c - (i - c)], r - i)
        else:
            re[i] = 1

        while (i + re[i] < len(arr) and i - re[i] > -1):
            if (arr[i + re[i]] == arr[i - re[i]]):
                re[i] += 1
            else:
                break
        if (i + re[i]) > r:
            r = i + re[i]
            c = i
        m = max(m, re[i])

    return (m - 1) / 2


def getList(st):
    arr =["."]
    for i in st:
        arr.append(i)
        arr.append(".")
    return arr


getMax('abccba')
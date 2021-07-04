class windows():
    def __init__(self, index, value):
        self.index = index
        self.value = value


def getDiffNum(arr, num):
    L = 0
    R = 0
    res = 0
    maxWindows = []
    minWindows = []
    while L < len(arr):
        while R < len(arr):
            while maxWindows != [] and maxWindows[0].value <= arr[R]:
                maxWindows.pop()
            maxWindows.append(windows(R, arr[R]))

            while minWindows != [] and minWindows[0].value >= arr[R]:
                minWindows.pop()
            minWindows.append(windows(R, arr[R]))

            if maxWindows[0].value - minWindows[0].value >= num:
                break

            R += 1
        if maxWindows[0].index == L:
            maxWindows.pop(0)
        if minWindows[0].index == L:
            minWindows.pop(0)

        res += R - L
        L += 1
    return res

arr = [4,3,5,4,3,3,6,7]

print (getDiffNum(arr,0))

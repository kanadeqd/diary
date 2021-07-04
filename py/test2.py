class LargeQ():
    def __init__(self):
        self.index = []
        self.value = 0

        
def get_rl(arr):
    dic = {}
    queue = []
    for i in range(0,len(arr)):
        if queue == [] or queue[-1].value > arr[i]:
            l = LargeQ()
            l.index.append(i)
            l.value = arr[i]
            queue.append(l)
        
        else :
            if queue[-1].value == arr[i]:
                queue[-1].index.append(i)
            else:
                right = arr[i]
                while queue != [] and queue[-1].value < arr[i]:
                    res = queue.pop()
                    if queue == []:
                        left = "Null"
                    else:
                        left = queue[-1].value
                    for k in res.index:
                        dic[k] = (left,right)
                l = LargeQ()
                l.index.append(i)
                l.value = arr[i]
                queue.append(l)
    
    right = "Null"
    while len(queue) > 1:
        res = queue.pop()
        left = queue[-1].value
        for k in res.index:
            dic[k] = (left,right)
        right = res.value
    last = queue.pop()
    left = "Null"
    for k in last.index:
        dic[k] = (left,right)


arr = [4,3,5,4,3,3,6,7]
print(get_rl(arr))
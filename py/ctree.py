def CtreeProcess(head):
    s = []
    state = 0
    res = True
    if (head._data is not None):
        s.append(head)
        while(s != []):
            node = s.pop(0)
            res = Ctree(node,state)
            state = res[1]
            if not res[0]:
                return res[0]
            if node._left is not None:
                s.append(node._left)
            if node._right is not None:
                s.append(node._right)
        return res[0]
                
def Ctree(node,state):
    if node._right and not node._left:
        return (False,0)
    if state == 0:
        if node._left and not node._right:
            return (True,1)
        else:
            return(True, 0)
    if state == 1:
        if node._left or node._right:
            return (False,1)
        else:
            return (True,1)


class Tree:

    def __init__(self, data=None, left=None, right=None):
        self._data = data
        self._left = left
        self._right = right


print(CtreeProcess(Tree(5,Tree(1),Tree(7))))
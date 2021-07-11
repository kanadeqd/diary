class Tree:

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def morrisIn(t):
    cur = t
    mostright = Tree()

    while cur != None:
        mostright = cur.left
        if mostright != None:
            while mostright.right != None and mostright.right != cur:
                mostright = mostright.right
            if mostright.right == None:
                mostright.right = cur
                print(cur.data)
                cur = cur.left
                continue
            else:
                mostright.right = None
                print(cur.data)
                cur = cur.right
        else:
            print(cur.data)
            cur = cur.right


tree = Tree(1)
tree.left = Tree(2,Tree(4),Tree(5))
tree.right = Tree(3,Tree(6),Tree(7))

morrisIn(tree)
class Tree:

    def __init__(self, data=None, left=None, right=None):
        self._data = data
        self._left = left
        self._right = right

    def preorder(self):
        if (not self._data):
            print("data", self._data)
        if (not self._left):
            self._left.preorder()
        if (not self._right):
            self._right.preorder()

    def inorder(self):
        if (not self._left):
            self._left.preorder()
        if (not self._data):
            print("data", self._data)
        if (not self._right):
            self._right.preorder()

    def postorder(self):
        if (not self._left):
            self._left.preorder()
        if (not self._right):
            self._right.preorder()
        if (not self._data):
            print("data", self._data)


tree = Tree(1)
tree._left = Tree(2,4,5)
tree._right = Tree(3,6,7)

tree.preorder()
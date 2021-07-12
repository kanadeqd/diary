class TripleInOne:

    def __init__(self, stackSize: int):
        self.stack = ['' * stackSize * 3]
        self.stack0End = 0
        self.stack1End = stackSize
        self.stack2End = stackSize * 2
        self.size = stackSize

    def push(self, stackNum: int, value: int) -> None:
        if stackNum == 0:
            if self.stack0End < self.size: 
                self.stack[self.stack0End] = value
                self.stack0End += 1
        if stackNum == 1:
            if self.stack1End < self.size * 2:
                self.stack[self.stack1End] = value
                self.stack1End += 1
        if stackNum == 2:
            if self.stack2End < self.size * 3:
                self.stack[self.stack2End] = value
                self.stack2End += 1
        return
            
    def pop(self, stackNum: int) -> int:
        if self.isEmpty(stackNum):
            return -1
        if stackNum == 0:
            self.stack0End -= 1
            return self.stack[self.stack0End]
        if stackNum == 1:
            self.stack1End -=1
            return self.stack[self.stack1End]
        if stackNum == 2:
            self.stack2End -=1
            return self.stack[self.stack2End]
            

    def peek(self, stackNum: int) -> int:
        if self.isEmpty(stackNum):
            return -1
        if stackNum == 0:
            return self.stack[self.stack0End -1]
        if stackNum == 1:
            return self.stack[self.stack1End -1]
        if stackNum == 2:
            return self.stack[self.stack2End -1]

    def isEmpty(self, stackNum: int) -> bool:
        if stackNum == 0:
            return self.stack0End == 0
        if stackNum == 1:
            return self.stack1End == self.size
        if stackNum == 2:
            return self.stack2End == self.size * 2

# Your TripleInOne object will be instantiated and called as such:
# obj = TripleInOne(stackSize)
# obj.push(stackNum,value)
# param_2 = obj.pop(stackNum)
# param_3 = obj.peek(stackNum)
# param_4 = obj.isEmpty(stackNum)
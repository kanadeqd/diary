class Stack:
    
    def __init__(self,size):
        self.size = size
        self.stack = [''] * size
        self.end = 0

    def isEmpty(self):
        if self.end == 0:
            return 1
        else:
            return 0

    def push(self,number):
        if self.end == self.size:
            print("stack is full")
        else:
            self.stack[self.end] = number 
            self.end += 1

    def peek(self):
        if Stack.isEmpty(self):
            print("stack is empty")
        else:
            tmp = self.end - 1
            return self.stack[tmp]
        
    def pop(self):
        if Stack.isEmpty(self):
            print("stack is empty")
        else:
            self.end -= 1
            return self.stack[self.end]

    def stackSize(self):
        return self.end
    
class Queue:
    
    def __init__(self,size):
        self.queue = [''] * size
        self.size = size
        self.sizeCurrent = 0
        self.end = 0
        self.start = 0
    
    def isEmpty(self):
        if self.sizeCurrent == 0:
            return 1
        else:
            return 0
    
    def push(self,number):
        if self.sizeCurrent == self.size :
            print("queue is full")
        else:
            self.queue[self.start] = number
            self.start += 1
            self.sizeCurrent += 1
            if(self.start >= self.size):
                self.start -= self.size
        
    def pop(self):
        if self.sizeCurrent == 0:
            print("queue is empty")
        else:
            temp = self.end 
            self.end  += 1
            self.sizeCurrent -= 1
            if(self.end >= self.size):
                self.end -= self.size
            return self.queue[temp]
    
    def peek(self):
        if self.sizeCurrent == 0:
            print("queue is empty")
        else:
            return self.queue[self.end]
        
    def queueSize(self):
        return self.sizeCurrent
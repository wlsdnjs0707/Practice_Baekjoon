# 스택

class Stack:
    def __init__(self):
        self.myStack = []

    def push(self,value):
        self.myStack.append(value)

    def pop(self):
        try:
            print(self.myStack.pop())
        except IndexError:
            print(-1)
    
    def size(self):
        print(len(self.myStack))
    
    def top(self):
        if len(self.myStack)==0:
            print(-1)
        else:
            print(self.myStack[-1])

    def empty(self):
        if len(self.myStack)==0:
            print(1)
        else:
            print(0)

n = int(input())

s = Stack()

for i in range(n):
    command=list(input().split())

    if command[0]=='push':
        s.push(int(command[1]))
    elif command[0]=='pop':
        s.pop()
    elif command[0]=='size':
        s.size()
    elif command[0]=='top':
        s.top()
    elif command[0]=='empty':
        s.empty()


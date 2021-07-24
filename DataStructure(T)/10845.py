# 큐

class Queue:
    def __init__(self):
        self.myQueue=[]

    def push(self,value):
        self.myQueue.append(value)

    def pop(self):
        try:
            print(self.myQueue.pop(0))
        except IndexError:
            print(-1)

    def size(self):
        print(len(self.myQueue))

    def empty(self):
        if len(self.myQueue)==0:
            print(1)
        else:
            print(0)
    
    def front(self):
        if len(self.myQueue)==0:
            print(-1)
        else:
            print(self.myQueue[0])
    
    def back(self):
        if len(self.myQueue)==0:
            print(-1)
        else:
            print(self.myQueue[-1])

n = int(input())
q = Queue()

for i in range(n):
    command = list(input().split())

    if command[0]=='push':
        q.push(int(command[1]))
    elif command[0]=='pop':
        q.pop()
    elif command[0]=='size':
        q.size()
    elif command[0]=='empty':
        q.empty()
    elif command[0]=='front':
        q.front()
    elif command[0]=='back':
        q.back()
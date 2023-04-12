# Enter your code here. Read input from STDIN. Print output to STDOUT
class Queue:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    
    def enqueue(self,item):
        self.stack1.append(item)
    
    def dequeue(self):
        self.print()
        self.stack2.pop()
    
    def print(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

if __name__=='__main__':
    inp=int(input())
    q=Queue()
    for i in range(inp):
        query=list(map(int,input().split()))
        # print(query)
        if query[0]==1:
            q.enqueue(query[1])
        elif query[0]==2:
            q.dequeue()
        else:
            print(q.print())
            
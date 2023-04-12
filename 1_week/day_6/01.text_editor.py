class TextEditor():
    def __init__(self):
        self.s=''
        self.stack=[]
    
    def append(self,char):
        self.stack.append(self.s)
        self.s+=char
    
    def delete(self,k):
        if k>len(self.s):
            return
        self.stack.append(self.s)
        self.s=self.s[:len(self.s)-k]
        
    def print_k(self,k):
        print(self.s[k-1])
    
    def undo(self):
        if len(self.stack):
            self.s=self.stack.pop()

if __name__=='__main__':
    rng=int(input())
    S=TextEditor()
    for i in range(rng):
        query=list(input().split(' '))
        if query[0]=='1':
            S.append(query[1])
        elif query[0]=='2':
            S.delete(int(query[1]))
        elif query[0]=='3':
            S.print_k(int(query[1]))
        else:
            S.undo()
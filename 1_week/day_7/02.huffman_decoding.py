def traversal(root,s,i):
    if root:
        if not root.left and not root.right:
            return i,root.data
        if s[i]=='0':
            return traversal(root.left,s,i+1) 
        if s[i]=='1':
            return traversal(root.right,s,i+1)
        
def decodeHuff(root, s):
    #Enter Your Code Here
    i=0
    res=''
    while i<len(s):
        new_i,char=traversal(root,s,i)
        res+=char
        i=new_i
    print(res)


# alternate solution
def decodeHuff(root, s):
    currentNode = root
    for letter in s:
        if letter == '1':
            currentNode = currentNode.right
        else:
            currentNode = currentNode.left
        if currentNode.right == None and currentNode.left == None:
            print(currentNode.data,end='')
            currentNode = root
def preOrder(root):
    #Write your code here
    if root:
        print(root.info,end=' ')
        preOrder(root.left)
        preOrder(root.right)
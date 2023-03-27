def flippingMatrix(matrix):
    # Write your code here
    res=0
    for i in range(len(matrix)//2):
        for j in range(len(matrix)//2):
            res+=max(matrix[i][j],matrix[i][~j],matrix[~i][j],matrix[~i][~j])
    return res
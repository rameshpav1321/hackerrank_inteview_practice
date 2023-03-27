def diagonalDifference(arr):
    # Write your code here
    left_sum=0
    right_sum=0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i==j:
                left_sum+=arr[i][j]
            if i+j==len(arr)-1:
                right_sum+=arr[i][j]
    return abs(left_sum-right_sum)

# a better solution
def diagonalDifference(arr):
    # Write your code here
    diff = 0
    for i in range(len(arr)):
        diff += arr[i][i] - arr[i][-i-1]
    return abs(diff)
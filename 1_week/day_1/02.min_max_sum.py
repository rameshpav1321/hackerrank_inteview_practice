def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    print(sum(arr[:-1]),sum(arr[1:]))
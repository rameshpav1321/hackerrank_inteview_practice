def countingSort(arr):
    # Write your code here
    res=[0]*100
    for num in arr:
        res[num]+=1
    return res
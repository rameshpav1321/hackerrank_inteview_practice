def pairs(k, arr):
    # Write your code here
    sorted_arr=sorted(arr,reverse=True)
    count=0
    my_set=set()
    for num in sorted_arr:
        if num+k in my_set:
            count+=1
        my_set.add(num)
    return count
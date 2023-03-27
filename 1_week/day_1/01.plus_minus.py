def plusMinus(arr):
    # Write your code here
    total=len(arr)
    counts=[0,0,0]
    for num in arr:
        if num>0:
            counts[0]+=1
        elif num<0:
            counts[1]+=1
        else:
            counts[2]+=1
    for i in range(len(counts)):
        print('%.6f'%(counts[i]/total))

def minimumBribes(q):
    # Write your code here
    res=0
    for i in range(len(q)-1,0,-1):
        if q[i]!=i+1:
            if q[i-1]==i+1:
                res+=1
                q[i-1],q[i]=q[i],q[i-1]
            elif q[i-2]==i+1:
                res+=2
                q[i-2],q[i-1],q[i]=q[i-1],q[i],q[i-2]
            else:
                print('Too chaotic')
                return
    print(res)
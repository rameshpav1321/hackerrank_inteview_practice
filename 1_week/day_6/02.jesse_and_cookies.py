from queue import PriorityQueue            
def cookies(k, arr):
    # Write your code here
    count=0
    q=PriorityQueue()
    for num in arr:
        q.put(num)
    while q.queue[0]<k:
        if q.qsize()<2:
            return -1
        a,b=q.get(),q.get()
        q.put(a+(2*b))
        count+=1
    return count
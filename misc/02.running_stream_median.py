from queue import PriorityQueue
def running_median(nums):
    res=[]
    res.append(nums[0])
    min_heap=PriorityQueue()
    max_heap=PriorityQueue()
    max_heap.put(-nums[0])
    for num in nums[1:]:
        if max_heap.qsize()>min_heap.qsize():
            if num<-max_heap.queue[0]:
                min_heap.put(-max_heap.get())
                max_heap.put(-num)
            else:
                min_heap.put(num)
            res.append((-max_heap.queue[0]+min_heap.queue[0])/2)
        else:
            if num<-max_heap.queue[0]:
                max_heap.put(-num)
            else:
                min_heap.put(num)
                max_heap.put(-min_heap.get())
            res.append(-max_heap.queue[0])
    return res

print(running_median([12, 15, 10, 5, 8, 7, 16]))



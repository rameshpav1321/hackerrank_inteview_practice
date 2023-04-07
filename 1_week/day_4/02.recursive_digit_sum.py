def superDigit(n, k):
    # Write your code here
    res=sum([int(c) for c in n])*k
    while True:
        if len(str(res))==1:
            break
        res=sum(int(c) for c in str(res))
    return res
   
# recursive solution
def superDigit(n:str, k:int):
    result = sum(map(int, n)) * k
    # base case
    if result <= 9:
        return result    
    # recursive case
    return superDigit(str(result), 1)
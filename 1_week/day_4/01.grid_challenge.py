def gridChallenge(grid):
    # Write your code here
    for i in range(len(grid)):
        grid[i]=sorted(list(grid[i]))
    for i in range(len(grid[0])):
        tmp=[]
        for lst in grid:
            tmp.append(lst[i])
        if tmp!=sorted(tmp):
            return 'NO'
    return 'YES'
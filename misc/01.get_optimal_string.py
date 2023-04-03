def get_optimal_string(str):
    str_len=len(str)
    ones_count=str.count('1')
    zeros_count=str_len-ones_count
    if ones_count==str_len:
        return str
    count=0
    res=''
    flag=True
    while ones_count>0 and zeros_count>0:
        if flag:
            flag=False
            ones_count-=1
            res='1'+res
        else:
            flag=True
            zeros_count-=1
            res='0'+res
    if ones_count==0:
        for i in range(zeros_count):
            res='0'+res
    else:
        for i in range(ones_count):
            res='1'+res
    return res


print(get_optimal_string('011'))
print(get_optimal_string('011000'))
print(get_optimal_string('111'))


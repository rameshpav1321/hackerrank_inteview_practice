def timeConversion(s):
    # Write your code here
    lst=s.split(':')
    seconds=''.join(list(lst[-1][:-2]))
    if list(lst[-1])[-2]=='P':
        lst[0]=str(12+int(lst[0])) if lst[0]!='12' else lst[0]     
    else:
        lst[0]='00' if lst[0]=='12' else lst[0]
    hours_mins=':'.join(lst[:-1])
    return (hours_mins+':'+seconds)
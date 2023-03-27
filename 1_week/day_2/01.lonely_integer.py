def lonelyinteger(a):
    # Write your code here
    my_dict={}
    for num in a:
        my_dict[num]=1+my_dict.get(num,0)
    sorted_dict=sorted(my_dict.items(),key=lambda i:i[1])
    return sorted_dict[0][0]
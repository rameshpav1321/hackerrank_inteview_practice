def legoBlocks(n, m):
    # Write your code here
    mod=10**9+7
    single_row_combos=[1,2,4,8]
    for i in range(4,m):
        single_row_combos.append(sum(single_row_combos[-4:])%mod)
    total_combos=[row**n%mod for row in single_row_combos]
    
    valid_combos=[1]
    for i in range(1,m):
        invalid_combo=sum([total*valid for total,valid in zip(total_combos[:i],valid_combos[::-1])])
        valid_combos.append((total_combos[i]-invalid_combo)%mod)
    return valid_combos[-1]
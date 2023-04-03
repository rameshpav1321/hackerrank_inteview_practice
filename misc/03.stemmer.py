def stemmer(str):
    word_lst=str.split(' ')
    match_suffix={'ed','ly','ing'}
    res=[]
    for word in word_lst:
        if len(word)>1 and (word[-2:] in match_suffix or word[-3:] in match_suffix):
            if len(word)>10 or len(word)>11:
                res.append(word[:8])
            else:
                res.append(word[:-2]) if not word[-3:]=='ing' else res.append(word[:-3])
        else:
            if len(word)>8:
                res.append(word[:8])
            else:
                res.append(word)
    return ' '.join(res)


print(stemmer('an extremely dangerous dog is barking'))
print(stemmer('a boy is jumping quickly'))
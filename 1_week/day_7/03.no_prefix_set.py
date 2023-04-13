# def noPrefix(words):
#     # Write your code here
#     pos_dict={}
#     for ind,word in enumerate(words):
#         pos_dict[word]=ind
#     sorted_words=sorted(words)
#     res=float('inf')
#     for i in range(1,len(sorted_words)):
#         if sorted_words[i].startswith(sorted_words[i-1]):
#            res=min(res,pos_dict[sorted_words[i]])
#     print('GOOD SET') if res==float('inf') else print('BAD SET',words[res],sep='\n')
def noPrefix(words):
    # Write your code here
    prefixes=set()
    seen_words=set()
    for word in words:
        if word in prefixes:
            print('BAD SET',word,sep='\n')
            return
        curr_prefixes=[word[:i+1] for i in range(len(word))]
        if seen_words.intersection(curr_prefixes):
            print('BAD SET',word,sep='\n')
            return
        prefixes.update(curr_prefixes)
        seen_words.add(word)
    print('GOOD SET')
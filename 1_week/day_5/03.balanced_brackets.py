def isBalanced(s):
    # Write your code here
    bracket_match={'}':'{',']':'[',')':'('}
    stack=[]
    for char in s:
        if char in bracket_match.keys():
            if not stack or stack[-1]!=bracket_match[char]:
                return 'NO'
            else:
                stack.pop()
        else:
            stack.append(char)
    return 'YES' if len(stack)==0 else 'NO'
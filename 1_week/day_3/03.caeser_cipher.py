def caesarCipher(s, k):
    # Write your code here
    res=''
    print(ord('z'),ord('Z'))
    for char in s:
        if char.isalpha() and char.isupper():
            res+=chr(ord('A')+(ord(char)+k-ord('A'))%26)
        elif char.isalpha() and char.islower():
            res+=chr(ord('a')+(ord(char)+k-ord('a'))%26)
        else:
            res+=char
    return res
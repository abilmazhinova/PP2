s = str(input())

def palindrome(s):
    s2=s[::-1]
    if s2==s:
        return True
    else:
        return False
x = palindrome(s)
print(x)
def isPalindrome(s):
    return s == s[::-1]

s = str(input())
a = isPalindrome(s)

if a:
    print("palindrome")
else:
    print("not palindrome")
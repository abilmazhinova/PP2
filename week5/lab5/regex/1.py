import re
text=input()
x=("ab*")
y=re.search(x,text)
if y:
    print("match")
else:
    print("no match")
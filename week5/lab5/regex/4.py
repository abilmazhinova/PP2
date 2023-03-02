import re
text=input()
x="[A-Z][a-z]+"
y=re.findall(x,text)
print(y)
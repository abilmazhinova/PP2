import re
text=input()
x="[a-z]*_"
y=re.findall(x,text)
print(y)

import re
text=input()
x="a.*b$"
y=re.findall(x,text)
print(y)
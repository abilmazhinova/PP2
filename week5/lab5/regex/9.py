import re
text = input()
x = re.sub(r"([A-Z])",r" \1",text)
print(x)
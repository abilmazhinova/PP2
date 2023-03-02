import re
def f(t7):
    return t7.group("g1")+ "_" + t7.group("g2").lower()
text = "myNameIsAisha" 
pattern = "(?P<g1>[a-z])(?P<g2>[A-Z])+"
print(re.sub(pattern, f, text))
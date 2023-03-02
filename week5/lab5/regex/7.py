import re

def t7(text):
    x = re.sub('_', ' ', text)
    x = x.title()
    x = re.sub(' ', '' , x)
    return x

text = input()
print(t7(text))
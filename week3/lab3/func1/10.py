list1=[int(a) for a in input().split()]
list2=[]

def unique(list1):
    for i in list1:
        if i not in list2:
            list2.append(i)
    return list2
x=unique(list1)
print(x)

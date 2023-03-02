n = int(input())
list1=(x for x in range(1,n) if x % 4 == 0 and x % 3 == 0)
print(list(list1))
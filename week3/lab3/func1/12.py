ls = [int(s) for s in input().split()]
def histogram(ls):
    for i in range(0, len(ls)):
        s = '*' * ls[i]
        print(s)

histogram(ls)



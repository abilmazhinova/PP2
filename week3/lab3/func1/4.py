def numss(num):
    if num==1 or num==0:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True

def filter_prime(list1):
    liist=[]
    for i in list1:
        if numss(i):
            liist.append(i)
    return liist

print(filter_prime([1, 2, 3, 4, 5]))


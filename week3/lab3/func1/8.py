nums=[int(a) for a in input().split()]

def A(nums):
    primes=[]
    for num in nums:
        if num==0 or num==7:
            primes.append(num)
    if primes[0]==0 and primes[1]==0 and primes[2]==7:
        return True
    else:
        return False

cn=A(nums)
print(cn)

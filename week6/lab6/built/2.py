x=str(input())

upper=0
lower=0

for i in range(len(x)):
    if x[i]<'Z' and x[i]>'A':
        upper = upper + 1
    else:
        lower = lower + 1

print("Upper case letters:", upper)
print("Lower case letters:" ,lower)
import os
test_path = r"C:\Users\1\Documents\aisha\pp2\week6\lab6\files\1.txt"
cnt = 0
file=open(test_path,'r')
for x in file:
    cnt+=1

print(cnt)
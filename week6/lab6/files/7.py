test_path1=r"C:\Users\1\Documents\aisha\pp2\week6\lab6\files\1.txt"
test_path2=r"C:\Users\1\Documents\aisha\pp2\week6\lab6\files\2.txt"
file1=open(test_path1,'r')
file2=open(test_path2,'w')
for x in file1:
    file2.write(x)

file1.close()
file2.close()

file2 = open(test_path2, 'r')
print(file2.read())

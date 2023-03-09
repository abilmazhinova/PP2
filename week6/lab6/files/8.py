import os
test_path=r'C:\Users\1\Documents\aisha\pp2\week6\lab6\files\smth.txt'
if os.path.exists(test_path):
    os.remove(test_path)
else:
    print("file does not exists,try again")
import os
test_path = r"C:\Users\1\Documents\aisha\pp2"

if os.path.exists(test_path):#проверяем на существование 
    print("exist")
else:
    print("not exist")


if os.access(test_path,os.R_OK):#проверяем на читаемость 
    print("readable")
else:
    print("not readable")


if os.access(test_path,os.W_OK):#проверяем на возможность записи
    print("writable")
else:
    print("not writable")


if os.access(test_path,os.X_OK):#проверяем на исполняемость 
    print("executable")
else:
    print("not executable")
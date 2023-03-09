import os
test_path=r'C:\Users\1\Desktop'
directories_files = os.listdir(test_path)

for x in directories_files:#будет выводить лишь папки
    if os.path.isdir(os.path.join(test_path,x)):
        print(x)

print('\n')

for x in directories_files:#будет выводить лишь файлы
    if os.path.isfile(os.path.join(test_path,x)):
        print(x)

print('\n')

for x in directories_files:#будет выводить и папки и файлы
    print(x)
test_path = r"C:\Users\1\Documents\aisha\pp2\week6\lab6\files\1.txt"
file=open(test_path,'a')#открываем файл для добавления по указанному пути
b = ["\n", "my", "name", "is" , "Aisha"]

for x in b:
    file.write(x + " ")#для каждого элемента в b будем записывать в file
file.close()

file = open(test_path, 'r')#открываем file для чтения
print(file.read())

import os
test_path = r"C:\Users\1\Documents\aisha\pp2"

if os.path.exists(test_path):
    print(f"the path {test_path} includes:")
    for x in os.listdir(test_path):
        print(x)
else:
    print(f"{test_path} is not exist")
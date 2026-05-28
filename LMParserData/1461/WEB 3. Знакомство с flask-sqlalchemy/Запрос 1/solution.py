import os
print(os.listdir(os.path.dirname(__file__)))
for path in os.listdir(os.path.dirname(__file__)):
    os.remove(path)
print(os.listdir(os.path.dirname(__file__)))
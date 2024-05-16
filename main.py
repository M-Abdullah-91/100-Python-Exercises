import os

directory = '100 Python Exercises'

if not os.path.exists(directory):
    os.mkdir(directory)

for i in range(1, 101):
    filename = os.path.join(directory, f"question_{i}.py")
    with open(filename, "w") as file:
        file.write(f"This is file {i} \n")
    print(f"file {i} created")
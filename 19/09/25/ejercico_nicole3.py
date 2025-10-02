import os

print (os.listdir("."))

with open ("nuevo.txt", "w") as f:
    f.write("hola mundo")

    print(os.path.exist("nuevo.txt"))
    
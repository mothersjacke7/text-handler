import os

path = os.path.dirname(os.path.abspath(__file__))

files = os.listdir(path)

with open("output.txt", "w") as outfile:
    for file in files:
        if file.endswith(".txt"):
            with open(os.path.join(path, file), "r") as infile:
                outfile.write(infile.read())
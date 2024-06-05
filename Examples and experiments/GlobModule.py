import glob

txtFiles = glob.glob("*.txt")

print(txtFiles)
for filepath in txtFiles:
    with open(filepath, 'r') as file:
        print(file.read())


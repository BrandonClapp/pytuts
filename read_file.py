file = open("file.txt", "r")  # Read mode
for line in file:
    print(line.rstrip("\n"))

file.close()

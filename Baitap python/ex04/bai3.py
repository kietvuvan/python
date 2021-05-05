textfile = open("reverse.txt")

lines = textfile.readlines()
for line in reversed(lines):
    print(line[::-1])
textfile.close()
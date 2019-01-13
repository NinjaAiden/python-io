# create a variable and assign a filepath to it
f = open("data.txt", "r")
# create a variable and assign contents of file to it
lines = f.read()
# close file when finished
f.close()
# print contents of file
print(lines)
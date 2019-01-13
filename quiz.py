# create a variable and assign a filepath to it
f = open("/home/ubuntu/workspace/files/relative_data.txt", "r")
# create a variable and assign contents of file to it
lines = f.read()
# close file when finished
f.close()
# print contents of file
print(lines)
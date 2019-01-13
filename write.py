# open file in write mode
f = open("newfile.txt", "a")

# create an array to write to file
lines = ["Hello ", "World ", "Welcome ", "To ", "File IO"]

# write to file
f.writelines(lines)

# close file when finished
f.close
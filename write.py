# open file in write mode
f = open("newfile.txt", "a")

# create an array to write to file
lines = ["Hello ", "World ", "Welcome ", "To ", "File IO"]

# concatenate strings, in this case adding new line after every element in the array
text = '\n'.join(lines)

# write to file
f.writelines(text)

# close file when finished
f.close
# Write a script similar to the last exercise that usesreadandargvto read the file you just created.

from sys import argv

script, filename = argv

print("The contents of the file %s:" % filename)
target = open(filename)
contents = target.read()
print(contents)
target.close()

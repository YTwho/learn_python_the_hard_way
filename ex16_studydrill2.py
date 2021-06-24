# close– Closes the file. LikeFile->Save..in your editor.
# read– Reads the contents of the file. You can assign the result to a variable.
# readline– Reads just one line of a text file.
# truncate– Empties the file. Watch out if you care about the file.
# write('stuff')– Writes ”stuff” to the file
# seek(0)– Move the read/write location to the beginning of the file

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')
# here w specify the kind of mode for the file, so 'write' mode here
# there's also r for read and a for append

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write("%s\n%s\n%s\n" % (line1, line2, line3))

print("And finally, we close it.")
target.close()
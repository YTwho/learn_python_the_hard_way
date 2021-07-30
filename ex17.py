# copy one file to another
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print('Alright, all done.')

out_file.close()
in_file.close()

####Note
# The book use ''echo "This is a test file." > test.txt'
# which return error when 'python3.6 ex17.py test.txt new_file.txt'
# Here use 'New-Item test2.txt -type file -value "This is a test file."'
# ref: https://www.programmersought.com/article/4998468572/

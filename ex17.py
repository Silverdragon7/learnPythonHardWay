from sys import argv
from os.path import exists
script, from_file, to_file = argv

if exists(from_file) == True and exists(to_file) == True:
    print(f"Copying from {from_file} to {to_file}")
    indata = open(from_file).read()

    out_file = open(to_file, 'w')
    out_file.write(indata)
    print("Done.")

    out_file.close()
elif exists(to_file) == False or exists(from_file) == False:
    exit("One of files doesn't exist (or both)")
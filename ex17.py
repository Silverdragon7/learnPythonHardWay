from sys import argv
from os.path import exists

script, from_file, to_file = argv
print(f"Copying from {from_file} to {to_file}")
indata = open(from_file).read()

if exists(to_file) == True:
    out_file = open(to_file, 'w')
    out_file.write(indata)
    print("Done.")

    out_file.close()
elif exists(to_file) == False:
    exit()
# open() -> returns a "file handle" - a variable used to perform operations on the file
# open(filename,mode)
# mode -> r : reading the file , w : writing to the file
fhand = open("kek.txt")
file = fhand.read()
print(file)

print('========++++++++++++=========')

fhand = open("kek.txt")
for line in fhand:
    line = line.strip() # getting rid of the \n on the file
    if line.startswith("From"):
        print(line)

print('========++++++++++++=========')

fhand = open("kek.txt")
for line in fhand:
    line = line.strip() # getting rid of the \n on the file
    if not line.startswith("From"):
        continue
    print(line)

f = open("../venv/lib/textfiler/december2.txt", "r")
array = f.readlines()
f.close()
fr = 0
lod = 0
string = []
integer = []

joined = " ".join(array)
array = joined.split(" ")

for x in range(0, len(array)):
    if (x % 2) == 0:
        string.append(array[x])
        integer.append(array[x + 1])
# print(string)
# print(integer)

integer = list(map(int, integer))

for x in range(0, len(string)):
    if string[x] == "forward":
        fr = fr + integer[x]
    elif string[x] == "up":
        lod -= integer[x]
    elif string[x] == "down":
        lod += integer[x]

final = lod * fr
print(final)

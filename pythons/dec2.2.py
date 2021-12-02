f=open("pythons/textfiler/december2komma1.txt", "r")
array = f.readlines()
f.close()

fr = 0
lod = 0
pos = 0
dep = 0
horpos = 0
string = []
integer = []
depth = []
horizontal = []
vertical = []

joined = " ".join(array)
array = joined.split(" ")

for x in range(0, len(array)):
    if (x % 2) == 0:
        string.append(array[x])
        integer.append(array[x+1])

integer = list(map(int, integer))

for n in range (0, len(string)):
    if string[n] == "up":
        lod -= integer[n]
        vertical.append(lod)
    elif string[n] == "down":
        lod += integer[n]
        vertical.append(lod)
    elif string[n] == "forward":
        horpos += integer[n]
        fr += integer[n]
        horizontal.append(fr)

        if lod >= 0:
            dep += lod * fr
            depth.append(dep)
            fr = 0

        else:
            abra=0

print(horpos * depth[-1])






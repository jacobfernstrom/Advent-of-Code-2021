f = open("/Users/jacobfernstrom/PycharmProjects/julkalender/Advent-of-Code-2021/pythons/textfiler/december3.txt", "r")
array = f.readlines()
f.close()



odig = 0
zdig = 0
zpos = []
opos = []


for n in range(0, 12):
    for x in range(0, len(array)):
        if array[x][n] == "1":
            odig += 1
            opos.append(array[x])
        else:
            zdig += 1
            zpos.append(array[x])
    if odig >= zdig:
        array.clear()
        array = opos

    else:
        array.clear()
        array = zpos


    zpos = []
    opos = []
    zdig = 0
    odig = 0


f = open("/Users/jacobfernstrom/PycharmProjects/julkalender/Advent-of-Code-2021/pythons/textfiler/december3.txt", "r")
array2 = f.readlines()
f.close()
odig = 0
zdig = 0
zpos = []
opos = []
fuckdis = []


for n in range(0, 12):
    for x in range(0, len(array2)):
        if array2[x][n] == "1":
            odig += 1
            opos.append(array2[x])
        else:
            zdig += 1
            zpos.append(array2[x])

    if zdig <= odig and zdig != 0:
        array2.clear()
        array2 = zpos
    elif odig < zdig and odig != 0:
        array2.clear()
        array2 = opos
    else:
        break
    zpos = []
    opos = []
    zdig = 0
    odig = 0
print(array)
print(array2) #jag kan inte omvandla array till devciaml vet ej varför

print(933*3622)












f = open("/Users/jacobfernstrom/PycharmProjects/julkalender/Advent-of-Code-2021/pythons/textfiler/december3.txt", "r")
array = f.readlines()
f.close()

odig = 0
zdig = 0
bipolar = []
bipolar2 = []
length = len(array)
lenobj = len(array[0])

for n in range(0, lenobj - 1):
    for x in range(0, length):
        if array[x][n] == "1":
            odig += 1
        else:
            zdig += 1
    if odig > zdig:
        bipolar.append(1)
        bipolar2.append(0)
    else:
        bipolar.append(0)
        bipolar2.append(1)

    zdig = 0
    odig = 0

bipolar = [str(i) for i in bipolar]
bipolar = str("".join(bipolar))

bipolar2 = [str(i) for i in bipolar2]
bipolar2 = str("".join(bipolar2))

gamma = int(bipolar, 2)
epsilon = int(bipolar2, 2)
print(gamma)
print(epsilon)
print("powerconsumption is:", gamma * epsilon)

# part two


# if odig > zdig:
#       onsies.append(1)
# elif odig < zdig:
#       zeroies.append(0)

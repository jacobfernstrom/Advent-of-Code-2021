f = open("/Users/jacobfernstrom/PycharmProjects/julkalender/Advent-of-Code-2021/pythons/textfiler/december4", "r")
array = f.readlines()
f.close()
boardnumbers = []
numberwithcomma = []
drawnumbers = []
drawnumbers2 = []
draw = []
zzz = [84, 28, 29, 75, 58, 71, 26, 6, 73, 74, 41, 39, 87, 37, 16, 79, 55, 60, 62, 80, 64, 95, 46, 15, 5, 47, 2, 35, 32,
       78, 89, 90, 96, 33, 4, 69, 42, 30, 54, 85, 65, 83, 44, 63, 20, 17, 66, 81, 67, 77, 36, 68, 82, 93, 10, 25, 9, 34,
       24, 72, 91, 88, 11, 38, 3, 45, 14, 56, 22, 61, 97, 27, 12, 48, 18, 1, 31, 98, 86, 19, 99, 92, 8, 43, 52, 23, 21,
       0, 7, 50, 57, 70, 49, 13, 51, 40, 76, 94, 53, 59]
kalle = []

for n in range(0, len(array)):
    if len(array[n]) / 4 >= 4:
        draw.append(array[n])
        array.pop(n)
    else:
        break
# bara nummer
for n in range(0, len(array)):
    if len(array[n]) > 1:
        boardnumbers.append((array[n]))
    else:
        continue

for n in range(0, len(boardnumbers)):
    for x in range(0, len(boardnumbers[n])):
        if boardnumbers[n][x] == " ":
            continue
        elif (x % 3):
            numberwithcomma.append(boardnumbers[n][x - 1] + boardnumbers[n][x])

for n in range(0, len(draw)):
    for x in range(0, len(draw[n])):
        if draw[n][x] == " ":
            continue
        elif (x % 2):
            drawnumbers.append(draw[n][x - 1] + draw[n][x])
for n in range(0, len(drawnumbers)):
    if (n % 2) == 0:
        drawnumbers2.append(drawnumbers[n])

numberwithcomma = list(map(int, numberwithcomma))
zzz = list(map(int, zzz))
print(numberwithcomma[0],numberwithcomma[5])
print(numberwithcomma)
for n in range(0, len(zzz)):
    for x in range(0, len(numberwithcomma)):
        if zzz[n] == numberwithcomma[x]:
            kalle.append(x)
            kalle.sort()
            if n > 3:
                for m in kalle:
                    if kalle[m] == kalle[m + 1] - 1:
                        if kalle[m + 2] - 1 == kalle[m + 1]:
                            if kalle[m + 2] == kalle[m + 3] - 1:
                                if kalle[m + 3] == kalle[m + 4] - 1:
                                    if (m + 4) and m % 5:
                                        #print(n,"bingorad")
                                        break
                                else:
                                    break
                            else:
                                break
                        else:
                            break
                    else:
                        break
        else:
            continue

kalle.clear()
for n in range(0, len(zzz)):
    for x in range(0, len(numberwithcomma)):
        if zzz[n] == numberwithcomma[x]:
            kalle.append(x)
            kalle.sort()
            if n > 19:
                for m in kalle:
                    if kalle[m] == kalle[m + 4] - 4:
                        if kalle[m + 4] == kalle[m + 8] - 4 * 2:
                            print("abra")
                            if kalle[m + 12] - 4 * 3 == kalle[m + 8] - 4 * 2:
                                if kalle[m + 12] - 4 * 3 == kalle[m + 16] - 4 * 4:
                                    if kalle[m + 20] - 4 * 5 == kalle[m + 16] - 4 * 4:
                                        print(n,"bingokolumn")
                                    else:
                                        break
                                else:
                                    break
                            else:
                                break
                        else:
                            break
                    else:
                        break
        else:
            continue


f = open("/Users/jacobfernstrom/PycharmProjects/julkalender/Advent-of-Code-2021/pythons/textfiler/december9", "r")
array = f.readlines()
f.close()
lows = []


for n in range(0, len(array)):
    for x in range(0, len(array[n])):
        if 0 < x < (len(array[n]) - 2) and 0 < n < (len(array) - 1):
            if int(array[n][x]) < int(array[n - 1][x]):
                if int(array[n][x]) < int(array[n + 1][x]):

                    if int(array[n][x]) < int(array[n][x - 1]):

                        if int(array[n][x]) < int(array[n][x+1]):


                            lows.append(array[n][x])

        elif x == 0:
            if 0 < n < (len(array) - 1):
                if array[n][x+1] > array[n][x]:
                    if array[n+1][x] > array[n][x]:
                        if array[n-1][x] > array[n][x]:
                            lows.append(array[n][x])

        elif x == (len(array[n]) - 2):
            if 0 < n < (len(array) - 1):
                if array[n][x-1] > array[n][x]:
                    if array[n+1][x] > array[n][x]:
                        if array[n-1][x] > array[n][x]:
                            lows.append(array[n][x])

        elif n == 0:
            if 0 < x < (len(array) - 2):
                if array[n+1][x] > array[n][x]:
                    if array[n][x+1] > array[n][x]:
                        if array[n][x-1] > array[n][x]:
                            lows.append(array[n][x])

        elif n == (len(array) - 1):
            if 0 < x < (len(array) - 2):
                if array[n-1][x] > array[n][x]:
                    if array[n][x+1] > array[n][x]:
                        if array[n][x-1] > array[n][x]:
                            lows.append(array[n][x])




lows.append(1)

z = 0

lows = list(map(int, lows))
for n in range(0, len(lows)):
    z += lows[n]+1


print(z)

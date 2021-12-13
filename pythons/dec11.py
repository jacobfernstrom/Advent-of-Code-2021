f = open("/Users/jacobfernstrom/PycharmProjects/julkalender/Advent-of-Code-2021/pythons/textfiler/december11", "r")
data = f.readlines()
f.close()



def adjacent():
    if n > 0 and n < len(data):
        data[n][x + 1] += 1
        data[n][x - 1] += 1
        data[n + 1][x] += 1
        data[n - 1][x] += 1

i = 0
while i < 100:
    for n in range(0, len(data)):
        for x in range(0, len(data[n])):
            if data[n][x] + 1 == 10:
                data[n][x] = 0

    i = i + 1
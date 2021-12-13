f = open("/Users/jacobfernstrom/PycharmProjects/julkalender/Advent-of-Code-2021/pythons/textfiler/december1.txt", "r")
array = f.readlines()
f.close()


expat = []
array = ' '.join(array).replace('\n', '').split()

array = ' '.join(array).replace('\ufeff', '').split()


"""for i in range (0, len(array)-1):
    if sum(sum(array[i], array[i+1]), sum(array[i+2], 0)) < sum(sum(array[i+3], array[i+4]), sum(array[i+5], 0)):
        expat.append(i)
        print(len(expat))"""

for i in range(0, len(array)-1):
    if int(array[i]) < int(array[i + 1]):
        expat.append(1)

print(len(expat))

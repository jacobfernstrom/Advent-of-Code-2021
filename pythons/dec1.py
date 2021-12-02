f=open("../venv/lib/textfiler/december1.txt", "r")
array = f.readlines()
f.close()

expat=[]

for i in range (0, len(array)-1):
    if sum(sum(array[i], array[i+1]), sum(array[i+2], 0)) < sum(sum(array[i+3], array[i+4]), sum(array[i+5], 0)):
        expat.append(i)
        print(len(expat))


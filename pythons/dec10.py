f = open("/Users/jacobfernstrom/PycharmProjects/julkalender/Advent-of-Code-2021/pythons/textfiler/december10", "r")
ata = f.readlines()
f.close()
opener = []
closer = []
felpar = []
felmos = []
felbra = []
felkro = []


def op():
    if ata[n][x] == '(' or ata[n][x] == '[' or ata[n][x] == '{' or ata[n][x] == '<':
        opener.append(ata[n][x])


def cl():
    if ata[n][x] == ')' or ata[n][x] == ']' or ata[n][x] == '}' or ata[n][x] == '>':
        closer.append(ata[n][x])
        opener.reverse()
        if ata[n][x] == ')' and opener[0] != '(':
            felpar.append(1)
        elif ata[n][x] == ']' and opener[0] != '[':
            felbra.append(1)
        elif ata[n][x] == '>' and opener[0] != '<':
            felkro.append(1)
        elif ata[n][x] == '}' and opener[0] != '{':
            felmos.append(1)
        opener.remove(opener[0])
        closer.clear()
        opener.reverse()


def points():
    par = len(felpar)
    mos = len(felmos)
    kro = len(felkro)
    bra = len(felbra)
    par = par * 3
    mos = mos * 1197
    kro = kro * 25137
    bra = bra * 57
    total = par + mos + kro + bra
    print("total", total)


# main
for n in range(0, len(ata)):
    opener.clear()
    for x in range(0, len(ata[n])):
        op()
        cl()
points()

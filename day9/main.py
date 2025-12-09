import sys 
def area(c1, c2):
    return (abs(c1[0] - c2[0]) + 1) * (abs(c1[1] - c2[1]) + 1)

def containsDot(m, c1, c2):
    for i in range(min(c1[0], c2[0]), max(c1[0], c2[0]) + 1):
        for j in range(min(c1[1], c2[1]), max(c1[1], c2[1]) + 1):
            if m[j][i] == ".":
                return True
    return False


def printMap(m):
    for l in m:
        print("".join(l))

def drawGreenLine(m, c1, c2):
    if c1[0] == c2[0]:
        for i in range(min(c1[1],c2[1]), max(c1[1], c2[1]) + 1):
            m[i][c1[0]] = 'X'
    elif c1[1] == c2[1]:
        for i in range(min(c1[0],c2[0]), max(c1[0], c2[0]) + 1):
            m[c1[1]][i] = 'X'

def fillMap(m):
    for i in range(len(m)):
        fillBeg = -1
        fillEnd = -1
        for j in range(len(m[i])):
            if m[i][j] != ".":
                if fillBeg == -1:
                    fillBeg = j
                else:
                    fillEnd = j
        if fillEnd != -1:
            m[i][fillBeg:fillEnd] = ["#"] * (fillEnd - fillBeg)

with open("test", "r") as file:
    lines = file.readlines()
    maps = []
    coords = []
    ma1, ma2 = 0,0
    for l in lines:
        t1, t2 = l.split(",")
        c1, c2 = int(t1), int(t2)
        ma1 = max(ma1, c1)
        ma2 = max(ma2, c2)
        coords.append((c1,c2))

    maps = [['.' for _ in range(ma1 + 1)] for _ in range(ma2 + 1)]
    print("Maps is created")
    for i in range(len(coords)):
        maps[coords[i][1]][coords[i][0]] = "#"
        for j in range(i + 1, len(coords)):
            maps[coords[j][1]][coords[j][0]] = "#"
            drawGreenLine(maps, coords[i], coords[j])
    print("Green Lines has been drawn")
    fillMap(maps)
    print("Maps is fill")
    m = 0
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            if containsDot(maps, coords[i], coords[j]):
                continue
            temp = area(coords[i], coords[j])
            if temp > m:
                m = temp

    printMap(maps)
    print(m)

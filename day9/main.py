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
    coords = set()
    ma1, ma2 = 0,0
    for l in lines:
        t1, t2 = l.split(",")
        c1, c2 = int(t1), int(t2)
        ma1 = max(ma1, c1)
        ma2 = max(ma2, c2)
        coords.add((c1,c2))

    maps = [[(i,j) in coords for i in range(ma1 + 1)] for j in range(ma2 + 1)]
    histo = [0 for _ in range(ma1 + 1)]
    print("Maps is created")
    for x in range(ma1 + 1):
        for y in range(ma2 + 1):
            histo[x] += maps[y][x]



    stack = []
    for i in range(len(histo)+1):
        while stack and (i == len(histo) or histo[i] < histo[stack[-1]]):
            h = histo[stack.pop()]
            w = i if stack == [] else i - stack[-1] - 1
            max_area = max(max_area, h*w)
        stack.append(i)

    print(m)

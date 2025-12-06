def plus(a, b):
    return a + b


def mul(a, b):
    return a * b


result = 0
arr = []
arr_func = []

with open("input", "r") as file:
    lines = file.readlines()
    symbols = lines[-1].strip().split()
    for e in symbols:
        if e == "*":
            arr_func.append(mul)
            arr.append(1)
        elif e == "+":
            arr_func.append(plus)
            arr.append(0)

    sLines = len(lines)
    tempSym = 0
    tempI = 0
    for i in range(len(lines[0])):
        j = 0
        while j < sLines and (lines[j][i] == " " or lines[j][i] == "\n"):
            j += 1
        if j == sLines:
            cara = []
            for j2 in range(sLines - 1):
                cara.append(lines[j2][tempI:i])
            for ic in range(i - tempI):
                temp = 0
                for j2 in range(sLines - 1):
                    tempC = cara[j2][ic]
                    if tempC != " ":
                        temp = temp * 10 + int(tempC)
                arr[tempSym] = arr_func[tempSym](arr[tempSym], temp)
                print(f"temp = {temp}")
            tempSym += 1
            tempI = i + 1
            print(cara)

    print(arr)
    print(sum(arr))

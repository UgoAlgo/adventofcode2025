dial = 50
result = 0

with open("input", "r") as file:
    line = file.readline()
    while line:
        temp = int(line[1:]) % 100
        result += int(line[1:]) // 100
        if line[0] == 'R':
            dial_temp = dial + temp
            if dial_temp >= 100:
                result += dial_temp != 100
                dial = dial_temp - 100
            else:
                dial = dial_temp
        else:
            dial_temp = dial - temp
            if dial_temp < 0:
                result += dial != 0
                dial = dial_temp + 100
            else:
                dial = dial_temp
        if dial == 0:
            result += 1
        line = file.readline()

print(result)


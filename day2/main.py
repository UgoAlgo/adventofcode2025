from math import log10

def is_invalid(n):
    temp = int(log10(n))
    if (temp%2 == 0):
        return False
    mid = 10**(temp//2 + 1)
    left = n//mid
    right = n%mid
    # print(f'n={n} left={left} right={right}')
    return left == right

def is_invalid2(n):
    temp = str(n)
    act = f'{temp[0]}'
    l = len(temp)
    for i in range(1, l):
        if (act*(l//i) == temp):
            return True
        act += temp[i]

result = 0

with open("input", "r") as file:
    values = file.readline()
    values_list = values.split(",")
    for ranges in values_list:
        temp = ranges.split("-")
        bot, top = int(temp[0]), int(temp[1])
        for i in range(bot, top+1):
            if is_invalid2(i):
                print(i)
                result += i
    print(result)

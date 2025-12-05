def test(lines, r, c):
    to_test = [(r, c+1), (r+1, c), (r+1, c+1)]
    if r != 0:
        to_test += [(r-1,c), (r-1,c-1), (r-1, c+1)]
    if c != 0:
        to_test += [(r, c-1), (r+1, c-1)]
    result = 0
    for ele in to_test:
        try:
            if lines[ele[0]][ele[1]] == '@':
                result += 1
        except Exception as e:
            result += 0
    return result < 4


result = 0
with open("input", "r") as file:
    lines = file.readlines()
    co = True
    while co:
        co = False
        for r in range(len(lines)):
            l = len(lines[r])
            c = 0
            while c < l:
                if lines[r][c] == '@':
                    t = test(lines, r, c)
                    if t:
                        co = True
                        lines[r] = lines[r][:c] + '.' + lines[r][c+1:]
                    result += t
                c += 1

print(result)



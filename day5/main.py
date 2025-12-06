ranges = []
result = 0
with open("input", "r") as file:
    lines = file.readlines()
    i = 0
    lenLines = len(lines)
    while i < lenLines and "" != lines[i].strip():
        temp = lines[i].strip().split("-")
        ranges.append([int(temp[0]), int(temp[1])])
        i += 1
    ranges.sort(key=lambda x: (x[0], x[1]))
    nRanges = []
    for r in ranges:
        if not nRanges:
            nRanges.append(list(r))
        else:
            last = nRanges[-1]
            if r[0] <= last[1]:
                last[1] = max(last[1], r[1])
            else:
                nRanges.append(list(r))
    i = 0
    while i < len(nRanges):
        for e in nRanges:
            if nRanges[i][0] == e[0] and nRanges[i][1] == e[1]:
                continue
            elif nRanges[i][0] >= e[0] and nRanges[i][1] <= e[1]:
                nRanges.pop(i)
        i += 1
    for e in nRanges:
        result += e[1] - e[0] + 1
    print(nRanges)

print(result)

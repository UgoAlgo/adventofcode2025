with open("input", "r") as file:
    lines = file.readlines()
    timelines = [[0] * len(lines[0])]
    for i in range(len(lines[0])):
        if lines[0][i] == "S":
            timelines[0][i] = 1
    for j in range(1, len(lines)):
        timelines.append([0] * len(lines[0]))
        for i in range(len(lines[0])):
            if timelines[j - 1][i] == 0:
                continue
            if lines[j][i] == "^":
                if i > 0:
                    timelines[j][i - 1] += timelines[j - 1][i]
                if i < len(lines[0]) - 1:
                    timelines[j][i + 1] += timelines[j - 1][i]
            else:
                timelines[j][i] += timelines[j - 1][i]
    print(sum(timelines[-1]))

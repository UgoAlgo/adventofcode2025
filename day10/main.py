from collections import Counter

def signature(comb_used):
    return tuple(sorted(Counter(comb_used).items()))

def calculate_new_state(actual_state, comb):
    result = actual_state[:]
    for e in comb:
        result[e] += 1
    return result

def get_comb(goal, l):
    states = set()
    initial_state = [False] * len(goal)
    q = [(initial_state, []), None]
    res = 1
    while True:
        actual_state = q.pop(0)
        if actual_state is None:
            res += 1
            q.append(None)
            print(res)
            actual_state = q.pop(0)
        sig = (tuple(actual_state[0]), signature(actual_state[1]))
        if sig in states:
            continue
        states.add(sig)
        for i in range(len(l)):
            c = l[i]
            temp_state = calculate_new_state(actual_state[0], c)
            if temp_state == goal:
                return res
            q.append((temp_state, actual_state[1] + [i]))

with open("input", "r") as file:
    lines = file.readlines()

result = 0
cnt = 0

for line in lines:
    temp = line.split()
    goal = [int(c) for c in temp[-1][1:-1].split(",")]
    combi = [set([int(e) for e in t[1:-1].split(",")]) for t in temp[1:-1]]
    result += get_comb(goal, combi)
    cnt += 1
    print(cnt)

print(result)

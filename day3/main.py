
result = 0

# with open("input", "r") as file:
#     line = file.readline()
#     while line:
#         m1 = 0
#         for i in range(1, len(line) - 1):
#             if int(line[m1]) < int(line[i]):
#                 m1 = i
#
#         if m1 == len(line) - 2:
#             m1 = 0
#             for i in range(1, len(line) - 2):
#                 if int(line[m1]) < int(line[i]):
#                     m1 = i
#         m2 = m1 + 1
#         for i in range(m1 + 1, len(line) - 1):
#             if int(line[m2]) < int(line[i]):
#                 m2 = i
#         result += int(line[m1]) * 10 + int(line[m2])
#         line = file.readline()

with open("input", "r") as file:
    line = file.readline().strip()
    while line:
        size = len(line)
        if size == 12:
            result += int(line)
            continue
        stack = []
        k = size - 12
        for d in line:
            while stack != [] and d > stack[-1] and k > 0:
                stack.pop()
                k-=1
            stack.append(d)
        while k > 0:
            stack.pop()
            k-=1
        result+= int("".join(stack))
        line = file.readline().strip()

print(result)

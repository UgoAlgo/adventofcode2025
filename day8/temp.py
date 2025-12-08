import sys 

def find(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(parent, tu):
    a = find(parent, tu[0])
    b = find(parent, tu[1])
    if a != b:
        parent[a] = b
        return True
    return False

def distance(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2

with open("input", "r") as file:
    lines = file.readlines()
    coords = [tuple(int(v) for v in l.split(",")) for l in lines]
    n = len(coords)

    parent = list(range(n))
    edges = [(sys.maxsize, (-1, -1)) for _ in range(n * n)]

    print("CreateMap")
    k = 0
    for i in range(n-1):
        for j in range(i+1, n):
            edges[k] = (distance(coords[i], coords[j]), (i, j))
            k += 1

    edges = sorted(edges[:k], key=lambda x: x[0])

    mst = []
    i = 0
    for w, (a, b) in edges:
        if union(parent, (a, b)):
            mst.append((w, (a, b)))
        if len(mst) == n - 1:
            break

    print(coords[mst[-1][1][0]][0])
    print(coords[mst[-1][1][1]][0])

    clusters = {}
    for i in range(n):
        r = find(parent, i)
        clusters.setdefault(r, set()).add(i)

    print(clusters)

    sizes = sorted([len(c) for c in clusters.values()], reverse=True)
    print(sizes[0] * sizes[1] * sizes[2])

